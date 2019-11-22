from django.db import models
import datetime,uuid
from django.utils import timezone
from django.forms import ModelForm

# Create your models here.
class Comment(models.Model):
    title = models.CharField(verbose_name='评论标题',max_length=50)
    content = models.TextField(max_length=10)
    parent_cmt = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)
    ctime = models.DateTimeField(auto_now=True)

class ModelFile(models.Model):
    upload = models.FileField(verbose_name='上传文件',upload_to='uploads/')
    imagefd = models.ImageField(upload_to='upimages/')
    uuid = models.UUIDField(default=uuid.uuid4(),editable=False)
    pathfiles = models.FilePathField(path='F:\\工作文档')
    text = models.CharField(max_length=32)

class FileForm(ModelForm):
    class Meta:
        model = ModelFile
        fields = ['upload','imagefd','pathfiles','text']

class userinfo(models.Model):
    #如果没有models.AutoField，默认会创建一个id的自增列
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=256)
    email = models.EmailField()
    addr = models.TextField()

class question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('发布日期',default=timezone.now)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Publish_Recent'

class Choice(models.Model):
    question = models.ForeignKey(question, on_delete=models.CASCADE,related_name='aboutco')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s the place" % self.name

class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name

class Supplier(Place):
    customers = models.ManyToManyField(Place,related_name='provider')

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

    class Meta(CommonInfo.Meta):
        db_table = 'student_info'