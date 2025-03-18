from django import forms

class CreateNewList(forms.Form):
    nameSSSS = forms.CharField(label="Name", max_length=200)
