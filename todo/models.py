from django.db import models

# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length=200)
    is_end = models.BooleanField(default=False)
    deleted_at = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.content

# class Choice(models.Model):
