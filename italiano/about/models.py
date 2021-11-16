from django.db import models

# Create your models here.
class About(models.Model):
	title = models.CharField(max_length=200, verbose_name="Titre")
	subtitle = models.CharField(max_length=200, verbose_name='sous titre')
	content = models.TextField(max_length=300, verbose_name='contenu')

	class Meta:
		verbose_name = 'A propos'
		verbose_name_plural = 'A propos'


	def __str__(self):
		return self.title

		