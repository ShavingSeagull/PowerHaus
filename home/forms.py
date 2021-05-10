from django import forms

SUBJECT_CHOICES = [
    ('generalEnquiry', 'General Enquiry'),
    ('feedback', 'Feedback'),
    ('careers', 'Careers'),
    ('orderEnquiry', 'Order Enquiry')
]


class ContactForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message_subject = forms.ChoiceField(required=True, widget=forms.Select,
                                        choices=SUBJECT_CHOICES)
    order_number = forms.CharField(required=False)
    message = forms.CharField(required=True, widget=forms.Textarea)
