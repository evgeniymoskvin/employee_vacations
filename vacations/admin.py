from django.contrib import admin
from .models import EmployeeModel, VacationsModel, VacationTypeModel, GroupDepartmentModel, CommandNumberModel, \
    AccessLevelModel, WritePermissionModel, JobTitleModel, EmployeeAccessWriteModel, YearModel

# Register your models here.

class CommandNumberAdmin(admin.ModelAdmin):
    ordering = ["command_number"]

class VacationsAdmin(admin.ModelAdmin):
    ordering = ["employee"]
    search_fields = ["employee", "day_count"]

class AccessLevelAdmin(admin.ModelAdmin):
    ordering = ["id"]

class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ["last_name", 'first_name', 'middle_name']
    list_filter = ['department', 'department_group', 'work_status']

class WritePermissionAdmin(admin.ModelAdmin):
    ordering = ["id"]


class EmployeeAccessWriteAdmin(admin.ModelAdmin):
    ordering = ["employee"]

class YearAdmin(admin.ModelAdmin):
    ordering = ["year"]

# admin.site.register(EmployeeModel, EmployeeAdmin)
admin.site.register(VacationsModel, VacationsAdmin)
admin.site.register(VacationTypeModel)
# admin.site.register(GroupDepartmentModel)
# admin.site.register(CommandNumberModel, CommandNumberAdmin)
admin.site.register(AccessLevelModel, AccessLevelAdmin)
admin.site.register(WritePermissionModel, WritePermissionAdmin)
admin.site.register(JobTitleModel)
admin.site.register(EmployeeAccessWriteModel, EmployeeAccessWriteAdmin)
admin.site.register(YearModel, YearAdmin)