from django.db import models
from django.contrib.auth.models import User


class Discipline(models.Model):
    title = models.CharField(max_length=200, verbose_name='Subjects')

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE,
                             blank=True, null=True
                             )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Discipline'
        verbose_name_plural = 'Disciplines'
        ordering = ['-id']
