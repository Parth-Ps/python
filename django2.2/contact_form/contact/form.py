from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        company_website = cleaned_data.get('company_website')
        company_challenge = cleaned_data.get('company_challenge')
        project_briefly = cleaned_data.get('project_briefly')
        budget = cleaned_data.get('budget')
