from unicodedata import name
from django.shortcuts import render
from . models import Message
# Create your views here.

def contact(request):
    context = {'cactive' : 'active'}

    if request.method == 'POST':
        v_Name = request.POST.get('inputName')
        v_Email = request.POST.get('inputEmail')
        v_Subject = request.POST.get('inputSubject')
        v_Message = request.POST.get('inputMessage')
        if v_Name != '' and v_Email != '' and v_Subject !='' and v_Message != '':

            Message.objects.create(m_Name=v_Name, m_Email=v_Email, m_Subject=v_Subject, m_Message=v_Message)
    return render(request, 'contact/contact.html',context)   
