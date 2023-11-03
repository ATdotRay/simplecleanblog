from django import forms 

class EmailForm(forms.Form):
    email = forms.EmailField(label="Email address")
    name = forms.CharField(label="Name")
    message = forms.CharField(label="Your message", widget=forms.Textarea(attrs={"rows": 3}))