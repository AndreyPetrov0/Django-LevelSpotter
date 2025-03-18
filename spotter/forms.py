from django import forms

class CreateNewList(forms.Form):
    nameSSS = forms.CharField(label="Name", max_length=200)
