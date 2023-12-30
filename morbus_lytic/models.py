from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models import CharField, EmailField, BooleanField
from django.utils.translation import gettext_lazy as _

#======================================================================================================================#
# UserManager
#======================================================================================================================#

class UserManager(BaseUserManager):

    def create_user(self, username: str, email: str, password: str) -> AbstractBaseUser:
        if not username:
            raise ValueError('username must be provided')

        if not email:
            raise ValueError('email must be provided')

        if not password:
            raise ValueError('password must be provided')

        user = self.model(username = username, email = self.normalize_email(email))

        user.set_password(password)
        user.save(using = self._db)

        return user

    #------------------------------------------------------------------------------------------------------------------#

    def create_superuser(self, username: str, email: str, password: str) -> AbstractBaseUser:
        user = self.create_user(username, email, password)
        
        user.is_admin = True
        user.is_superuser = True
        user.save(using = self._db)
        
        return user

#======================================================================================================================#
# End of UserManager
#======================================================================================================================#
# User
#======================================================================================================================#

class User(AbstractBaseUser):

    class Meta:
        db_table = 'user'

    #------------------------------------------------------------------------------------------------------------------#

    objects = UserManager()

    #------------------------------------------------------------------------------------------------------------------#

    username = CharField(max_length = 255, unique = True)
    email = EmailField(max_length = 255, unique = True)
    
    is_active = BooleanField(default = True)
    is_admin = BooleanField(default = False)
    is_superuser = BooleanField(default = False)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    #------------------------------------------------------------------------------------------------------------------#

    def get_full_name(self) -> str:
        return self.username

    #------------------------------------------------------------------------------------------------------------------#

    def get_short_name(self) -> str:
        return self.username

    #------------------------------------------------------------------------------------------------------------------#

    def __str__(self) -> str:
        return self.username

    #------------------------------------------------------------------------------------------------------------------#

    @property
    def is_staff(self) -> bool:
        return self.is_superuser

    #------------------------------------------------------------------------------------------------------------------#

    def has_perm(self, perm, obj = None) -> bool:
        return True

    #------------------------------------------------------------------------------------------------------------------#

    def has_module_perms(self, app_label) -> bool:
        return True

#======================================================================================================================#
# End of User
#======================================================================================================================#
