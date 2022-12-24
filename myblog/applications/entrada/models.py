from django.db import models
#apps terceros
from model_utils.models import TimeStampedModel


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

