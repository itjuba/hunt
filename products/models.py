from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):

    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    body = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images')
    votes_total_like = models.IntegerField(default=0)
    votes_total_dislike = models.IntegerField(default=0)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    stringlike = models.CharField(default='like',max_length=20)
    stringdislike = models.CharField(default='dislike', max_length=20)
    vote = models.CharField(default='False',max_length=20)



    def __str__(self):
        return self.title

    def pub_date_fix(self):
       return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]