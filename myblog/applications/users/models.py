from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )
    
    email = models.EmailField('Email', max_length=254, unique=True)
    full_name = models.CharField('Nombre Completo', max_length=100)
    ocupacion = models.CharField('Ocupacion', max_length=30, blank=True)
    genero = models.CharField('Genero', max_length=1, choices=GENDER_CHOICES, blank=True)
    date_birth = models.DateField('Fecha de Nacimiento', blank=True,null=True)
    codregistro = models.CharField(max_length=6, blank=True)
    #
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    
    
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['full_name']
    
    objects = UserManager()
    
    def get_short_name(self):
        return self.email
    
    def get_full_name(self):
        return self.full_name
    
    
    
