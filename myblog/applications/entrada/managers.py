from django.db import models

class EntryManager(models.Manager):
    """Procedimiento para entrada"""
    
    def entrada_en_portada(self):
        
        return self.filter(
            public = True,
            portada = True,
        ).order_by('-created').first()
        
    
    def entrada_en_home(self):
        # devuelve ultimas 4 entradas
        return self.filter(
            public = True,
            in_home = True,
        ).order_by('-created')[:4]
        
    def entrada_recientes(self):
        # devuelve ultimas 6 entradas recientes
        return self.filter(
            public = True,
        ).order_by('-created')[:3]