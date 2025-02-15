from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'age', 'weight', 'height', 'goal']
        widgets = {
            'password': forms.PasswordInput(),
        }
