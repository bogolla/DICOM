"""Django settings for configs project."""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k5w109f44-2#t0gmiynlblqtjc7&6zqfhi2zy91aleq(fg73tp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_swagger',
    'rest_framework_docs',
    'rest_hooks',

    'sil_dicom',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


ROOT_URLCONF = 'configs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': BASE_DIR + '/templates/',
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'configs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dicomweb',
        'USER': 'glar',
        'PASSWORD': 'glar',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# # Update database configuration with $DATABASE_URL.
# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)

# django-rest framework configs
REST_FRAMEWORK = {
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FileUploadParser',
        'rest_framework.parsers.FormParser',
        'rest_framework_xml.parsers.XMLParser',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.AdminRenderer',
        'rest_framework_xml.renderers.XMLRenderer',
    ),
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
    ),
    'PAGE_SIZE': 100,
    'PAGINATE_BY_PARAM': 'page_size',
    'DATETIME_FORMAT': 'iso-8601',
    'DATE_FORMAT': 'iso-8601',
    'TIME_FORMAT': 'iso-8601',
}

SWAGGER_SETTINGS = {
    'api_version': '0.1',
    'supportedSubmitMethods': [
        'get',
        'post'
    ],
    'info': {
        'contact': 'brian.ogollah@savannahinformatics.com',
        'description': 'This is a sample Dicom web implementation. '
                       'You can find out more about DICOM WEB at '
                       '<a href="http://dicomweb.hcintegrations.ca/#/home">'
                       'dicomweb.hcintegrations.ca</a> ',
        'title': 'DICOM WEB Sample',
    },
}

HOOK_EVENTS = {
    'ups.added': 'DICOM.UnifiedProcedureStep.created',
    'ups.changed': 'DICOM.UnifiedProcedureStep.updated',
    'ups.removed': 'DICOM.UnifiedProcedureStep.deleted',

    # Add the DICOM UPS Status configs here
    # This requires creation of custom hooks for each status
    'ups.created': 'DICOM.UnifiedProcedureStep.read'
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
