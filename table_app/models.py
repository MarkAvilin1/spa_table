from django.db import models


class TableData(models.Model):
    date = models.DateField(auto_now=True, name='date')
    title = models.CharField(max_length=250, name='title')
    quantity = models.IntegerField(name='quantity')
    distance = models.IntegerField(name='distance')

    def __str__(self):
        return self.title
