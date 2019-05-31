from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

#def index(request):
#    return HttpResponse("Hello, Django!")

# this function renders the html  
 
from django.shortcuts import render   # Added for this step

def index(request):
    now = datetime.now()

    return render(
        request,
        "HelloDjangoApp/index.html",  # Relative path from the 'templates' folder to the template file
        
        {
            'title' : "My Really Sweet Website",
            'message' : "Hello Everybody! ",
            'content': " The current time and date is... " + now.strftime("%A, %d %B, %Y at %X")
        }
    )

def about(request):
    return render(
        request,
        "HelloDjangoApp/about.html",
        {
            'title' : "My About Page Title",
            'content' : "My App Page Content"
        }
    )