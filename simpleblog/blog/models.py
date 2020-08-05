from django.db import models
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserProfileManager(BaseUserManager):

    def create_user(self, email, name, password=None):

        if not email:
            raise ValueError('Users must have an email address.')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with given detials."""

        # Create a new user with the function we created above.
        user = self.create_user(
            email,
            name,
            password
        )

        # Make this user an admin.
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """A user profile in our system"""
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email


class Post(models.Model):
    """post uoloaded by the user"""
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Post)
def slugify_name(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)
