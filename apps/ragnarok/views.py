from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from rest_framework import filters, viewsets
from rest_framework.response import Response

from .forms import AccountCreationForm
from .models import Item, Monster
from .serializers import ItemSerializer, MonsterSerializer


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


class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('pk', 'name')
    ordering = ('pk',)

    def list(self, request):
        queryset = Item.objects.order_by('?')[:10]
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)


class MonsterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Monster.objects.all()
    serializer_class = MonsterSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('pk', 'iname')
    ordering = ('pk',)
