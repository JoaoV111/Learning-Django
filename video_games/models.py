from django.db import models


class Console(models.Model):
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    image = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Comments(models.Model):
    console = models.ForeignKey(Console, on_delete=models.CASCADE)
    comment_txt = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.comment_txt
