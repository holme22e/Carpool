from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    # if request.method == "POST":
    #     print ("in home_page")
    #     return redirect('/user/')
        # return HttpResponse(request.POST['first_name_text'])
    return render(request, 'base.html')

def user_page(request):
    print ("in user_page")

    #return render(request, 'index.html')
    return HttpResponse(request.POST['first_name_text'])
