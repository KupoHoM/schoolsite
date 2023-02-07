
from django.contrib import admin
from .models import Lessons


# class LessonsAdm(admin.ModelAdmin):
#     list_display = ('id', 'title', 'number_lect', 'content', 'is_published', 'Lesson_Teacher', 'user')
#     list_display_links = ('id', 'title')
#     search_fields = ('id', 'number_lect', 'content', 'Lesson_Teacher')
#     list_filter = ('Lesson_Teacher',)
#     list_editable = ('Lesson_Teacher', 'user',)
#     list_per_page = 10
#     list_per_show_all = 100
#     fields = ('title', 'number_lect', 'content', 'Lesson_Teacher')


admin.site.register(Lessons,
                    # LessonsAdm
                    )

