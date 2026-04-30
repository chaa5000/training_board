from django.db import models

class Component(models.Model):
    name = models.CharField(max_length=100) # اسم المكون مثل ESP32
    description = models.TextField()

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200) # عنوان المشروع
    description = models.TextField() # وصف المشروع
    image = models.ImageField(upload_to='projects/', blank=True) # صورة المشروع
    components = models.ManyToManyField(Component) # المكونات المستخدمة
    code_snippet = models.TextField(blank=True) # كود البرمجة (Arduino/MicroPython)

    def __str__(self):
        return self.title
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False) # الحقل الذي سيتحكم به المدير

    def __str__(self):
        return self.user.username

# كود لإنشاء بروفايل تلقائياً عند تسجيل أي مستخدم جديد
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()