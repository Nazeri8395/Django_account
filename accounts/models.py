# from django.db import models
# from  django.utils.translation  import  gettext as _ 
# from django.contrib.auth.models import  AbstractBaseUser,PermissionsMixin,BaseUserManager,UserManager
# from django.utils import timezone
# from utils import FileUpload

# #===========================================================================
# class CustomUserManager(BaseUserManager):
    
#     def create_user(self,mobile_number,email="",name="",family="",active_code=None,gender=None,password=None):
#         if not mobile_number:
#             raise ValueError(_('Enter the mobile number')) 
    
#         user=self.model(
#             mobile_number=mobile_number,
#             email=self.normalize_email(email),
#             name=name,
#             family=family,
#             active_code=active_code,
#             gender=gender,
#         )
    
#         user.set_password(password)
    
#         user.save(using=self._db)
    
#         return user
        
#     def create_superuser(self,mobile_number,email="",name="",family="",active_code=None,gender=None,password=None ):
     
#         user=self.create_user(
#             mobile_number=mobile_number,
#             email=email,
#             name=name,
#             family=family,
#             active_code=active_code,
#             gender=gender,
#             password=password
#         )  
    
#         user.is_active=True
    
#         user.is_admin=True
    
#         user.is_superuser=True
    
#         user.set_password(password)
    
#         user.save(using=self._db)
    
#         return user

# #---------------------------------------------------------------------------
# class CustomUser(AbstractBaseUser,PermissionsMixin):
    
#     mobile_number=models.CharField(_("Mobile Number"), max_length=11, unique=True)
    
#     email=models.EmailField(_("email"), max_length=200, blank=True, unique=True)
    
#     name=models.CharField(_("first name"), max_length=50, blank=True)
    
#     family=models.CharField(_("last name"), max_length=50, blank=True)
    
#     file_upload = FileUpload('images','avatar')
#     avatar_identifier = models.ImageField(
#         _("avatar_identifier"), upload_to = file_upload.upload_to, blank=True, null=True
#     )
    
#     GENDER_CHOISE = (
#                 ('M', _('Male')),
#                 ('F', _("Female")),
#             )
#     gender=models.CharField(_("Gender"), max_length=20, choices=GENDER_CHOISE,
#                             default='True', null=True, blank=True
#                             )
    
#     USER_TYPE_CHOICES = [
#         ("regular", _("Regular")),#عادی
#         ("legal", _("Legal")), # قانونی
#         ("teacher", _("Teacher")),#استاد
#     ]
#     user_type = models.CharField(_("user type"), max_length=10,
#                                  choices=USER_TYPE_CHOICES, default="regular"
#                                 )
    
#     register_date=models.DateField(_('Register Date'),default=timezone.now)
    
#     is_active=models.BooleanField(_("Active"),default=False)
    
#     active_code=models.CharField(_("Active Code"),max_length=100,null=True,blank=True)
    
#     is_admin=models.BooleanField(_("Admin"),default=False)
    
#     USERNAME_FIELD='mobile_number'
    
#     REQUIRED_FIELDS=['email','name','family']
    
#     objects=CustomUserManager()
    
    
#     class Meta:
#         verbose_name = _("User")
#         verbose_name_plural = _("Users")
    
#     def __str__(self):
#         return self.name+" "+self.family
    

#     @property
#     def is_staff(self):
#         return self.is_admin






from django.db import models
from  django.utils.translation  import  gettext as _ 
from django.contrib.auth.models import  AbstractBaseUser,PermissionsMixin,BaseUserManager,UserManager
from django.utils import timezone
from utils import FileUpload

#===========================================================================
class CustomUserManager(BaseUserManager):
    
    def create_user(self,mobile_number,email="",name="",family="",active_code=None,gender=None,password=None):
        if not mobile_number:
            raise ValueError(_('Enter the mobile number')) 
    
        user=self.model(
            mobile_number=mobile_number,
            email=self.normalize_email(email),
            name=name,
            family=family,
            active_code=active_code,
            gender=gender,
        )
    
        user.set_password(password)
    
        user.save(using=self._db)
    
        return user
        
    def create_superuser(self,mobile_number,email="",name="",family="",active_code=None,gender=None,password=None ):
     
        user=self.create_user(
            mobile_number=mobile_number,
            email=email,
            name=name,
            family=family,
            active_code=active_code,
            gender=gender,
            password=password
        )  
    
        user.is_active=True
    
        user.is_admin=True
    
        user.is_superuser=True
    
        user.set_password(password)
    
        user.save(using=self._db)
    
        return user

#---------------------------------------------------------------------------
class CustomUser(AbstractBaseUser,PermissionsMixin):
    
    mobile_number=models.CharField(_("Mobile Number"), max_length=11, unique=True)
    
    email=models.EmailField(_("email"), max_length=200, blank=True, unique=True)
    
    name=models.CharField(_("first name"), max_length=50, blank=True)
    
    family=models.CharField(_("last name"), max_length=50, blank=True)
    
    file_upload = FileUpload('images','avatar')
    avatar_identifier = models.ImageField(
        _("avatar_identifier"), upload_to = file_upload.upload_to, blank=True, null=True
    )
    
    GENDER_CHOISE=(
                ('True',_('Male')),
                ('False',_("Female "))
        )
    gender=models.CharField(_("Gender"), max_length=20, choices=GENDER_CHOISE,
                            default='True', null=True, blank=True
                            )
    
    USER_TYPE_CHOICES = [
        ("regular", _("Regular")),#عادی
        ("legal", _("Legal")), # قانونی
        ("teacher", _("Teacher")),#استاد
    ]
    user_type = models.CharField(_("user type"), max_length=10,
                                 choices=USER_TYPE_CHOICES, default="regular"
                                )
    
    register_date=models.DateField(_('Register Date'),default=timezone.now)
    
    is_active=models.BooleanField(_("Active"),default=False)
    
    active_code=models.CharField(_("Active Code"),max_length=100,null=True,blank=True)
    
    is_admin=models.BooleanField(_("Admin"),default=False)
    
    USERNAME_FIELD='mobile_number'
    
    REQUIRED_FIELDS=['email','name','family']
    
    objects=CustomUserManager()
    
    
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
    
    def __str__(self) -> str:
        return self.name+" "+self.family
    

    @property
    def is_staff(self):
        return self.is_admin
