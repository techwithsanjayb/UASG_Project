"""
Django settings for UASG_Project project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*b6xsm$(sbkkjnfkd7^fg_f=qs$p@b^^@ha!&j%@d1s0jc3ck#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

ENCRYPT_KEY = b'tmzHcYuvLUhxjcxZ4k_iqfCx-HUq6PCvdbXr4vOC5B4='
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Application_Showcase',
    'Discussion_Forum',
    'Helpdesk',
    'User',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.linkedin_oauth2',
    'allauth.socialaccount.providers.github',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'UASG_Project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,'templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
print("settingsbase",BASE_DIR)
WSGI_APPLICATION = 'UASG_Project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'uasg_db',
        'USER': 'root',
        'PASSWORD': 'tanvi',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PASSWORD': 'manager',
        'HOST': '10.208.10.193',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"',
            'charset': 'utf8mb4'
        }
    },

}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

SITE_ID = 2
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "none"
SOCIALACCOUNT_QUERY_EMAIL = True
# ACCOUNT_EMAIL_REQUIRED = True
LOGIN_REDIRECT_URL = "/"

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '910561070965-aok45rslnkaverhie0gsshevnnrt75p0.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        }
    },
    # 'facebook':
    #     {
    #      'METHOD': 'oauth2',
    #      'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
    #      'SCOPE': ['email', 'public_profile'],
    #      'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
    #      'INIT_PARAMS': {'cookie': True},
    #      'FIELDS': [
    #          'id',
    #          'first_name',
    #          'last_name',
    #          'name',
    #          'name_format',
    #          'picture',
    #          'short_name'
    #      ],
    #      'EXCHANGE_TOKEN': True,
    #      'LOCALE_FUNC': lambda request: 'ru_RU',
    #      'VERIFIED_EMAIL': False,
    #      'VERSION': 'v7.0',
    #      # you should fill in 'APP' only if you don't create a Facebook instance at /admin/socialaccount/socialapp/
    #      'APP': {
    #          'client_id': '483350450324711',  # !!! THIS App ID
    #          'secret': 'fc52797b85a770bd32b4c3cba77b3de2',  # !!! THIS App Secret
    #          'key': ''
    #             }
    #      }
     'linkedin': {
        'SCOPE': [
            'r_basicprofile',
            'r_emailaddress'
        ],
        'PROFILE_FIELDS': [
            'id',
            'first-name',
            'last-name',
            'email-address',
            'picture-url',
            'public-profile-url',
        ]
    },
    'github': {
        'SCOPE': [
            'user',
            'repo',
            'read:org',
        ],
        'PROFILE_FIELDS': [
            'id',
            'first-name',
            'last-name',
            'email-address',
            'picture-url',
            'public-profile-url',
        ]
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

if DEBUG:

  STATICFILES_DIRS = [BASE_DIR, 'static']

else:

  STATIC_ROOT = [BASE_DIR, 'static']

# MEDIA_ROOT1 = [BASE_DIR, 'media']
MEDIA_ROOT = BASE_DIR / 'media'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# print(BASE_DIR)

# print("media1",MEDIA_ROOT1)

# print("media",MEDIA_ROOT)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
