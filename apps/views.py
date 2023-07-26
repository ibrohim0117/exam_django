from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, FormView, DeleteView, TemplateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from apps.forms import RegisterForm, CustomLoginForm
from apps.models import User


# def users_list(request):
#     users = User.objects.all()
#     return render(request, 'users.html', {'users': users})


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'phone', 'email', 'url', 'street', 'state', 'city', 'image', 'about_me']
    template_name = 'update.html'
    success_url = reverse_lazy('users_list')

    def get_object(self, queryset=None):
        return self.request.user


class UserDeleteView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        request.user.delete()
        return redirect(reverse('users_list'))


class RegisterView(CreateView):
    template_name = 'register.html'
    queryset = User.objects.all()
    form_class = RegisterForm
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'login.html'
    next_page = reverse_lazy('users_list')


def users_list(request):
    if request.GET:
        key = request.GET.get('q')
        users = User.objects.filter(Q(first_name__contains=key)| Q(last_name__contains=key))
    else:
        users = User.objects.all()
    return render(request, 'users.html', {'users': users})