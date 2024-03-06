from django.contrib.auth.models import User
from django.db import models


class Categories(models.TextChoices):
    """Categories available to the user when posting"""
    FULL_SET_BUILDS = 'full set builds'
    DIY_BUILDS = 'diy builds'

class Post(models.Model):
    """
    Post model is related to the 'owner', owner is a user instance.
    """
    image_filter_choices = [
        ('_1977', '1977'),
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'),
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'),
        ('xpro2', 'X-pro II')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(
        max_length=100, choices=Categories.choices, default=Categories.FULL_SET_BUILDS)
    image = models.ImageField(
        upload_to='images/', default='../default-post-edited_1_b3dicv_e_improve_e_sharpen_v6swmv', blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal')

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.id} {self.title}'