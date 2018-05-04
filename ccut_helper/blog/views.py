from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from serializer import LoginSerializer,StudentSerilizer,BlogSerializer,ChangePasswordSerializer,ChangeImageSerializer,ChangeNicknameSerializer
from blog.models import Student,Blog
# Create your views here.

class See_Students(APIView):
    def get(self,request,id,format = None):
        try:
            students = Student.objects.get(id=id)
        except:
            return Response('no_student', status.HTTP_400_BAD_REQUEST)
        s = StudentSerilizer(students)
        #many=True要加，因为有多个学生
        return Response(s.data, status.HTTP_200_OK)


class See_Blog(APIView):
    def get(self,request,user_id,format = None):
        try:
            blog = Blog.objects.filter(blog__user_id=user_id)
        except:
            return Response('no_blog', status.HTTP_400_BAD_REQUEST)
        s = BlogSerializer(blog,many=True)
        return Response(s.data, status.HTTP_200_OK)


class Login(APIView):
    def post(self,request,format=None):
        try:
            user_id = request.data['user_id']
            user_password = request.data['user_password']

        except :
            return Response('bad_post',status.HTTP_404_NOT_FOUND)
        try:
            user = Student.objects.get(user_id__exact=user_id, user_password__exact=user_password)

        except :
            return Response('error', status.HTTP_404_NOT_FOUND)

        if user :
            s = LoginSerializer(user)
            return Response(s.data,status.HTTP_200_OK)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)


class Changes(APIView):
    def post(self,request,format=None):
        try :
            affairs = request.data['affairs']
        except :
            return Response('bad_post', status.HTTP_400_BAD_REQUEST)
        #选择事务
        if affairs == 'change_password':
            try :
                user_id = request.data['user_id']
                oldpassword = request.data['oldpassword']
                newpassword = request.data['newpassword']
            except:
                return Response('bad_post', status.HTTP_400_BAD_REQUEST)
            if oldpassword == newpassword :
                return Response('same_pwd', status.HTTP_400_BAD_REQUEST)
            else:
                try :
                    student = Student.objects.get(user_id__exact=user_id)
                except:
                    return Response('no_student', status.HTTP_400_BAD_REQUEST)
                if student.user_password != oldpassword :
                    return Response('pwd_error', status.HTTP_400_BAD_REQUEST)
                else:
                    student.user_password=newpassword
                    student.save()
                    s = ChangePasswordSerializer(student)
                    return Response(s.data,status.HTTP_200_OK)

        elif affairs == 'change_image':
            try :
                user_id = request.data['user_id']
            except:
                return Response('bad_post', status.HTTP_400_BAD_REQUEST)
            try:
                student = Student.objects.get(user_id__exact=user_id)
            except:
                return Response('no_student', status.HTTP_400_BAD_REQUEST)
            image = request.data['image']
            student.user_image=image
            student.save()
            s = ChangeImageSerializer(student)
            return Response(s.data,status.HTTP_200_OK)

        elif affairs == 'change_nickname':
            try :
                user_id = request.data['user_id']
                user_nickname = request.data['user_nickname']
            except:
                return Response('bad_post', status.HTTP_400_BAD_REQUEST)
            try:
                student = Student.objects.get(user_id__exact=user_id)
            except:
                return Response('no_student', status.HTTP_400_BAD_REQUEST)
            student.user_nickname = user_nickname
            student.save()
            s = ChangeNicknameSerializer(student)
            return Response(s.data,status.HTTP_200_OK)


class PutBlog(APIView):
    def post(self,request,format=None):
        try:
            user_id = request.data['user_id']
            title = request.data['title']
            text = request.data['text']
            iscomment = request.data['iscomment']
            image1 = request.data['image1']
            image2 = request.data['image2']
            image3 = request.data['image3']
            image4 = request.data['image4']
            image5 = request.data['image5']
            image6 = request.data['image6']
            image7 = request.data['image7']
            image8 = request.data['image8']
            image9 = request.data['image9']
            blog_label = request.data['blog_label']
        except Exception as e:
            print(e)
            return Response('post_error',status.HTTP_400_BAD_REQUEST)
        try:
            student = Student.objects.get(user_id__exact=user_id)
        except:
            return Response('no_student', status.HTTP_400_BAD_REQUEST)
        blog = Blog.objects.create(
            blog=student,
            blog_title=title,
            blog_text=text,
            blog_image1=image1,
            blog_image2=image2,
            blog_image3=image3,
            blog_image4=image4,
            blog_image5=image5,
            blog_image6=image6,
            blog_image7=image7,
            blog_image8=image8,
            blog_image9=image9,
            blog_iscomment=iscomment,
            blog_label=blog_label
                                   )
        blog.save()
        s = BlogSerializer(blog)
        return Response(s.data,status.HTTP_200_OK)


class DeleteBlog(APIView):
    def delete(self,request,id):
        blog = Blog.objects.get(id=id)
        blog.delete()
        s = BlogSerializer(blog)
        return Response(s.data,status.HTTP_200_OK)