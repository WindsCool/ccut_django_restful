from django.db import models
from django.utils.timezone import now
from PIL import Image

class Student(models.Model):
    user_id = models.IntegerField(verbose_name='用户ID',blank=False)
    user_nickname = models.CharField(verbose_name='昵称',max_length=20,blank=False,default='例如   XXX')
    user_password = models.CharField('密码',max_length=16,blank=False,default='123456')
    user_image = models.ImageField(verbose_name='头像')

    def __str__(self):
        return self.user_nickname

    class Meta:
        ordering = ('user_id',)


class Blog(models.Model):
    atomic = False
    labels = (
        (0, '失物招领'),
        (1, '卖室友'),
        (2, '找朋友'),
        (3, '广告'),
        (4, '发心情')
    )
    blog = models.ForeignKey(Student, related_name='friend1', on_delete=True)
    blog_adddate = models.DateTimeField(verbose_name='发帖时间', default=now)
    blog_title = models.CharField(max_length=20, blank=False, default='********')
    blog_label = models.IntegerField(choices=labels, default=1)
    blog_text = models.TextField(blank=False)
    blog_image1 = models.ImageField(upload_to='images', blank=True, default='')
    blog_image2 = models.ImageField(upload_to='images', blank=True, default='')
    blog_image3 = models.ImageField(upload_to='images', blank=True, default='')
    blog_image4 = models.ImageField(upload_to='images', blank=True, default='')
    blog_image5 = models.ImageField(upload_to='images', blank=True, default='')
    blog_image6 = models.ImageField(upload_to='images', blank=True, default='')
    blog_image7 = models.ImageField(upload_to='images', blank=True, default='')
    blog_image8 = models.ImageField(upload_to='images', blank=True, default='')
    blog_image9 = models.ImageField(upload_to='images', blank=True, default='')
    blog_iscomment = models.BooleanField(blank=False, default=True)#是否允许评论

    def __str__(self):
        return self.blog.user_nickname

    class Meta:
        ordering = ('blog_adddate',)


class Comment(models.Model):
    comment = models.ForeignKey(Blog,related_name='friend2',on_delete=True)
    comment_content = models.TextField(verbose_name='评论区')
    comment_time = models.DateTimeField(verbose_name='评论时间', default=now)

    def __str__(self):
        return 'comment'

    class Meta:
        ordering = ('comment_time',)


class Agree(models.Model):
    agree = models.ForeignKey(Blog,related_name='friend3',on_delete=True)
    agree_time = models.DateTimeField(verbose_name='点赞时间', default=now)

    def __str__(self):
        return self.agree.blog.user_nickname + '的赞'


class Fan(models.Model):
    fan = models.ForeignKey(Student, related_name='friend4', on_delete=True)

    def __str__(self):
        return self.fan.user_nickname + '的粉丝'


