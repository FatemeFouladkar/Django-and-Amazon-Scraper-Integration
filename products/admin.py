import os
from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from django.contrib import messages

from .models import AmazonPhoneProducts, InputLinks


@admin.register(AmazonPhoneProducts)
class AmazonPhoneProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'ASIN', 'title', 'price', 'rating', 'brand', 'model_name',
                    'operating_system', 'cellular_technology', 'wireless_network_technology')

    search_fields = ('ASIN',)

@admin.register(InputLinks)
class InputLinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'scrape',)
    
    change_list_template = 'start_scraping.html'

    def get_urls(self):
        return [
            path('start_scraping/', self.start_scraping)
        ] + super().get_urls()

    def start_scraping(self, request):
        if request.method == 'GET':
            os.system("python manage.py crawl")
            self.message_user(self, request,
                             'Crawler initialized successfully',
                             level=messages.SUCCESS)
        return redirect('../')
