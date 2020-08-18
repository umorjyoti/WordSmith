from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    votes_total=models.ManyToManyField(User,default=None,blank=True,related_name="vote")
    smith=models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date=models.DateTimeField()

    def summary(self):
        return self.body[:100]

    def votesTotal(self):
        return self.votes_total.all().count()

    def __str__(self):
        return self.title

    def pubdate(self):
        return self.pub_date.strftime('%b %e %Y')
