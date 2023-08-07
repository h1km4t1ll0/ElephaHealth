import os
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y&4+r^a9^g!175fgk^bm9a1u9q+5lszj11i6g-_rkdn0_67*27'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if os.environ.get("DEBUG", '') in ["False", False] else True

ALLOWED_HOSTS = ["elepha.hikmatillo.ru", '0.0.0.0', '192.168.0.28', '127.0.0.1', '31.173.240.248', 'localhost']
if not DEBUG:
    CSRF_TRUSTED_ORIGINS = ['https://elepha.hikmatillo.ru', 'https://elepha.di.media']

if os.environ.get("SERVER", '') in ["True", True]:
    CSRF_TRUSTED_ORIGINS = ['https://elepha.hikmatillo.ru', 'https://elepha.di.media']

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'phonenumbers',
    'ElephaHealth.chill_app',
    'djoser',
    'rest_framework',
    'rest_framework_simplejwt',
]

# User
AUTH_USER_MODEL = 'chill_app.User'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=120),
    'REFRESH_TOKEN_LIFETIME': timedelta(minutes=360),
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ElephaHealth.chill_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'ElephaHealth.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
if os.environ.get("SERVER", '') in ["True", True]:
    DATABASES = {
        'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': os.environ.get("TABLE_NAME", ''),
             'USER': os.environ.get('DATABASE_USER', ''),
             'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
             'HOST':  os.environ.get('DATABASE_URL', ''),
             'PORT': os.environ.get("DATABASE_PORT", ''),
         }
    }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Etc/GMT-5'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = '/srv/telegram_admin/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
