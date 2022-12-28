from django.db import models
from django.conf import settings
#apps terceros
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

from .managers import EntryManager


class Category(TimeStampedModel):
    """Categorias"""
    short_name = models.CharField('Nombre corto', max_length=15)
    name = models.CharField('Nombre', max_length=30)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categoria'
        
    def __str__(self):
        return self.name
    

class Tag(TimeStampedModel):
    """Etiquetas de articulo"""
    name = models.CharField('Nombre', max_length=30)
    
    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Tags'
        
    def __str__(self):
        return self.name    


class Entry(TimeStampedModel):
    """Modelos para entradas o articulos"""
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuario', on_delete=models.CASCADE)
    categoty = models.ForeignKey(Category, verbose_name='Categoria', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name='Tag')
    title = models.CharField('Titulo', max_length=200)
    resume = models.TextField('Resumen')
    content = RichTextUploadingField('Contenido',)
    public = models.BooleanField('Publico', default=False)
    image = models.ImageField('Imagen', upload_to='media',)
    portada = models.BooleanField('Portada',default=False)
    in_home = models.BooleanField(default=False)
    slug = models.SlugField('Slug',editable=False,max_length=300)
    
    objects = EntryManager()
    
    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        
    def __str__(self):
        return self.title
    
    
    
    