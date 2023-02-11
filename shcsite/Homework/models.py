from django.db import models
from django.contrib.auth.models import User

from Discipline.models import Discipline
from Teachers.models import Teachers
from Lessons.models import Lessons


class HomeWork(models.Model):
    title = models.CharField(blank=True, max_length=60, verbose_name='Group number')
    hm_discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE,
                                      null=True, blank=True, verbose_name='Discipline')
    hm_lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE,
                                  null=True, blank=True, verbose_name='Lesson')
    hm_teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE,
                                   null=True, blank=True, verbose_name='Teacher')
    file = models.FileField(verbose_name='file', upload_to='HomeWork/',
                            blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE,
                             blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'HomeWork'
        verbose_name_plural = 'HomeWorks'
        ordering = ['-id']
