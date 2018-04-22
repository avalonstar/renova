import os

from django.conf import settings
from django.http import HttpResponse
from django.views.generic import View


class ReactView(View):

    def get(self, request):
        try:
            with open(
                os.path.join(settings.REACT_DIR, 'build', 'index.html')
            ) as file:
                return HttpResponse(file.read())

        except Exception:
            return HttpResponse(status=501)
