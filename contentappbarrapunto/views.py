from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotFound
from models import Put_App
from xmlbarrapunto import getNews
from django.core.cache import caches


cache = caches['default']


def updateNews(request):
    news = getNews()
    cache.set('news', news)
    return HttpResponse("News updated<br>")


@csrf_exempt
def processRequest(request, resource):
    if request.method == "GET":
        try:
            content = Put_App.objects.get(titulo=resource)
            news = cache.get('news')
            if news == None:
                news = getNews()
                cache.set('news', news)
            return HttpResponse(content.content + news)
        except Put_App.DoesNotExist:
            return HttpResponseNotFound(resource + " not found")
    elif request.method == "PUT":
        newContent = Put_App(titulo=resource, contenido=request.body)
        newContent.save()
        return HttpResponse(resource + " added to the list")
    else:
        return HttpResponse(status=403)
