from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50, null=True)
    slug =models.SlugField(max_length=50 ,unique=True, null=True)

    def __str__ (self):
        return self.name

class Memory(models.Model):
    name  = models.CharField(max_length=200, unique=True, verbose_name="Hikayenin Adı")
    category = models.ForeignKey(Category,null=True, on_delete=models.DO_NOTHING)
    description = models.TextField(blank=True, null=True, verbose_name="Hikaye İçeriği")
    image = models.ImageField(upload_to="memories/%Y/%m/%d/", default="memories/default.jpg")
    date = models.DateTimeField(auto_now=False, verbose_name="Hikaye Tarihi")
    available= models.BooleanField(default=True, verbose_name="Hikaye Aktif Mi?") 

    def __str__ (self):
        return self.name