from django import forms

from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			'pengarang',
			'author',
			'judul',
			'body',
			'category',
			'jenis_kelamin',
			'birth_date',
		]
