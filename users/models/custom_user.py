from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


class CustomUserManager(BaseUserManager):
    def create_user(self, fullname: str, email: str, password: str = None):
        """
        Creates and saves a User with the given email and password
        """
        if not email:
            raise ValueError('Users must have an email!')

        if not password:
            raise ValueError('All users must have a password!')
        email = self.normalize_email(email)
        user = self.model(
            fullname=fullname.upper(),
            email=email,
            username=email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, fullname, email, password):
        """
       Create and saves a staff users with the given email and password
        """
        user = self.create_user(
            fullname,
            email,
            password=password,
        )

        user.staff = True
        user.save(using=self._db)

    def create_superuser(self, fullname, email, password):
        """
       Create and saves a superuser with the given email and password
        """
        user = self.create_user(
            fullname,
            email,
            password=password,
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)


class CustomUser(AbstractUser):
    fullname = models.CharField(verbose_name='Nome completo', max_length=200)
    objects = CustomUserManager()
    email = models.EmailField(
        verbose_name='E-mail',
        max_length=255,
        unique=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname']

    def get_full_name(self):
        return self.fullname

    def get_short_name(self):
        return self.fullname.split(' ')[0]

    def __str__(self):
        return self.email
