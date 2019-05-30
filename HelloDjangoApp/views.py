from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

#def index(request):
#    return HttpResponse("Hello, Django!")

# this function renders the html response 
def index(request):
    now = datetime.now()

    html_content = "<html><head><title>Hello, Django</title></head><body>"
    html_content += "<strong>My HTML text!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
    html_content += "</body></html>"

    return HttpResponse(html_content)