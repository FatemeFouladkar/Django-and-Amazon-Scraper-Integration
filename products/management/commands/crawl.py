import os
from pathlib import Path
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Scrape Input Links"
    
    def handle(self, *args, **kwargs):
        django_path = Path(__file__).resolve().parent.parent.parent.parent

        os.chdir(str(django_path)+"/scraper")
        os.system("scrapy crawl phone")