from django.db import models

# Create your models here.

class Contact (models.Model):
    avatar=models.ImageField(upload_to='contact',blank=True,null=True)
    name=models.CharField(max_length=100,verbose_name='Nombre')
    email=models.EmailField(max_length=50, verbose_name='Correo electrónico')
    birth=models.DateField(null=True,blank=True, verbose_name='Fecha de nacimiento')
    phone=models.CharField(max_length=15,null=True,blank=True, verbose_name='Teléfono')
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name