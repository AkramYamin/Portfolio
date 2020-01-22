from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/bolg-images/')

    def __str__(self):
        return self.title
