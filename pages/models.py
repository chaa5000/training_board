from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# --- جدول المشاريع التعليمية ---
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان المشروع")
    description = models.TextField(verbose_name="وصف شامل")
    
    connection_table_image = models.ImageField( upload_to='projects/connections/', 
        blank=True, null=True, 
        verbose_name="صورة جدول التوصيلات")
    
    circuit_montage_image = models.ImageField(upload_to='projects/circuits/', 
        blank=True, null=True,  verbose_name="صورة مخطط الدائرة")
    
    # العلاقة التي كانت تسبب مشكلة في الشكل
    components = models.TextField(verbose_name="قائمة مكونات",blank=True,default="")
    
    code_snippet = models.TextField(blank=True, verbose_name="كود البرمجة")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "مشروع"
        verbose_name_plural = "المشاريع"

# --- جدول الملف الشخصي ---
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="المستخدم")
    is_approved = models.BooleanField(default=False, verbose_name="حالة الموافقة") 

    def __str__(self):
        return f"ملف {self.user.username}"

    class Meta:
        verbose_name = "ملف شخصي"
        verbose_name_plural = "ملفات المستخدمين"

# إشارات (Signals)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()