from django.shortcuts import render, redirect

# Create your views here.



def project(request):
    if request.COOKIES.get('mode') == 'dark':
        dark_mode = True
    else:
        dark_mode = False
    context = {'pactive' : 'active', 'dark_mode': dark_mode}
    return render(request,'project/project.html',context)

def toggle_mode(request):
    if request.COOKIES.get('mode') == 'dark':
        response = redirect(request.META.get('HTTP_REFERER'))
        response.set_cookie('mode', 'light')
    else:
        response = redirect(request.META.get('HTTP_REFERER'))
        response.set_cookie('mode', 'dark')
    return response