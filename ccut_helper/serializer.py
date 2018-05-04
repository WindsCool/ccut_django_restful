from blog.models import Student,Blog
from rest_framework import serializers



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id','blog_adddate','blog_title','blog_label','blog_text','blog_iscomment',)


class StudentSerilizer(serializers.ModelSerializer):
    blog =BlogSerializer(many=True, read_only=True)
    class Meta:
        model = Student
        fields = ('id','user_id','user_password','user_nickname','blog',)


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('user_id',)


class ChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('user_password',)


class ChangeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('user_nickname',)


class ChangeNicknameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('user_nickname',)


class DeleteBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('blog_title',)