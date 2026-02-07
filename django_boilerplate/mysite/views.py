from django.http import HttpResponse

def home(request):
    return HttpResponse("Django Server Running Successfully")
