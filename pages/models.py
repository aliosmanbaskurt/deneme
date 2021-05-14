from django.db import models

# Create your models here.


class Future (models.Model):
    future_name  = models.CharField(max_length=200, unique=True, verbose_name="Ülkenin Adı")
    future_image = models.ImageField(upload_to="memories/%Y/%m/%d/", default="memories/default.jpg")
    future_date = models.DateField(auto_now=False, verbose_name="Planlanan Tarih")
    future_okey = models.BooleanField(default=False, verbose_name="Gidildi Mi?")

    def __str__ (self):
        return self.future_name