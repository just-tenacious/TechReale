from django.shortcuts import render,get_object_or_404,redirect
from .models import Users
from .forms import UserForm

def user_list(request):
    users = Users.objects.all()
    return render(request, 'user_list.html', {'users': users})

def delete_user(request, user_id):
  if request.method == 'POST':
    user = get_object_or_404(Users,id=user_id)
    user.delete()
  return redirect('user_list')

def add_user(request):
  if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid() and request.POST.get('age').isdigit() and int(request.POST.get('age')) >= 0 and int(request.POST.get('age')) <= 100:
      form.save()
      return redirect('user_list')
  else:
    form = UserForm()
  return render(request, 'add_user.html', {'form': form})

def update_user(request, user_id):
  user = get_object_or_404(Users, id=user_id)
  if request.method == 'POST':
    form = UserForm(request.POST, instance=user)
    if form.is_valid():
      form.save()
      return redirect('user_list')
  else:
    form = UserForm(instance=user)
  return render(request, 'update_user.html', {'form': form})