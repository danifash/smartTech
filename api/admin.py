from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

UserAdmin.fieldsets[2][1]['fields'] = (
    'is_active', 'is_staff', 'is_superuser', 'groups', 'phone_number', 'address',
    'user_permissions', 'membership', 'avatar'
)

admin.site.register(models.User, UserAdmin)

admin.site.register(models.Post)
admin.site.register(models.Category)
admin.site.register(models.PostDescription)
admin.site.register(models.PostImgUrl)
admin.site.register(models.Comment)
admin.site.register(models.Rate)
