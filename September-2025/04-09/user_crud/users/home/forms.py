from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Users,Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserForm(forms.ModelForm):
  confirm_password = forms.CharField(widget=forms.PasswordInput)
  class Meta:
    model = Users
    fields = ['name', 'age','username','password']
    widgets = {
      'password': forms.PasswordInput(),  
    }

    def clean(self):
      cleaned_data = super().clean()
      password = cleaned_data.get('password')
      confirm_password = cleaned_data.get('confirm_password')

      if password and confirm_password and password != confirm_password:
        self.add_error('confirm_password', "Passwords do not match.")
      return cleaned_data
    
    def save(self, commit=True):
      user = super().save(commit=False)
      user.password = make_password(self.cleaned_data['password'])  # hash the password
      if commit:
          user.save()
      return user

  def clean_age(self):
    age=self.cleaned_data.get('age')
    if age is None:
      raise forms.ValidationError("Age is required.")
    if not isinstance(age, int):
      raise forms.ValidationError("Age must be an integer.")
    if age < 0 or age > 100:
      raise forms.ValidationError("Age must be between 0 and 100.")
    return age
  
  def clean_name(self):
    name=self.cleaned_data.get('name')
    if not name:
      raise forms.ValidationError("Name is required.")
    if len(name) < 2 or len(name) > 50:
      raise forms.ValidationError("Name must be between 2 and 50 characters.")
    return name
  
  def clean_username(self):
    username=self.cleaned_data.get('username')
    if not username:
      raise forms.ValidationError("Username is required.")
    if len(username) < 5 or len(username) > 20:
      raise forms.ValidationError("Username must be between 5 and 20 characters.")
    if Users.objects.filter(username=username).exists():
      raise forms.ValidationError("Username already exists.")
    return username
  
  def clean_password(self):
    password=self.cleaned_data.get('password')
    if not password:
      raise forms.ValidationError("Password is required.")
    if len(password) < 8:
      raise forms.ValidationError("Password must be at least 8 characters long.")
    return password
  
  # def confirm_password(self):
  #   password=self.cleaned_data.get('password')
  #   confirm_password=self.cleaned_data.get('confirm_password')
  #   if password != confirm_password:
  #     raise forms.ValidationError("Passwords do not match.")
  #   return confirm_password


class RegisterForm(UserCreationForm):
    name = forms.CharField(max_length=100, required=True)
    age = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            useruser.save()
            Profile.objects.create(
                user=user,
                name=self.cleaned_data['name'],
                age=self.cleaned_data['age']
            )
        return user
