from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import Contact


class RegisterForm(UserCreationForm):
    """Form to registrate user."""

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        """Added class 'form-control' for all form fields."""
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['required'] = 'required'

    def clean_email(self):
        """Check if email already exists."""
        email = self.cleaned_data.get('email')
        user = User.objects.filter(email=email).exists()
        if user:
            raise forms.ValidationError('E-mail is already registered!')
        return email


class ContactForm(forms.ModelForm):
    """Form for sending inquiry."""

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message', 'listing']
        labels = {
            'listing': 'Property',
        }
        widgets = {
            'listing': forms.TextInput(attrs={'disabled': 'disabled'}),
        }

    def __init__(self, *args, **kwargs):
        """Added class 'form-control' for all form fields."""
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
