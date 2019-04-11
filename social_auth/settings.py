"""
Django settings for social_auth project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import pymongo 

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!$1n6655jku#&@5hu=p@2jj$r(98ddnsdb_svept*qapc2)l6)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TIME_ZONE = 'Europe/Moscow'
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'rest_framework',
    'corsheaders',
    # 'social_django',
    'api',
]

# LOGIN_URL = 'login'
# LOGIN_REDIRECT_URL = 'home'
# LOGOUT_URL = 'logout'
# LOGOUT_REDIRECT_URL = 'login'

# SOCIAL_AUTH_FACEBOOK_KEY = '276416999911030'
# SOCIAL_AUTH_FACEBOOK_SECRET = 'd159180eecf26c2f7d561e46629a2f13'
# SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_link']

# SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
#       'fields': 'id, name, email, picture.type(large), link'
# }

# SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [                 
#         ('name', 'name'),
#         ('email', 'email'),
#         ('picture', 'picture'),
#         ('link', 'profile_url'),
# ]    

# SOCIAL_AUTH_INSTAGRAM_KEY = '8c6e3ee93d6b4094b805540616b3a729'
# SOCIAL_AUTH_INSTAGRAM_SECRET = 'dbab5680a98146a98a508030e1950f8f'

# SOCIAL_AUTH_INSTAGRAM_EXTRA_DATA = [
#     ('user', 'user'),
# ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware'
]

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    #'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.common.CommonMiddleware',
)

# CORS_ORIGIN_WHITELIST = (
#     'http://localhost:8080',
# )

CORS_ORIGIN_ALLOW_ALL = True 

# AUTHENTICATION_BACKENDS = [
#     'social_core.backends.linkedin.LinkedinOAuth2',
#     'social_core.backends.instagram.InstagramOAuth2',
#     'social_core.backends.facebook.FacebookOAuth2',
#     'django.contrib.auth.backends.ModelBackend',
# ]

# REST_FRAMEWORK = {
    
#     'PAGE_SIZE': 10,
    
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.BasicAuthentication',
#         # 'api.authentication.ClientAuthentication',
#         # 'rest_framework.authentication.SessionAuthentication',
#         # 'rest_framework.authentication.TokenAuthentication',
#     ),

#     'DEFAULT_PERMISSION_CLASSES':(
#         # 'rest_framework.permissions.IsAdminUser',
#         'rest_framework.permissions.AllowAny',
#         # 'rest_framework.permissions.IsAuthenticated',
#     ),

#     'EXEPTION_HANDLER': 'rest_framework_json_api.exception_handler',
#     'DEFAULT_PAGINATION_CLASS':
#         'rest_framework_json_api.pagination.PageNumberPagination',

#     'DEFAULT_PARSER_CLASSES':(
#         'rest_framework_json_api.parsers.JSONParser',
#         'rest_framework.parsers.FormParser',
#         'rest_framework.parsers.MultiPartParser'
#     ),

#     'DEFAULT_RENDERER_CLASSES':(
#         'rest_framework_json_api.renderers.JSONRenderer',
#         'rest_framework.renderers.BrowsableAPIRenderer',
#     ),
    
#     'DEFAULT_METADATA_CLASS': 'rest_framework_json_api.metadata.JSONAPIMetadata',
# }

ROOT_URLCONF = 'social_auth.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'api.settings_context.settings',
                # 'social_django.context_processors.backends',
                # 'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'social_auth.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': '',
#         'HOST': '',
#         'USER': '',
#         'PASSWORD': '',
#     }
# }


DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'user_db',
         'USER': 'user',
         'PASSWORD': '123qwe123qwe',
         'HOST': 'localhost',
         'PORT': '5432',
     }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_in_dev/'),
]