from django.db import models

# Create your models here.
class Event(models.Model):
	title = models.CharField(max_length=100, verbose_name='Titre de l\'evenement')
	description = models.TextField()
	date = models.DateTimeField()
	photo = models.ImageField(upload_to='media_root')

	class Meta:
		verbose_name = 'Evenement'
		verbose_name_plural = 'Evenements'



	def __str__(self):
		return self.title 
