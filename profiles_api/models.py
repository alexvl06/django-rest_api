from email.message import EmailMessage
from django.db import models
from  django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserProfileManager(BaseUserManager):
    """User Profile Manager"""
    def create_user(self, email, name, password = None):
        '''creating new user profile'''
        if not email:
            raise ValueError('User must have an email')
        email = self.normalize_email(email)
        user = self.model(name = name, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,name, password):
        '''To create a super user'''
        user= self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """User database model on the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        '''Get full user name'''
        return self.name
    
    def get_short_name(self):
        '''Get short user name'''
        return self.name

    def __str__(self):
        '''Representative user string'''
        return self.email