from django.db import models

# Create your models here.
from .validators import validate_author

class Post(models.Model):
	judul		= models.CharField(max_length = 100)
	pengarang	= models.CharField(max_length = 100)
	body		= models.TextField()
	author 		= models.CharField(
		max_length = 100, 
		validators = [validate_author]
		)
		
	birth_date = models.DateField(blank=True, null=True)
	LIST_CATEGORY = (
		('Jurnal', 'jurnal'),
		('Blog', 'blog'),
		('Berita', 'berita'),
		)

	LIST_GENDER = (
		('L', 'Laki-laki'),
		('P', 'Perempuan'),
		)

	category	= models.CharField(
		max_length=100,
		choices = LIST_CATEGORY,
		default = 'Blog',
		)

	jenis_kelamin	= models.CharField(
		max_length=100,
		choices = LIST_GENDER,
		default = 'L',
		)

	def __str__(self):
		return "{}.{}".format(self.id,self.judul)