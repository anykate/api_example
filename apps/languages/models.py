from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=50)
    pattern = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('language-detail', args=[str(self.id)])


class State(models.Model):
    name = models.CharField(max_length=50)
    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name='states'
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('state-detail', args=[str(self.id)])
