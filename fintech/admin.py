from django.contrib import admin
from .models import Teacher, Student, Group



# admin.site.register(Teacher)
# admin.site.register(Student)
# admin.site.register(Group)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'yosh', 'ism_group_familya', 'group', 'enrollment_date')
    search_fields = ('first_name', 'last_name',)


# @admin.register(Teacher)
# class TeacherAdmin(admin.ModelAdmin):
#     list_display = ('first_name',)



# @admin.register(Group)
# class GroupAdmin(admin.ModelAdmin):
#     list_display = ('first_name',)