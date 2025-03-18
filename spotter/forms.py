from django import forms

class Correct_value(forms.Form):
    correct_value = forms.CharField(label="Введіть корегувальне значення в мм.", max_length=200)


class Number_value(forms.Form):
    number_value = forms.CharField(label="Введіть значення на дісплею датчика", max_length=200)


