from django.shortcuts import render

# Create your views here.

def home(request):
    context = {'hactive' : 'active'}
    return render(request,'my_resume/home.html',context)
