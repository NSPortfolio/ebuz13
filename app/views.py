from django.shortcuts import render
from app import forms

def indexpage(request):
    return render(request,'index.html')

def homepage(request):
    return render(request,'homepage.html')

def websites(request):
    post_form = forms.PostOrganization()
    return render(request, 'mywebsite.html', {
        "post_form": post_form,
    })

def example(request):
    post_form = forms.PostOrganization()
    return render(request, 'web.html', {
        "post_form": post_form,
    })

def search(request):
    return render(request, 'search.html')
