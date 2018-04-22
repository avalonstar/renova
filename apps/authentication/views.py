from allauth.socialaccount.providers.twitch.views import TwitchOAuth2Adapter
from rest_auth.registration.views import SocialLoginView


class TwitchLogin(SocialLoginView):
    adapter_class = TwitchOAuth2Adapter
