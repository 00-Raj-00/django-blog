
from io import BytesIO


from PIL import Image


from django.core.files.base import ContentFile

from django.db import models

from django.contrib.auth.models import User
from django.db.transaction import commit


# Create your models here.

class Article(models.Model):
    image = models.ImageField(upload_to='article/',blank=True,null=True)
    title = models.CharField(max_length=500)
    intro = models.TextField(blank=True,null=True)
    body = models.TextField(blank=True,null=True)
    conc = models.TextField(blank=True,null=True)
    author =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.author}--{self.date}--{self.title}"


    def save(self,*args,**kwargs):
       if self.image :
            img = Image.open(self.image)
            img.thumbnail((1200,1200))
            buffer = BytesIO()

            img.convert("RGB").save(
                buffer,

                format="JPEG",
                quality = 70,
                optimize=True
            )
            self.image.save(
                self.image.name,

                ContentFile( buffer.getvalue()),
                save = False

            )
       super().save(*args,**kwargs)








