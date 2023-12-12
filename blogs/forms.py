from django import forms

class Create_Blog_Form(forms.Form):
    title = forms.CharField()
    subtitle = forms.CharField()
    body = forms.CharField()
    author = forms.CharField()
    date = forms.DateField()
    image = forms.ImageField()

class Blog_Form_Search(forms.Form):
    title = forms.CharField()