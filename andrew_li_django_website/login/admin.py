from django.contrib import admin
from login.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email')

    def user_info(self, obj):
        return obj.email

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('user')
        return queryset

admin.site.register(UserProfile, UserProfileAdmin)
