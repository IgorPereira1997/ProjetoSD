"""
Django settings for ProjetoSD_2 project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Faz com que possa ser possível salvar dados essenciais em um arquivo .env, que pode ser configurado no ambiente que o site é disponibilizado
# para proteção de dados sensíveis. Para saber mais sobre, acesse o site:
# https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get("DEBUG", default=0))

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")

# Application definition

INSTALLED_APPS = [
    # 'whitenoise.runserver_nostatic',
    'storages',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'contato',
    'errors',
    'listar_produtos',
    'listar_transportadoras',
    'login',
    'gerenciar_pedidos',
    'inicial',
    'django_cleanup',
]
# django cleanup faz a limpeza de qualquer resquício de dados estáticos inválidos ou não mais utilizados para otimização do código,
# principalmente por limpar imagens que também não tenham mais referências válidas.

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ProjetoSD_2.urls'

SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    os.path.join(SETTINGS_PATH, 'templates'),
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]
        },
    },
]

WSGI_APPLICATION = 'ProjetoSD_2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        "ENGINE": os.environ.get("DATABASE_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("DATABASE_NAME", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("DATABASE_USER", "user"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD", "password"),
        "HOST": os.environ.get("DATABASE_HOST", "localhost"),
        "PORT": os.environ.get("DATABASE_PORT", "5432"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'Brazil/East'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# Configuração do S3 para guardar e servir os arquivos estáticos do projeto, utilizando para isso a biblioteca S3Boto3
# para fazer a conexão da aplicação com o servidor AWS S3 que fora configurado para tal fim.

# caminho padrão dos arquivos estáticos, modificado para ser resolvido pelo Amazon Web Services S3


if os.environ.get("SECRET_KEY") == 1:
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = os.environ.get('AWS_S3_CUSTOM_DOMAIN')
    AWS_LOCATION = 'static'

    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    DEFAULT_FILE_STORAGE = 'ProjetoSD_2.storage_backends.MediaStorage'
    STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    MEDIA_LINK = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, 'media')
else:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    MEDIA_URL = "/media/"
    MEDIA_ROOT = BASE_DIR / "mediafiles"
    MEDIA_LINK = '/media/'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# dados da sandbox do paypal para permitir o teste de transações e pagamentos
# configure do paypal, configure-a seguindo https://encurtador.com.br/ltvAS

PAYPAL_CLIENT_ID = "sb-d2uth6329914@business.example.com"
PAYPAL_SECRET_ID = "access_token$sandbox$cr2shk6sw2vz3yh4$73cb41d4747ebcee972351629b1e9883"
# PAYPAL_CLIENT_ID = os.environ.get("PAYPAL_CLIENT_ID")
# PAYPAL_SECRET_ID = os.environ.get("PAYPAL_CLIENT_ID")

# Configura a aplicação django para o Heroku, no deploy inicial e/ou utilizando whitenoise para
# servir os arquivos estáticos. Neste código, foi modificado para ser utilizado AWS S3 para este fim.

# import django_heroku
# django_heroku.settings(locals(), AWS_S3_CUSTOM_DOMAIN)

# Email Configs para o fale conosco e para a recuperação de senha, Configure o arquivo .env com tais dados
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_USE_TLS = bool(os.environ.get('EMAIL_USE_TLS'))

# session timeout é utilizada para colocar um timestamp nas sessões, garatindo que, sem qualquer operação em um determinado tempo, a sessão
# seja finalizada e o usuário redirecionado para a página que o mesmo especificar

SESSION_EXPIRE_SECONDS = 600  # 10 minutes

SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True

SESSION_TIMEOUT_REDIRECT = '/'

LOGOUT_REDIRECT_URL = '/'