from django.db import models
from django.contrib.auth.models import User
from Discipline.models import Discipline


class Teachers(models.Model):
    title = models.CharField(max_length=200, verbose_name='Name of Teacher')
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE,
                                   null=True, blank=True, verbose_name='Discipline')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
        ordering = ['-id']
