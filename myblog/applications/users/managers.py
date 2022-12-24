from django.db import models

from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager, models.Manager):
    
    def _create_user(self,email,password,is_staff,is_superuser,is_active, **extra_fields):
        user = self.model(
            email = email,
            is_staff = is_staff,
            is_superuser = is_superuser,
            is_active =is_active,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self,email,password=None,**extra_fields):
        return self._create_user(email,password,is_staff=False,is_superuser=False,is_active=False,**extra_fields)
    
    def create_superuser(self,email,password=None,**extra_fields):
        
        return self._create_user(email,password,is_staff=True,is_superuser=True,is_active=True,**extra_fields)
    
    def cod_validation(self,id_user,cod_registro):
        if self.filter(id=id_user,codregistro=cod_registro).exists:
            return True
        else:
            return False