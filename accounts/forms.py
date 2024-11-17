from django import forms
from.models import Account

class RegisterForm(forms.ModelForm):

    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    class Meta:

        model=Account
        fields=['first_name','last_name','email','phone_number','country']


    def clean(self):

        # cleaned_date=super(RegisterForm,self).clean()
        # password=cleaned_date.get('password')
        # confirm_password=cleaned_date.get('confirm_password')

        cleaned_date=super().clean()
        password=cleaned_date['password']
        confirm_password=cleaned_date['confirm_password']

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Your Passwords don\'t match!")
        return cleaned_date