"""renova URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from apps.views import SiteView
from apps.players.views import PlayerViewSet
from apps.ragnarok.views import AccountCreationView

router = routers.DefaultRouter()
router.register('players', PlayerViewSet)

urlpatterns = [
    path('', SiteView.as_view(), name='site_home'),
    path('', include('apps.players.urls')),
    path(
        'accounts/create/',
        AccountCreationView.as_view(),
        name='account_create',
    ),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
