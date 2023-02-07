from django.db import models
from django.contrib.auth.models import User
from Teachers.models import Teachers
from Discipline.models import Discipline


class Lessons(models.Model):
    title = models.TextField(blank=True, verbose_name='Lecture topic')
    content = models.TextField(blank=True, verbose_name='Lecture')
    Lesson_Teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE,
                                       null=True, blank=True, verbose_name='Teacher')
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE,
                                   null=True, blank=True,)
    file = models.FileField(verbose_name='file', upload_to='Lessons/',
                            blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        # verbose_name = 'Lessons'
        # verbose_name_plural = 'Lessons'
        ordering = ['-id']

    # @property
    # def title_name(self):
    #     return self.title.name
    #
    # @title_name.setter
    # def title_name(self, value):
    #     self.title, _ = Discipline.objects.get_or_create(name=value)
