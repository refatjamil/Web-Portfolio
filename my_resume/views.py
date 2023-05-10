from django.shortcuts import render, redirect
# Create your views here.

# def home(request):
    # if request.method == 'POST':
    #     fm = Mode(request.POST)
    #     fm.save()
    # else:     
    #     fm = Mode()   

    # context = {'hactive' : 'active'}
    # return render(request,'my_resume/home.html',context)



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