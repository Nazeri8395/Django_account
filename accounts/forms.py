from typing import Any
from  django  import forms
from .models import CustomUser
from  django.forms import ModelForm
from django.core.exceptions  import ValidationError 
from django.contrib.auth.forms  import  ReadOnlyPasswordHashField
import re

#========================================================
class UserCreationForm(forms.ModelForm):
    password1=forms.CharField(label='password',widget=forms.PasswordInput)
    password2=forms.CharField(label='Repassword',widget=forms.PasswordInput)
    
    class Meta:
        model=CustomUser
        fields=['mobile_number','email','name','family','gender']
    def clean_password2(self):
            pass1=self.cleaned_data["password1"]
            pass2=self.cleaned_data["password2"]
            if pass1 and pass2 and pass1!=pass2:
                raise  ValidationError("رمز  و رمز عبور با هم مغایرت دارند")
            return pass2
        
    def save(self,commit=True):
            user=super().save(commit=False)
            user.set_password(self.cleaned_data['password1'])
            if commit:
                user.save()
            return user
        

#----------------------------------------------------------------------------------
class  UserChangeForm(forms.ModelForm):
    password=ReadOnlyPasswordHashField(help_text="برای تغییر رمز عبور روی  <a href='../password'> لینک</a>کلیک کنید")
    class Meta:
        model=CustomUser
        fields=['mobile_number','password','email','name','family','gender','is_active','is_admin']
        
#-----------------------------------------------------------------------------------
class RegisterUserForm(forms.ModelForm):
    password1=forms.CharField(label='password',widget=forms.PasswordInput({
                            'class':'form_control',
                            'placeholder':'رمز عبور را وارد کنید'})
                            )
    password2=forms.CharField(label='Repassword',widget=forms.PasswordInput({
                            'class':'form_control',
                            'placeholder':'تکرار رمز عبور را وارد کنید'})
                            )
    
    class Meta:
        model=CustomUser
        fields=['mobile_number']
        widgets={
            'mobile_number':forms.TextInput(attrs={
                'class':'form_control','placeholder':'موبایل خود را وارد کنید'
            })
        }
        
    def clean_password2(self):
        pass1=self.cleaned_data['password1']
        pass2=self.cleaned_data['password2']
        if pass1 and pass2 and pass1!=pass2:
            raise ValidationError('رمز عبور و تکرار با هم مغایرت دارند')
        #بررسی شرایط پسورد
        password_regex = r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[_@#$]).{8,}$'
        if not re.match(password_regex, pass1):
            raise ValidationError('پسورد باید حداقل شامل حرف، عدد و یکی از علامت‌های _، @، # یا $ باشد و حداقل 8 کاراکتر طول داشته باشد.')

        return pass2
    
    def clean_mobile_number(self):
        mobile_number = self.cleaned_data.get('mobile_number')
        #بررسی اینکه حتما شماره موبایل با 0 شروع شود
        if not mobile_number.startswith("0"):
            raise ValidationError("شماره موبایل را درست وارد کنید. مثال09125678990")
        if not re.match(r'^\d{11}$', mobile_number):
            raise ValidationError('شماره موبایل باید 11 رقمی و فقط شامل اعداد باشد.')
        return mobile_number


    
    
#------------------------------------------------------------------------
class VerifyRegisterForm(forms.Form):
    active_code=forms.CharField(label='کدفعال سازی',
                    error_messages={'required':'این فیلد نمی تواند خالی باشد'}
                    )

#------------------------------------------------------------------------
class LoginUserForm(forms.Form):
    mobile_number=forms.CharField(label="شمـاره مـوبایـل",
                                  error_messages={'required': 'این فیلد نمی تواند خالی رها شود'},
                                  widget=forms.TextInput(attrs={'placeholder':'شماره موبایل خود را وارد کنید'})
                                  )
    password=forms.CharField(label="رمــز عبـور",
                                error_messages={'required': 'این فیلد نمی تواند خالی رها شود'},
                                widget=forms.PasswordInput(attrs={'placeholder':'رمز خود را وارد کنید'})
              
                            )

#-------------------------تغییر پسورد و فراموشی رمز عبور -------------------------
class  changePasswordForm(forms.Form):
    password1=forms.CharField(label='رمز عبـور',error_messages={'required':'این فیلد نمی تواند خالی رها شود'},
                    widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'رمز عبور را وارد کنید'}))
    
    password2=forms.CharField(label='تکرار رمز عبـور',error_messages={'required':'این فیلد نمی تواند خالی رها شود'},
                    widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'رمز عبور را وارد کنید'}))
    
    def clean_password2(self):
        pass1=self.cleaned_data['password1']
        pass2=self.cleaned_data['password2']
        if pass1 and pass2 and pass2!=pass1:
            raise ValidationError("رمز عبور و تکرار آن با هم مغایرت دارند")    
        return pass2
    
#----------------------------- فراموشی رمز عبور -----------------------------------
class RememberPasswordForm(forms.Form):
    mobile_number=forms.CharField(label='شماره موبـایل',
                                  error_messages={'required':'این فیلد نمی تواند خالی رها شود'},
                                  widget=forms.TextInput(attrs={'class':'form-control','placeholder':'شماره موبایل را وارد کنید'}))
    
