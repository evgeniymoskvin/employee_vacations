from django.contrib import admin
from .models import EmployeeModel, VacationsModel, VacationTypeModel, DepartmentModel, CommandNumberModel, \
    AccessLevelModel, WritePermissionModel, JobTitleModel, EmployeeAccessWriteModel

# Register your models here.

class CommandNumberAdmin(admin.ModelAdmin):
    ordering = ["command_number"]

class AccessLevelAdmin(admin.ModelAdmin):
    ordering = ["id"]

class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ["last_name", 'first_name', 'middle_name']
    list_filter = ['command_number_user', 'department_user', 'show_employee']

class WritePermissionAdmin(admin.ModelAdmin):
    ordering = ["id"]


class EmployeeAccessWriteAdmin(admin.ModelAdmin):
    ordering = ["employee"]


admin.site.register(EmployeeModel, EmployeeAdmin)
admin.site.register(VacationsModel)
admin.site.register(VacationTypeModel)
admin.site.register(DepartmentModel)
admin.site.register(CommandNumberModel, CommandNumberAdmin)
admin.site.register(AccessLevelModel, AccessLevelAdmin)
admin.site.register(WritePermissionModel, WritePermissionAdmin)
admin.site.register(JobTitleModel)
admin.site.register(EmployeeAccessWriteModel, EmployeeAccessWriteAdmin)
