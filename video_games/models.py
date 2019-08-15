from django.db import models
import datetime

class Console(models.Model):
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Comments(models.Model):
    console = models.ForeignKey(Console, on_delete=models.CASCADE)
    comment_txt = models.TextField(max_length=200)
    score = models.IntegerField(default=0, choices=[(0, '0'), (1, '1'),
                                                    (2, '2'), (3, '3'),
                                                    (4, '4'), (5, '5')])
    pub_date = models.DateTimeField(default=datetime.date.today)
    def __str__(self):
        return self.comment_txt
