"""
Django settings for demosite project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'q$i&rh-y8*&m6)47_$5g-f!lg3qe$c*u1e$ypa=rdb=_94bh-@'
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag')

# TODO: SET FALSE ON PRODUCTION
DEBUG = True

# TODO: UNCOMMENT ON PRODUCTION
SECURE_CONTENT_TYPE_NOSNIFF = True  # prevent the browser from guessing the content type and force it to always use the type provided in the Content-Type header
SECURE_HSTS_SECONDS = 60  # 1 year # refuse to connect to your domain name via an insecure connection (for a given period of time) by setting the „Strict-Transport-Security” header
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # add the includeSubDomains directive to the Strict-Transport-Security header.
SECURE_SSL_REDIRECT = True  # redirect from http to https
SESSION_COOKIE_SECURE = True  # This instructs the browser to only send these cookies over HTTPS connections.
CSRF_COOKIE_SECURE = True  # This instructs the browser to only send these cookies over HTTPS connections.
SECURE_HSTS_PRELOAD = True  # Preload page for google
SECURE_BROWSER_XSS_FILTER = True  # work by looking for JavaScript content in the GET or POST parameters of a page. If the JavaScript is replayed in the server’s response, the page is blocked

ALLOWED_HOSTS = [
    'relaksownia.wizytoowka.pl',
    'demosite.arturszwagrzak.atthost24.pl',
    '127.0.0.1'
]

FILE_UPLOAD_PERMISSIONS = 0o644

# Application definition

INSTALLED_APPS = [
    'phonenumber_field',
    'main.apps.MainConfig',
    'faq.apps.FaqConfig',
    'contact.apps.ContactConfig',
    'opinions.apps.OpinionsConfig',
    'info.apps.InfoConfig',
    'blog.apps.BlogConfig',
    'offer.apps.OfferConfig',
    'newsletter.apps.NewsletterConfig',
    'bootstrap_modal_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djrichtextfield',
    'django_sass',
    'cookielaw',
    'sslserver'
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

# MY CUSTOM SETTINGS

ROOT_URLCONF = 'demosite.urls'

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_CHARSET='utf-8'


DJRICHTEXTFIELD_CONFIG = {
    'js': ['//cdn.ckeditor.com/4.14.0/standard/ckeditor.js'],
    'init_template': 'djrichtextfield/init/ckeditor.js',
    'settings': {  # CKEditor
        'toolbar': [
            {'items': ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker', 'Undo', 'Redo']},
            {'items': ['Link', 'Unlink', 'Image', 'Table', 'TextColor', 'BGColor', 'Indent', 'Outdent']},
            {'items': ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', 'NumberedList', 'BulletedList']},
            {'items': ['Source']}
        ],
        'format_tags': 'p;h1;h2;h3',
        'width': 700,
        'sanitizer': 'bleach.clean'
    }
}

# END OF MY CUSTOM SETTINGS

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'demosite.context_processor.contact_phone_processor',
                'demosite.context_processor.social_media_processor'
            ],
        },
    },
]

WSGI_APPLICATION = 'demosite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'OPTIONS': {
    #         'read_default_file': os.path.join(BASE_DIR, 'mysql.cnf'),
    #     },
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'demosite',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'localhost'
        }
    # }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'pl-pl'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'demosite/static')
]

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'arturszwagrzak.atthost24.pl'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'artur@wizytoowka.pl'
EMAIL_HOST_PASSWORD = os.environment.get('EMAIL_HOST_PASSWORD')
