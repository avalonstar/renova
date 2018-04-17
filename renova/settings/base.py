import os

import dj_database_url

from configurations import Configuration, values


class Base(Configuration):
    # Path Configuration.
    # --------------------------------------------------------------------------
    BASE_DIR = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )

    # Debug Settings.
    # SECURITY WARNING: Don't run with debug turned on in production!
    # --------------------------------------------------------------------------
    DEBUG = values.BooleanValue(True)
    TESTING = values.BooleanValue(False)

    # Application Definition.
    # --------------------------------------------------------------------------
    DJANGO = [
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
    ]
    COMPONENTS = ['apps.authentication', 'apps.players', 'apps.ragnarok']
    PLUGINS = [
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.twitch',
        'compressor',
    ]
    ADMINISTRATION = ['django.contrib.admin']
    INSTALLED_APPS = DJANGO + COMPONENTS + PLUGINS + ADMINISTRATION

    # Middleware Definition.
    # --------------------------------------------------------------------------
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    # Manager Definition.
    # --------------------------------------------------------------------------
    ADMINS = [('Bryan Veloso', 'bryan@avalonstar.tv')]

    # Database Definition.
    # https://docs.djangoproject.com/en/2.0/ref/settings/#databases
    # --------------------------------------------------------------------------
    DATABASES = {
        'default': dj_database_url.config(conn_max_age=None),
        'ragnarok': dj_database_url.parse(
            os.getenv('RAGNAROK_URL'), conn_max_age=None
        ),
    }
    DATABASE_ROUTERS = ['apps.ragnarok.router.RagnarokRouter']

    # Template Definition.
    # --------------------------------------------------------------------------
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR + '/templates/'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ]
            },
        }
    ]

    # URL Configuration.
    # --------------------------------------------------------------------------
    ROOT_URLCONF = 'renova.urls'
    WSGI_APPLICATION = 'renova.wsgi.application'

    # User and Authentication Definitions.
    # --------------------------------------------------------------------------
    AUTH_USER_MODEL = 'players.Player'
    AUTHENTICATION_BACKENDS = [
        'django.contrib.auth.backends.ModelBackend',
        'allauth.account.auth_backends.AuthenticationBackend',
    ]
    LOGIN_REDIRECT_URL = 'dashboard'

    # https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'
        },
    ]

    # django-allauth
    ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
    ACCOUNT_ADAPTER = 'apps.authentication.adapters.AccountAdapter'
    SOCIALACCOUNT_ADAPTER = 'apps.authentication.adapters.SocialAccountAdapter'
    SOCIALACCOUNT_EMAIL_VERIFICATION = False
    SOCIALACCOUNT_PROVIDERS = {
        'twitch': {'SCOPE': ['user_read', 'user_subscriptions']}
    }

    # Static Files. (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/
    # --------------------------------------------------------------------------
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    STATICFILES_FINDERS = [
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'compressor.finders.CompressorFinder',
    ]

    # django-compressor
    COMPRESS_OFFLINE = True
    COMPRESS_PRECOMPILERS = (('text/x-scss', 'django_libsass.SassCompiler'),)

    # Internationalization.
    # https://docs.djangoproject.com/en/2.0/topics/i18n/
    # --------------------------------------------------------------------------
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    # Secret Key Configuration.
    # SECURITY WARNING: Keep the secret key used in production secret!
    # --------------------------------------------------------------------------
    SECRET_KEY = os.getenv('SECRET_KEY')

    # Other.
    # --------------------------------------------------------------------------
    ALLOWED_HOSTS = []
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    SITE_ID = 1
