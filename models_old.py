# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TodoTasksApprovemodel(models.Model):
    approve_status = models.BooleanField()
    approve_date = models.DateTimeField(blank=True, null=True)
    approve_task = models.ForeignKey('TodoTasksTaskmodel', models.DO_NOTHING, blank=True, null=True)
    approve_user = models.ForeignKey('TodoTasksEmployee', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ToDo_tasks_approvemodel'


class TodoTasksAttachmentfilesmodel(models.Model):
    add_data = models.DateTimeField(blank=True, null=True)
    task = models.ForeignKey('TodoTasksTaskmodel', models.DO_NOTHING, blank=True, null=True)
    file = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ToDo_tasks_attachmentfilesmodel'


class TodoTasksBackcommentmodel(models.Model):
    bad_comment = models.TextField(blank=True, null=True)
    task = models.ForeignKey('TodoTasksTaskmodel', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ToDo_tasks_backcommentmodel'


class TodoTasksCanacceptmodel(models.Model):
    user_accept = models.ForeignKey('TodoTasksEmployee', models.DO_NOTHING, blank=True, null=True)
    dep_accept = models.ForeignKey('TodoTasksCommandnumbermodel', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ToDo_tasks_canacceptmodel'


class TodoTasksCanchangeworkersmodel(models.Model):
    dep_accept = models.ForeignKey('TodoTasksCommandnumbermodel', models.DO_NOTHING, blank=True, null=True)
    user_accept = models.ForeignKey('TodoTasksEmployee', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ToDo_tasks_canchangeworkersmodel'


class TodoTasksCommandnumbermodel(models.Model):
    command_number = models.CharField(max_length=15)
    command_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'ToDo_tasks_commandnumbermodel'


class TodoTasksContractmodel(models.Model):
    contract_name = models.CharField(max_length=250)
    contract_object = models.ForeignKey('TodoTasksObjectmodel', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ToDo_tasks_contractmodel'


class TodoTasksCpemodel(models.Model):
    cpe_user = models.ForeignKey('TodoTasksEmployee', models.DO_NOTHING, blank=True, null=True)
    cpe_object = models.ForeignKey('TodoTasksObjectmodel', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ToDo_tasks_cpemodel'


class TodoTasksEmployee(models.Model):
    department = models.ForeignKey(TodoTasksCommandnumbermodel, models.DO_NOTHING, blank=True, null=True)
    user_phone = models.IntegerField(blank=True, null=True)
    department_group = models.ForeignKey('TodoTasksGroupdepartmentmodel', models.DO_NOTHING, blank=True, null=True)
    user = models.OneToOneField('AuthUser', models.DO_NOTHING)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150)
    right_to_sign = models.BooleanField()
    job_title = models.ForeignKey('TodoTasksJobtitlemodel', models.DO_NOTHING, blank=True, null=True)
    can_make_task = models.BooleanField()
    cpe_flag = models.BooleanField()
    mailing_list_check = models.BooleanField()
    work_status = models.BooleanField()
    check_edit = models.BooleanField()
    personnel_number = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ToDo_tasks_employee'


class TodoTasksFavoriteslistmodel(models.Model):
    favorite_list_name = models.CharField(max_length=25)
    favorite_list_holder = models.ForeignKey(TodoTasksEmployee, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ToDo_tasks_favoriteslistmodel'


class TodoTasksFavoritessharemodel(models.Model):
    can_change_list = models.BooleanField()
    favorite_list = models.ForeignKey(TodoTasksFavoriteslistmodel, models.DO_NOTHING)
    favorite_share_user = models.ForeignKey(TodoTasksEmployee, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ToDo_tasks_favoritessharemodel'


class TodoTasksGroupdepartmentmodel(models.Model):
    group_dep_abr = models.CharField(max_length=10)
    group_dep_name = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'ToDo_tasks_groupdepartmentmodel'


class TodoTasksJobtitlemodel(models.Model):
    job_title = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'ToDo_tasks_jobtitlemodel'


class TodoTasksMarkdocmodel(models.Model):
    mark_doc = models.CharField(max_length=5)
    mark_doc_full_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'ToDo_tasks_markdocmodel'


class TodoTasksObjectmodel(models.Model):
    object_name = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'ToDo_tasks_objectmodel'


class TodoTasksOrdersmodel(models.Model):
    order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ToDo_tasks_ordersmodel'


class TodoTasksStagemodel(models.Model):
    stage_name = models.CharField(max_length=250)
    stage_contract = models.ForeignKey(TodoTasksContractmodel, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ToDo_tasks_stagemodel'


class TodoTasksTaskmodel(models.Model):
    text_task = models.TextField()
    task_number = models.CharField(max_length=15)
    department_number = models.ForeignKey(TodoTasksCommandnumbermodel, models.DO_NOTHING, blank=True, null=True)
    author = models.ForeignKey(TodoTasksEmployee, models.DO_NOTHING)
    task_type_work = models.IntegerField()
    task_order = models.ForeignKey(TodoTasksOrdersmodel, models.DO_NOTHING, blank=True, null=True)
    task_contract = models.ForeignKey(TodoTasksContractmodel, models.DO_NOTHING, blank=True, null=True)
    task_object = models.ForeignKey(TodoTasksObjectmodel, models.DO_NOTHING)
    task_change_number = models.IntegerField(blank=True, null=True)
    back_to_change = models.BooleanField()
    cpe_sign_user = models.ForeignKey(TodoTasksEmployee, models.DO_NOTHING, blank=True, null=True)
    first_sign_status = models.BooleanField()
    first_sign_user = models.ForeignKey(TodoTasksEmployee, models.DO_NOTHING, blank=True, null=True)
    second_sign_user = models.ForeignKey(TodoTasksEmployee, models.DO_NOTHING, blank=True, null=True)
    cpe_sign_status = models.BooleanField()
    second_sign_status = models.BooleanField()
    cpe_sign_date = models.DateTimeField(blank=True, null=True)
    first_sign_date = models.DateTimeField(blank=True, null=True)
    second_sign_date = models.DateTimeField(blank=True, null=True)
    task_create_date = models.DateTimeField(blank=True, null=True)
    task_last_edit = models.DateTimeField(blank=True, null=True)
    task_status = models.IntegerField()
    incoming_date = models.DateTimeField(blank=True, null=True)
    incoming_employee = models.ForeignKey(TodoTasksEmployee, models.DO_NOTHING, blank=True, null=True)
    incoming_status = models.BooleanField()
    cpe_comment = models.TextField(blank=True, null=True)
    incoming_dep = models.ForeignKey(TodoTasksCommandnumbermodel, models.DO_NOTHING, blank=True, null=True)
    task_workers = models.BooleanField()
    task_building = models.CharField(max_length=150, blank=True, null=True)
    task_approved = models.BooleanField()
    task_need_approve = models.BooleanField()
    task_mark_doc = models.ForeignKey(TodoTasksMarkdocmodel, models.DO_NOTHING, blank=True, null=True)
    task_stage = models.ForeignKey(TodoTasksStagemodel, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ToDo_tasks_taskmodel'


class TodoTasksTasknumbersmodel(models.Model):
    count_of_task = models.IntegerField()
    command_number = models.ForeignKey(TodoTasksCommandnumbermodel, models.DO_NOTHING)
    year_of_task = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ToDo_tasks_tasknumbersmodel'


class TodoTasksTasksinfavoritesmodel(models.Model):
    favorite_list = models.ForeignKey(TodoTasksFavoriteslistmodel, models.DO_NOTHING)
    favorite_task = models.ForeignKey(TodoTasksTaskmodel, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ToDo_tasks_tasksinfavoritesmodel'


class TodoTasksWorkermodel(models.Model):
    read_status = models.BooleanField()
    task = models.ForeignKey(TodoTasksTaskmodel, models.DO_NOTHING, blank=True, null=True)
    worker_user = models.ForeignKey(TodoTasksEmployee, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ToDo_tasks_workermodel'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
