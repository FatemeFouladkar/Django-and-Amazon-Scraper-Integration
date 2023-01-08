from django.db import models
from django.utils.translation import gettext as _


class InputLinks(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('title'),\
                             help_text=_('Say what you searched for to get the links'))
    links = models.TextField(blank=True, null=True, verbose_name=_('links'),
                            help_text=_('Enter coma-separated links to be scraped'))
    scrape = models.BooleanField(default=True, verbose_name=_('scrape'),\
                                 help_text=_('Check if the links should be scraped'))

    class Meta:
        verbose_name = _('Input Link')
        verbose_name_plural = _('Input Links')


class AmazonPhoneProducts(models.Model):
    ASIN = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('ASIN'))
    link = models.URLField(null=True, blank=True, verbose_name=_('link'))
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('title'))
    price = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('price'))
    rating = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('rating'))
    brand = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('brand'))
    model_name = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('model name'))
    operating_system = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('operating system'))
    cellular_technology = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('cellular technology'))
    wireless_network_technology = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('wireless network technology'))
    about = models.TextField(null=True, blank=True, verbose_name=_('about'))

    class Meta:
        verbose_name = _('Amazon Phone Product')
        verbose_name_plural = _('Amazon Phone Products')
