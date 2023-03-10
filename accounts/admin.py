from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


# Register your models here.

admin.site.register(CustomUser)
admin.site.register(UserVerification)




# class UserAdminConfig(UserAdmin):
#     model = CustomUser
#     search_fields = ('email', 'username', 'first_name', 'last_name')
#     ordering = ('-id',)
#     list_display = ('username', 'first_name', 'last_name')
#     fieldsets = (
#         ("Details", {'fields': ('email', 'username', 'password', 'first_name', 'last_name', 'about', 'profile_picture', 
#                                 'email_verified_at', 'is_verified', 'is_admin', 'two_step_auth')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'user_permissions')}),
#         # ('Stripe Details', {'fields': ('stripe_customer_id', 'stripe_customer_response')}),
#     )
#     formfield_overrides = {
#         CustomUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
#     }
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'username', 'first_name', 'last_name', 'mobile_number', 'password1', 'password2', 'is_verified', 'email_verified_at', 'is_active', 'is_staff')}
#          ),
#     )

# admin.site.register(CustomUser, UserAdminConfig)


# class UserVerificationConfig(UserAdmin):

#     model  = UserVerification
#     search_fields = ('email')
#     ordering = ('-id',)
#     list_display = ('email', 'action', 'otp', 'token')

# admin.site.register(UserVerification, UserVerificationConfig)


