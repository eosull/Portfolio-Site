from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponse

import csv

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            file = open('responses.csv', 'a')
            writer = csv.writer(file)
            writer.writerow([name,email,message])
            file.close()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})

    return render(request, 'contact/contact.html')

def success(request):
    return render(request, 'contact/success.html')

