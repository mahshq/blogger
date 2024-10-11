from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "user_author"
        verbose_name = "author"
        verbose_name_plural = "authors"
        ordering = ["-id"]


    def __str__(self):
        return self.user.username

