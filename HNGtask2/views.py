from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.

def home(request):
    form = ContactForm()
    return render(request, 'index.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Resume Enquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com',
                          'admin@example.com')
                # messages.success(request, 'messages.html')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return redirect("home")
        # messages.error(request, "Error. Message not sent.")

    form = ContactForm()
    return render(request, "index.html", {'form': form})
