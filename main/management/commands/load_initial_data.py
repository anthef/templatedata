from django.core.management.base import BaseCommand
from main.models import Category, Link

class Command(BaseCommand):
    help = 'Loads initial data for categories and links'

    def handle(self, *args, **kwargs):
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        Category.objects.all().delete()
        
        # Create categories
        self.stdout.write('Creating categories...')
        auto_eda = Category.objects.create(
            name='AutoEDA',
            slug='auto-eda',
            description='Tools untuk melakukan Exploratory Data Analysis secara otomatis',
            order=1
        )
        
        auto_fe = Category.objects.create(
            name='AutoFE Template',
            slug='auto-fe',
            description='Template untuk mengotomatisasi feature engineering',
            order=2
        )
        
        auto_ml = Category.objects.create(
            name='AutoML Template',
            slug='auto-ml',
            description='Template untuk otomatisasi machine learning',
            order=3
        )
        
        # Create links
        self.stdout.write('Creating links...')
        
        # AutoEDA links
        Link.objects.create(
            title='Sweetvis',
            url='https://www.kaggle.com/code/maeule/autoeda-sweetvis/',
            category=auto_eda,
            order=1
        )
        
        Link.objects.create(
            title='Pandas-profiling',
            url='https://www.kaggle.com/code/maeule/autoeda-pandas-profiling',
            category=auto_eda,
            order=2
        )
        
        # AutoFE links
        Link.objects.create(
            title='Feature Tools',
            url='https://www.kaggle.com/code/maeule/autofe-template-feature-tools/',
            category=auto_fe,
            order=1
        )
        
        Link.objects.create(
            title='Autofeat',
            url='https://www.kaggle.com/code/maeule/autofe-template-autofeat',
            category=auto_fe,
            order=2
        )
        
        Link.objects.create(
            title='T-Fresh',
            url='https://www.kaggle.com/code/maeule/autofe-template-tsfresh/',
            category=auto_fe,
            order=3
        )
        
        Link.objects.create(
            title='Kats',
            url='https://www.kaggle.com/code/maeule/autofe-template-kats/',
            status='BELUM BERHASIL',
            category=auto_fe,
            order=4
        )
        
        # AutoML links
        Link.objects.create(
            title='PyCaret',
            url='https://www.kaggle.com/code/maeule/automl-autofe-template-pycaret',
            category=auto_ml,
            order=1
        )
        
        Link.objects.create(
            title='FLAML',
            url='https://www.kaggle.com/code/maeule/automl-template-flaml/',
            category=auto_ml,
            order=2
        )
        
        Link.objects.create(
            title='AutoGluon & AutoSklearn',
            url='https://www.kaggle.com/competitions/playground-series-s4e5/discussion/499494',
            category=auto_ml,
            order=3
        )
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded initial data!'))