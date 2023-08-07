from django.db import models


class Review_Review(models.Model):
    content = models.CharField(max_length=140)
    is_block = models.BooleanField(default=False)

    def __str__(self):
        return self.content
