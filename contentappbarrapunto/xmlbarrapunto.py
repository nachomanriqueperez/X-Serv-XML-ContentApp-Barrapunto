#!/usr/bin/python

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import string


class headerHandler(ContentHandler):

    def __init__(self):
        self.inContent = False
        self.theContent = ""
        self.inItem = False
        self.title = ""
        self.html = ""

    def startElement(self, name, attrs):
        if name == "item":
            self.inItem = True
        elif self.inItem:
            if name == "title" or name == "link":
                self.inContent = True

    def endElement(self, name):
        if name == "item":
            self.inItem = False
        elif self.inItem:
            if name == "title":
                self.title = self.theContent
                self.inContent = False
                self.theContent = ""
            elif name == "link":
                self.html += "Title: <a href=" + self.theContent + ">" +\
                            self.title + "</a><br/>"
                self.inContent = False
                self.theContent = ""

    def characters(self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars


def getNews():
    parser = make_parser()
    handler = headerHandler()
    parser.setContentHandler(handler)
    parser.parse("http://barrapunto.com/index.rss")
    return  "<br><hr>" + handler.html
