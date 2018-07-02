from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['206.81.7.39']

# Database

    # https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_secrets('DB_NAME'),
        'USER': get_secrets('USER'),
        'PASSWORD': get_secrets('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR.child('static')
STATICFILES_DIRS = [BASE_DIR.child('staticfiles')]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

LOCALE_PATHS = [BASE_DIR.child('locale')]
