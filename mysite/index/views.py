##   return HttpResponse(f'Hello, world. {request}')

##from django.http import HttpResponse


##def index(request):
##    return HttpResponse("Hello, world.You' re at the polls index {request}")

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.You' re at the polls index {request}")