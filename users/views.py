from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from users.forms import LoginUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm      #AuthenticationForm
    template_name = 'users/login.html'
    extra_context = { 'title': 'Авторизація'}

    def get_success_url(self):
        return reverse_lazy('main:home')


def login_user(request: HttpRequest):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('main:home'))
    else:
        form = LoginUserForm()

    context = {
        'title': 'Авторизація',
        'form': form,
    }
    return render(request, 'users/login.html', context=context)


def logout_user(request: HttpRequest):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))