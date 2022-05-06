from django.db import models

class product(models.Model):

    title = models.CharField(max_length = 255)
    description = models.TextField()
    price = models.PositiveIntegerField(default = 0 )

    def __str__(self):
        return self.title
    