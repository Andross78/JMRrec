from django.db import models

from random import choice
import string


def generate_key():
    chars = string.digits + string.ascii_letters
    return ''.join(choice(chars) for _ in range(3))


class ShortUrl(models.Model):
    key = models.CharField(max_length=3, primary_key=True, default=generate_key)
    target = models.URLField(unique=True)


    def __str__(self):
        return f'{self.target}, {self.key}'


