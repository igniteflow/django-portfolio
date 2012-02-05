from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, error_messages={'required': 'Please enter a subject'})
    message = forms.CharField(widget=forms.Textarea, error_messages={'required': 'Please enter a message'})
    your_email = forms.EmailField(
        error_messages={'required': 'Please enter your email address', 'invalid': 'Please enter a valid email address'})
    cc_myself = forms.BooleanField(required=False)