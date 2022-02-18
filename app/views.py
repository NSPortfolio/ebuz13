from django.shortcuts import render
from app import forms

def indexpage(request):
    return render(request,'templates/index.html')

def homepage(request):
    return render(request,'templates/homepage.html')

def websites(request):
    post_form = forms.PostOrganization()
    return render(request, 'templates/mywebsite.html', {
        "post_form": post_form,
    })

def example(request):
    post_form = forms.PostOrganization()
    return render(request, 'templates/web.html', {
        "post_form": post_form,
    })

def search(request):
    return render(request, 'templates/search.html')
