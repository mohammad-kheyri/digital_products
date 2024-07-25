
from distutils.command.upload import upload
from itertools import product
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=('parent'), blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='categories')
    is_enable = models.BooleanField(_('is_enable'), default=True)
    created_time = models.DateTimeField(_('created_time'), auto_now_add=True)
    updated_time =models.DateTimeField(_('updated_time'), auto_now=True)


class Meta:
    db_table = 'categories'
    very_name = _('Category')
    very_name_plural = _('Categories')



class Product(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='products/')
    is_enable = models.BooleanField(_('is_enable'), default=True)
    categories = models.ManyToManyField('Category', verbose_name=_('categories'), blank=True)
    created_time = models.DateTimeField(_('created_time'), auto_now_add=True)
    updated_time =models.DateTimeField(_('updated_time'), auto_now=True)


    
    

class Meta:
    db_table = 'product'
    very_name = _('product')
    very_name_plural = _('products')

    

class File(models.Model):
    product = models.ForeignKey('Product', verbose_name=_('product'), on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    file = models.FieldFile(_('file'), upload_to='files/%Y/%m/%d/')
    is_enable = models.BooleanField(_('is_enable'), default=True)
    created_time = models.DateTimeField(_('created_time'), auto_now_add=True)
    updated_time =models.DateTimeField(_('updated_time'), auto_now=True)

class Meta:
    db_table = 'file'
    very_name = _('file')
    very_name_plural = _('files')


