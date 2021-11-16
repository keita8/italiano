from django.db import models

# Create your models here.

class Plat(models.Model):
	title = models.CharField(max_length=200, verbose_name='Nom du plat')
	description = models.TextField()
	image = models.ImageField(upload_to='media_root', verbose_name='Photo')
	price = models.IntegerField(default=0, verbose_name='Prix')


	class Meta:
		verbose_name = 'Plat'
		verbose_name_plural = 'Plats'


	def __str__(self):
		return f" {self.title} " + ' -  ' + str({self.price}) + 'gnf'