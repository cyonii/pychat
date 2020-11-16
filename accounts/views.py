from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import (FormView, PasswordContextMixin,
    SuccessURLAllowedHostsMixin, LoginView)
from .forms import SignUpForm

# Create your views here.
class SignUpView(PasswordContextMixin, SuccessURLAllowedHostsMixin, FormView):
    template_name = 'accounts/signup.html'

    def get(self, request):
        form = SignUpForm
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            messages.success(request, 'Welcome, login to start chatting')
            return redirect('accounts:login')
        messages.error(request, 'Invalid data')
        return self.get(request)


class SignInView(LoginView):
    template_name = 'accounts/login.html'
