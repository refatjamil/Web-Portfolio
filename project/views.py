from django.shortcuts import render

# Create your views here.
def project(request):

    context = {'pactive' : 'active'}

    return render(request,"project/project.html",context)