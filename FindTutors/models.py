from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, UserManager
from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class TUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, default='0')
    email = models.EmailField(('email address'), unique=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phone_number = models.IntegerField(blank=True, null=True)
    is_tutee = models.BooleanField('student status', default=False)
    is_tutor = models.BooleanField('teacher status', default=False)
    year = models.IntegerField(blank=True, null=True)
    subjects = models.CharField(max_length=500, default="")
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


# profile of tutee?
class Profile(models.Model):
    user = models.OneToOneField(TUser, on_delete=models.CASCADE)
    firstname = TUser.firstname
    lastname = TUser.lastname
    image = models.ImageField(default='default.jpg',
                              upload_to='profile_pictures')

    FIRST = '1st'
    SECOND = '2nd'
    THIRD = '3rd'
    FOURTH = '4th'
    YEAR_CHOICES = (
        (FIRST, 'First Year'),
        (SECOND, 'Second Year'),
        (THIRD, 'Third Year'),
        (FOURTH, 'Fourth Year'),
    )
    year = models.CharField(max_length=3, choices=YEAR_CHOICES, default=FIRST)

    TUTOR = 'tutor'
    TUTEE = 'tutee'
    BOTH = 'tutor_tutee'
    USER_CHOICES = (
        (FIRST, 'Tutor'),
        (SECOND, 'Tutee'),
        (THIRD, 'Tutor and Tutee'),
    )
    user_type = models.CharField(
        max_length=15, choices=USER_CHOICES, default=TUTOR)
    subjects = models.CharField(max_length=500, default="")
    bio = models.TextField(default=' ')

    def __str__(self):
        return "%s's profile" % self.user

    def save(self, *args, **kwargs):
        super().save()


@receiver(post_save, sender=TUser)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
