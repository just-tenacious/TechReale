from django import forms
from .models import Users

class UserForm(forms.ModelForm):
  class Meta:
    model = Users
    fields = ['name', 'age']
  
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