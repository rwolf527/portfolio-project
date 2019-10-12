from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        len_limit = 150
        suffix = ''
        if len(self.body) > len_limit:
            suffix = ' ...'
        return self.body[:len_limit] + suffix

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
