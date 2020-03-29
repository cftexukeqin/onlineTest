from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):

    gender_choices = (
        ('male','男'),
        ('female','女'),
    )

    department_choices = (
        ('dep_one','一大队'),
        ('dep_two','二大队'),
        ('dep_three','三大队'),
        ('dep_six','六大队'),
        ('dep_seven','七大队'),
    )

    major_choices = (
        ('jixie','机械'),
        ('teshe','特设'),
        ('hangdian','航电'),
        ('junxie','军械'),
        ('feican','飞参'),
    )

    nick_name = models.CharField(max_length=50, verbose_name=u"姓名", default = '')
    major = models.CharField(max_length=50,verbose_name=u"专业",choices=major_choices,default = 'jixie')
    department = models.CharField(max_length=50,verbose_name=u"部门",choices=department_choices,default='dep_two')
    gender = models.CharField(max_length=50,verbose_name=u"性别",choices=gender_choices,default='male')
    birthday = models.DateField(verbose_name=u"生日",null=True,blank=True)
    image = models.ImageField(upload_to='image/%Y%m',default='image/default.png',max_length=100)
    status = models.IntegerField(verbose_name=u"考试状态", default=0)#0考试中，1是未考试.

    job_code = models.IntegerField(default=0)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username  #在默认数据库中


class EmailVerifyRecord(models.Model):
    send_choices = (
        ('register','注册'),
        ('forget','找回密码')
    )

    code = models.CharField('验证码',max_length=20)
    email = models.EmailField('邮箱',max_length=50)
    send_type = models.CharField('验证码类型',choices=send_choices,max_length=10)
    send_time = models.DateTimeField('发送时间',default=datetime.now)

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name