from django.db import models

# Create your models here.
class Gallery(models.Model):
	photo = models.ImageField(upload_to='media_root/gallery/%Y/%m/%d')
	photo_small = models.ImageField(upload_to='media_root/gallery/%Y/%m/%d')

	class Meta:
		verbose_name = 'Galerie'
		verbose_name_plural = 'Galeries'
