from django.db import models
from django.db.models.expressions import OrderBy

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    #me contengo de usar mi poder de urls automaticas
    slug = models.SlugField(max_length=255) 

    #orde de las etiquetas

    ordering = models.IntegerField(default=0)
    class Meta:
        ordering = ('ordering',) #la variable es el parametro del admin, y el string es nuestro campo, se usa la coma para que detecte una tupla


    #IS FEATURED


    def __str__(self):
        return self.title

#

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255) 
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    
    #Ordenar por fecha
    date_add = models.DateTimeField(auto_now_add=True)

    caracteristica = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date_add',)

    def __str__(self):
        return self.title

