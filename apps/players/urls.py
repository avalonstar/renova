from django.urls import include, path

from .views import DashboardView

urlpatterns = [path('dashboard/', DashboardView.as_view(), name='dashboard')]
