import urllib
import json
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm


def index(request):
    """
    Function for rendering the main home page
    """
    return render(request, "home/index.html")


def about(request):
    """
    Function for rendering the about page
    """
    return render(request, "home/about.html")


def delivery_info(request):
    """
    Function for rendering the delivery information page
    """
    return render(request, "home/delivery_info.html")


def contact(request):
    """
    Function for the contact page, which allows users to email PowerHaus.
    reCAPTCHA verfication adapted from the excellent article by Vitor Freitas:
    https://simpleisbetterthancomplex.com/tutorial/2017/02/21/how-to-add-recaptcha-to-django-site.html
    """
    # Variable is sent to the template as a hidden field,
    # which the JS will pick up
    # to determine if the message confirmation modal should fire
    fire_modal = False

    if request.method == 'POST':
        form_data = {
            "first_name": request.POST.get("fname", ""),
            "last_name": request.POST.get("lname", ""),
            "email": request.POST.get("email", ""),
            "message_subject": request.POST.get("subjectSelection", ""),
            "order_number": request.POST.get("orderNum", ""),
            "message": request.POST.get("message", "")
        }
        contact_form = ContactForm(form_data)

        if contact_form.is_valid():

            # reCAPTCHA validation
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())

            # Only send email if reCAPTCHA response was successful
            if result['success']:
                send_mail(
                    form_data['message_subject'],
                    form_data['message'],
                    form_data['email'],
                    ['info@powerhaus.com'],
                    fail_silently=False
                )
                fire_modal = True
            else:
                messages.error(request, "Invalid reCAPTCHA. Please try again.")
        else:
            messages.error(request,
                           "Sorry, something went wrong! Please try again.")

    context = {
        "captcha_key": settings.RECAPTCHA_PUBLIC_KEY,
        "fire_modal": fire_modal
    }

    return render(request, "home/contact.html", context=context)
