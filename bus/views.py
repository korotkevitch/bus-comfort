from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseRedirect
from bus.models import Head, Contact
from .forms import UserForm
from django.views.generic.edit import FormView
from django.core.mail import send_mail


class IndexView(ListView):
    context_object_name = 'index'
    template_name = 'index.html'
    queryset = Head.objects.all()


class ContactView(FormView):
    model = Contact
    form_class = UserForm
    success_url = '/thanks'

    def form_valid(self, myform):
        myform.send_mail()
        myform.save()  # сохранение в БД
        return super().form_valid(myform)

