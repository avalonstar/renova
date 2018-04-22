from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import viewsets

from .models import Player
from .serializers import PlayerSerializer


class DashboardView(LoginRequiredMixin, DetailView):
    model = Player
    template_name = 'players/dashboard.html'

    def get_object(self):
        return self.request.user


class PlayerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
