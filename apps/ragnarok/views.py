from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .forms import AccountCreationForm


class AccountCreationView(LoginRequiredMixin, FormView):
    template_name = 'minerva/create.html'
    form_class = AccountCreationForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(AccountCreationView, self).get_form_kwargs()
        kwargs['instance'] = self.request.user
        return kwargs
