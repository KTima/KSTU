from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import *
from django.forms import  DateInput, ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин',widget=forms.TextInput(attrs = { 'class':'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['images','tittle','full_text','date']

        widgets = {
            'date':DateInput(attrs = {'type':'date'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))


class ProgrammsForm(ModelForm):
    class Meta:
        model = Programms
        fields = ['tittle','date','length','location','set']

        widgets = {
            'date':DateInput(attrs = {'type':'date'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))