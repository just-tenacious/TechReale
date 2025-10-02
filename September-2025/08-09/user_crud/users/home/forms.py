from django import forms
from .models import Users

class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(), required=True, label="Confirm Password")
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Users
        fields = ['name', 'age', 'password', 'username', 'email']

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is None:
            raise forms.ValidationError("Age is required.")
        if age < 0 or age > 100:
            raise forms.ValidationError("Age must be between 0 and 100.")
        return age

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("Name is required.")
        if len(name) < 2 or len(name) > 50:
            raise forms.ValidationError("Name must be between 2 and 50 characters.")
        return name

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError("Enter appropriate password")
        if len(password) < 8 or len(password) > 15:
            raise forms.ValidationError("Length of password should be between 8 to 15")
        return password

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError("Username is required.")
        if len(username) < 2 or len(username) > 50:
            raise forms.ValidationError("Username must be between 2 and 50 characters.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Enter valid email")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Password and Confirm Password do not match.")
