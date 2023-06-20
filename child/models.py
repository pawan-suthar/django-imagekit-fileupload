from django.db import models

# Create your models here.
class filedata(models.Model):
    file = models.URLField(verbose_name="fileurl")

    def __str__(self):
        return str(self.id)
