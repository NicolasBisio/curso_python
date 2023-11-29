from django import forms

class User_Form(forms.Form):
    name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

class User_Form_Search(forms.Form):
    name = forms.CharField()
    
class Product_Form(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()

class Product_Form_Search(forms.Form):
    title = forms.CharField()

class Cart_Form(forms.Form):
    user = forms.CharField()
    products = forms.CharField()

class Cart_Form_Search(forms.Form):
    user = forms.CharField()