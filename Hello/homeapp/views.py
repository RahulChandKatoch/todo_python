from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context ={
        'variable1':'Harry is great',
        'variable2':'Rohan is great'
    }
    return render(request,'index.html',context)
    # return HttpResponse('this is the home page')


def about(request):
    # return HttpResponse('this is about page')
    return render(request,'about.html')


def services(request):
    # return HttpResponse('this is services page')
    return render(request,'services.html')


def contact(request):
    # return HttpResponse('this is contact page')
    return render(request,'contact.html')
