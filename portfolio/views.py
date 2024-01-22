from django.shortcuts import render, redirect
from .models import Message


def home(request):
    if request.COOKIES.get('mode') == 'dark':
        dark_mode = True
    else:
        dark_mode = False
    context = {'hactive' : 'active', 'dark_mode': dark_mode}
    return render(request,'my_resume/home.html',context)

def toggle_mode(request):
    if request.COOKIES.get('mode') == 'dark':
        response = redirect(request.META.get('HTTP_REFERER'))
        print(response, '----------')
        response.set_cookie('mode', 'light')
    else:
        response = redirect(request.META.get('HTTP_REFERER'))
        response.set_cookie('mode', 'dark')
    return response

def skill(request):
    if request.COOKIES.get('mode') == 'dark':
        dark_mode = True
    else:
        dark_mode = False
    context = {'sactive' : 'active', 'dark_mode': dark_mode}
    return render(request,'my_resume/skill.html',context)


def project(request):
    if request.COOKIES.get('mode') == 'dark':
        dark_mode = True
    else:
        dark_mode = False
    context = {'pactive' : 'active', 'dark_mode': dark_mode}
    return render(request,'my_resume/project.html',context)


def contact(request):
    context = {'cactive' : 'active'}

    if request.method == 'POST':
        v_Name = request.POST.get('inputName')
        v_Email = request.POST.get('inputEmail')
        v_Subject = request.POST.get('inputSubject')
        v_Message = request.POST.get('inputMessage')
        if v_Name != '' and v_Email != '' and v_Subject !='' and v_Message != '':

            Message.objects.create(m_Name=v_Name, m_Email=v_Email, m_Subject=v_Subject, m_Message=v_Message)
    return render(request, 'my_resume/contact.html',context) 







