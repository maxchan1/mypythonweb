from django.db import models

# Create your models here.

class User(models.Model):
    gender = (
        ("male","男"),
        ('female','女'),
    )

    name = models.CharField(max_length=256)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32,choices=gender,default='男')
    c_time = models.DateTimeField(auto_now_add=True)
    has_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"

class ConfirmString(models.Model):
    """
       Stores a single blog entry, related to :model:`login.User` and
       :model:`auth.User`.
       """
    code = models.CharField(max_length=256)
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name+":    "+self.code

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"