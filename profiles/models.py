from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from django.db import models


def image_upload(instance, file):
    """
    Function for uploading profile pictures. Uploads the image to a
    directory with the user's username.
    """
    return f"{instance.user.username}/{file}"


class Profile(models.Model):
    profile_id = models.CharField(primary_key=True, max_length=150)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(max_length=300, blank=True,
                           default="This user likes to keep an air of mystery about them...")  # noqa: E501
    location = models.CharField(max_length=40, blank=True,
                                default="Earth")
    profile_pic = models.ImageField(upload_to=image_upload, blank=True,
                                    null=True)
    address_1 = models.CharField(max_length=80, blank=True, null=True)
    address_2 = models.CharField(max_length=80, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    county = models.CharField(max_length=50, blank=True, null=True)
    post_code = models.CharField(max_length=20, blank=True, null=True)
    country = CountryField(blank_label='Country', blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    """
    Function for creating or updating the user profile
    """
    if created:
        Profile.objects.create(pk=instance, user=instance)
    instance.profile.save()
