#coding:utf-8
from django import forms 

class UploadFileForm(forms.Form):
    f = forms.FileField()
