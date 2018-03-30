from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Player


class DashboardView(LoginRequiredMixin, DetailView):
    model = Player
    template_name = 'players/dashboard.html'

    def get_object(self):
        return self.request.user
