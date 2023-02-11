from django.contrib import admin
from .models import HomeWork


class HomeWorkAdm(admin.ModelAdmin):
    list_display = ('id', 'title', 'hm_discipline', 'hm_lesson', 'hm_teacher',
                    'file', 'user', 'time_create', 'time_update')
    list_display_links = ('id', 'title',)
    search_fields = ('hm_discipline', 'hm_lesson', 'hm_teacher')
    list_filter = ('hm_discipline', 'hm_lesson', 'hm_teacher', 'user')
    list_editable = ('hm_discipline', 'hm_lesson', 'hm_teacher', 'user')
    list_per_page = 10
    list_per_show_all = 100
    fields = ('title',)


admin.site.register(HomeWork,
                    HomeWorkAdm
                    )
