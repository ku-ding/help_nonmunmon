from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render,redirect
from django.views.generic import CreateView

# for signup 
signup = CreateView.as_view(
    form_class=UserCreationForm,
    template_name='form.html',
    success_url=settings.LOGIN_URL,
)

#for login
login = LoginView.as_view(
    template_name='form.html',
)

#for logout
logout = LogoutView.as_view(
    next_page='/app',
)

#access next to login
@login_required
def profile(request):
    return redirect('/app')
