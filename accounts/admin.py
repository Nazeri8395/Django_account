# from django.contrib  import admin
# from django.contrib.auth.admin import UserAdmin
from  .forms  import UserChangeForm,UserCreationForm
# from .models import CustomUser

# #================================================================
# @admin.register(CustomUser)
# class  CustomUserAdmin(UserAdmin):
#     form=UserChangeForm
#     add_form=UserCreationForm
#     list_display=('mobile_number','email','name','family','gender','is_active','is_admin')
#     list_filter=('is_active','is_admin','family')
#     # fieldsets = (
#     #     (None, {
#     #         "fields": (
#     #             'mobile_number','password'
#     #         ),
#     #     }),
#     #  ('personal info',{'fields':('email','name','family','gender','active_code')}),
#     #  ('permissions',{'fields':('is_active','is_admin','is_superuser','groups','user_permissions')}),
#     # )
#     # add_fieldsets=(
#     #         (None,{
#     #             'fields':(
#     #                 'mobile_number','email','name','family','gender','active_code','password1','password2'
#     #                 )
#     #         })   
#     # )
#     search_fields=('mobile_number',)
#     ordering=('mobile_number',)
#     # filter_horizontal=('groups','user_permissions')


# # ==============================================







from django.contrib import admin
from .models import CustomUser
from .forms import RegisterUserForm

class CustomUserAdmin(admin.ModelAdmin):
    form=UserChangeForm
    add_form=UserCreationForm
    form = RegisterUserForm
    list_display = ('mobile_number', 'email', 'name', 'family', 'is_active')
    fieldsets = (
        (None, {
            "fields": ('mobile_number', 'password'),
        }),
        ('Personal info', {
            'fields': ('email', 'name', 'family', 'gender'),
        }),
        
    )
    
    add_fieldsets = (
        (None, {
            'fields': ('mobile_number', 'email', 'name', 'family', 'gender', 'password1', 'password2')
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)