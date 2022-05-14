from django.shortcuts import render
from .models import Keyboard

# Create your views here.
def home(request):
    return render(request, 'home.html')  

def keyboards_index(request):
    keyboards = Keyboard.objects.all()
    return render(request, 'keyboards/index.html', {'keyboards': keyboards})
