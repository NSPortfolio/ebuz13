from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from app.models import Post

class PostOrganization(forms.ModelForm):
    website = forms.CharField(required=True)
    area = forms.CharField(required=True)
    update = forms.CharField(widget=forms.Textarea, required=False)
    recentevent = forms.CharField(widget=forms.Textarea, required=False)
    file = forms.FileField()

    class Meta:
        model = Post
        fields = ('name_of_organization', 'organization', 'interest', 'website', 'yes', 'file', 'area', 'communication', 'description', 'looking', 'update', 'recentevent',)

