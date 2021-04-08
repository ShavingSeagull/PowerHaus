from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
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
    Function for the contact page, which allows users to email PowerHaus
    """
    # Variable is sent to the template as a hidden field, which the JS will pick up 
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
            send_mail(
                form_data['message_subject'],
                form_data['message'],
                form_data['email'],
                ['info@powerhaus.com'],
                fail_silently=False
            )
        
            fire_modal = True
        else:
            messages.error(request, "Sorry, something went wrong! Please try again.")

    return render(request, "home/contact.html", {"fire_modal": fire_modal})
