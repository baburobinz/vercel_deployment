from django.contrib import admin
from .models import*
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth.models import User

class mobileInline(admin.StackedInline):

    model = UserMobile

    can_delete = False

    verbose_name = 'UserMobiles'

  


class CustomizedUserAdmin(UserAdmin):

    inlines = (mobileInline, )


admin.site.unregister(User)
admin.site.register(User,CustomizedUserAdmin )
admin.site.register(UserMobile)
admin.site.register(to_do_list)
