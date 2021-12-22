from django.shortcuts import render

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import forms


def contact(request):
    if request.method == 'GET':
        form = forms.ContactForm()
    else:
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ['admin@ForestForLife.co.uk'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('support:success')
    return render(request, "email.html", {'form': form})


def success(request):
    return render(request, "success.html")
