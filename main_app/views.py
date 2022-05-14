from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Keyboard

# Create your views here.
def home(request):
    return render(request, 'home.html')

def keyboards_index(request):
    keyboards = Keyboard.objects.all()
    return render(request, 'keyboards/index.html', {'keyboards': keyboards})

def keyboard_detail(request, keyboard_id):
    keyboard = Keyboard.objects.get(id=keyboard_id)
    return render('keyboards/detail.html', {'keyboard': keyboard})

def signup(request):
    error_message = ''
    # Code block below only executes if the from is submitted
    if request.method == 'POST':
        print(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) #Logs user in after saving to user table
            return redirect('keyboards')
        else:
            error_message = 'Invalid sign up - try again'
    # This is the GET method of the form. Just renders a blank form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html',context)
