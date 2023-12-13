from django import forms

class Create_Blog_Form(forms.Form):
    title = forms.CharField()
    subtitle = forms.CharField()
    body = forms.CharField()
    author = forms.CharField()
    date = forms.CharField()
    #image_URL = forms.CharField()

class Blog_Form_Search(forms.Form):
    title = forms.CharField()