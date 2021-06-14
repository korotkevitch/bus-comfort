from django import forms
from django.core.mail import send_mail as django_send_mail
from django.forms import ModelForm
from .models import Contact

class UserForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def send_mail(self):
        return django_send_mail('Сообщение с сайта bus-comfort.by',
                    str('Имя: ') + self.cleaned_data['f_name'] + '\n' + str('Фамилия: ') + self.cleaned_data['l_name'] +
                                '\n' + str('Емейл: ') + self.cleaned_data['email'] + '\n' + str('Тема: ') +
                                self.cleaned_data['subject'] + '\n' + str('Сообщение: ') + self.cleaned_data['message'],
                    'no-reply@bus-comfort.by',
                    ['info@iko-studio.com'])