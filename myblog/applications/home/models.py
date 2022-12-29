from django.db import models
#apps terceros
from model_utils.models import TimeStampedModel

class Home(TimeStampedModel):
    """Modelo de la pagina principal"""
    tittle = models.CharField('Nombres', max_length=30)
    description = models.TextField()
    about_title = models.CharField('Titulo Nosotros', max_length=50)
    about_text =  models.TextField()
    contact_email = models.EmailField('email de contacto', max_length=254, blank=True,null=True)
    phone = models.CharField('Telefono contacto', max_length=20)
    
    class Meta:
        verbose_name = 'Pagina principal'
        verbose_name_plural = 'Pagina principal'
        
    def __str__(self):
        return self.tittle


class Suscribers(TimeStampedModel):
    """Suscriptores"""
    email = models.EmailField()
    
    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'
        
    def __str__(self):
        return self.email
    
class Contact(TimeStampedModel):
    """Contacto"""
    full_name = models.CharField('Nombres', max_length=80)
    email = models.EmailField()
    message = models.TextField()
    
    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Mensajes'
        
    def __str__(self):
        return self.full_name
    
    