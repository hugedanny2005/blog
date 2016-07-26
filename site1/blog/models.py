from django.db import models

# Create your models here.


class Account(models.Model):
    name = models.CharField(max_length=100)
    pwd = models.CharField(max_length=12)
    date = models.DateField()

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=300)
    post = models.CharField(max_length=1200)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    publish = models.DateTimeField('date_published')

    def __str__(self):
        return self.title
