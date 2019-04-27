from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('What sin do you like the best?')
    #return render(request, 'polls/sinpoll.html',{})
