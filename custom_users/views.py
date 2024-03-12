from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from . import models, forms


class RegisterView(CreateView):
    form_class = forms.CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = '/login/'


class InLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse('persons:user_list')


class OutLogoutView(LogoutView):
    next_page = reverse_lazy('tv_shows_list')


class UserListView(ListView):
    template_name = 'registration/user_list.html'
    model = models.CustomUser
    context_object_name = 'user'

    def get_queryset(self):
        return self.model.objects.all()