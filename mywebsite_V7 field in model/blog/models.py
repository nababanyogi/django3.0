from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    email = models.EmailField(default='yogi@admin.com')
    alamat = models.CharField(max_length=200,blank=True)
    waktu_posting = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.title)