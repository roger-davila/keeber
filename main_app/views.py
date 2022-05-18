from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Count
from .models import Keyboard
from .forms import UserRegistrationForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def keyboards_index(request):
    keyboards = Keyboard.objects.all().annotate(total_likes=Count('likes'))
    return render(request, 'keyboards/index.html', {'keyboards': keyboards})


def keyboard_detail(request, keyboard_id):
    keyboards = Keyboard.objects.annotate(total_likes=Count('likes'))
    keyboard = keyboards.get(id=keyboard_id)
    return render(request, 'keyboards/detail.html', {'keyboard': keyboard})


class KeyboardCreate(LoginRequiredMixin, CreateView):
    model = Keyboard
    fields = ['case', 'keycaps', 'switches', 'size', 'plate', 'stabilizers', 'split']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super(KeyboardCreate, self).get_form(form_class)
        for visible in form.visible_fields():
            if visible.field.label == 'Size':
                visible.field.widget.attrs.update({'id': 'size-select'})
            else:
                visible.field.widget.attrs.update({'class': 'input'})
        return form


class KeyboardDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Keyboard
    permission_required = ('keyboards.can_edit')

    def get_success_url(self):
        return reverse('keyboards', kwargs={'user_id': self.request.user.pk})


class KeyboardUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Keyboard
    permission_required = ('keyboards.can_edit')
    fields = ['case', 'keycaps', 'switches', 'size', 'plate', 'stabilizers', 'split']

    def get_form(self, form_class=None):
        form = super(KeyboardUpdate, self).get_form(form_class)
        for visible in form.visible_fields():
            if visible.field.label == 'Size':
                visible.field.widget.attrs.update({'id': 'size-select'})
            else:
                visible.field.widget.attrs.update({'class': 'input'})
        return form

def like_view(request, keyboard_id):
    keyboard = Keyboard.objects.get(id=keyboard_id)
    keyboard.likes.add(request.user)
    return redirect('detail', keyboard_id=keyboard_id)


def signup(request):
    error_message = ''
    # Code block below only executes if the from is submitted
    if request.method == 'POST':
        print(request.POST)
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Logs user in after saving to user table
            return redirect('keyboards')
        else:
            error_message = 'Invalid sign up - try again'
    # This is the GET method of the form. Just renders a blank form
    form = UserRegistrationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'user/index.html', {'user': user})


def user_keyboards(request, user_id):
    user = User.objects.get(id=user_id)
    keyboards = Keyboard.objects.filter(
        owner=user_id).annotate(total_likes=Count('likes'))
    return render(request, 'user/keyboards.html', {'user': user, 'keyboards': keyboards})
