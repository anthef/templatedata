import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# Use environment variable or hardcoded value for development
SECRET_KEY = 'django-insecure-e&&!-$m(!h3naqmxb5e@h8kiv==5=$n=g9dscea6cc@pzjwc_y'

# SECURITY WARNING: don't run with debug turned on in production!
# Set to False by default and only True if explicitly set in environment
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Add your Railway app domain and localhost to allowed hosts
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.railway.app']
if os.environ.get('RAILWAY_STATIC_URL'):
    ALLOWED_HOSTS.append(os.environ.get('RAILWAY_STATIC_URL'))

# CSRF settings for Railway deployment
CSRF_TRUSTED_ORIGINS = ['https://*.railway.app']
if os.environ.get('RAILWAY_STATIC_URL'):
    CSRF_TRUSTED_ORIGINS.append(f"https://{os.environ.get('RAILWAY_STATIC_URL')}")

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add whitenoise middleware for static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Database configuration for Railway PostgreSQL
# It will use SQLite locally if DATABASE_URL is not provided
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# If DATABASE_URL is present (Railway provides this automatically)
if os.environ.get('DATABASE_URL'):
    import dj_database_url
    DATABASES['default'] = dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600
    )

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Enable whitenoise compression and caching for better performance
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'