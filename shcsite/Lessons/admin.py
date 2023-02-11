from django.contrib import admin
from .models import Lessons


class LessonsAdm(admin.ModelAdmin):
    list_display = ('id', 'title', 'discipline', 'content', 'file', 'is_published', 'Lesson_Teacher', 'user')
    list_display_links = ('id', 'title', 'discipline',)
    search_fields = ('id', 'discipline', 'content', 'Lesson_Teacher')
    list_filter = ('Lesson_Teacher', 'discipline',)
    list_editable = ('Lesson_Teacher', 'user',)
    list_per_page = 10
    list_per_show_all = 100
    fields = ('title', 'discipline', 'content', 'Lesson_Teacher')


admin.site.register(Lessons,
                    LessonsAdm
                    )
