from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.conf import settings

from .forms import ContactForm
from django.http import HttpResponse

import csv

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Building Email
            subject = render_to_string(
                'contact/emails/email_subject.txt',
                {'name': name, 'subject': subject})
            body = render_to_string(
                'contact/emails/email_body.txt',
                {'name': name,
                 'email': email,
                 'message': message
                })
            # Sending Email
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})

    return render(request, 'contact/contact.html')

def success(request):
    return render(request, 'contact/success.html')
