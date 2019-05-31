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
            'content': "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )