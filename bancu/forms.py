from django import forms

class SaqueForm(forms.Form):
    valor = forms.IntegerField(label='Digite o valor do saque: ')