from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User,Blog,BlogComments
from django.db import IntegrityError

# Create your views here.
@api_view(['POST'])
def add_user(request):
    user_name=request.POST.get('user_name',None)
    mobile_number=request.POST.get('mobile_number',None)
    user_info=request.POST.get('user_info',None)
    if user_name is None or mobile_number is None or user_info is None:
        context ={
            'message':'user_name/mobile_number/user_info is missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)

    if not mobile_number.isdigit() or len(mobile_number)!=10:
        context ={
            'message':'invalid mobile number or mobile number should be exactly 10 digits'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    try:
        new_user=User.objects.create(
            user_name=user_name,
            mobile_number=mobile_number,
            user_info=user_info
        )
        new_user.save()
        context={
            'message':'new_user created',
            'data': {
                'user_id': new_user.id,
                'user_name': new_user.user_name,
                'mobile_number': new_user.mobile_number,
                'user_info': new_user.user_info
            }
        }
        return Response(context,status=status.HTTP_200_OK)
    except ValueError:
        context={
            'message':'invalid user data'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_user(request):
    user_list = User.objects.all()
    user_data = []

    if not user_list:
        context = {
            'message': 'No users present'
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    for user in user_list:
        data = {
            'user_id': user.id,
            'user_name': user.user_name,
            'mobile_number': user.mobile_number,
            'user_info': user.user_info
        }
        user_data.append(data)

    context = {
        'data': user_data
    }
    return Response(context, status=status.HTTP_200_OK)

@api_view(['PATCH'])
def update_user(request):
    user_id = request.POST.get('user_id', None)
    new_user_name = request.POST.get('new_user_name', None)
    new_mobile_number = request.POST.get('new_mobile_number', None)
    new_user_info = request.POST.get('new_user_info', None)

    if user_id is None or new_user_name is None or new_mobile_number is None or new_user_info is None:
        context = {
            'message': 'user_id/new_user_name/new_mobile_number/new_user_info  is missing'
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            user = User.objects.get(id=user_id)
            if new_user_name:
                user.user_name = new_user_name
            if new_mobile_number:
                user.mobile_number = new_mobile_number
            if new_user_info:
                user.user_info = new_user_info
            user.save()

            context = {
                'message': "user updated successfully"
            }
            return Response(context, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            context = {
                'message': 'Invalid user_id'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            context = {
                'message': 'Duplicate entry or invalid ID'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            context = {
                'message': 'Invalid user_id'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(request):
    user_id=request.POST.get('user_id',None)
    if user_id is None:
        context ={
            'message':'user id is missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            user=User.objects.get(id=user_id)
            user.delete()
            context = {
                'message': 'user successfully deleted'
            }
            return Response(context, status=status.HTTP_200_OK)
        except ValueError:
            context = {
                'message': 'invalid user id'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_blog(request):
    user_id=request.POST.get('user_id',None)
    title=request.POST.get('title',None)
    blog_description=request.POST.get('blog_description',None)

    if user_id is None or title is None or blog_description is None :
        context ={
            'message':'user_id/title/blog_description/ is missing'
        }
        return  Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            new_blog=Blog.objects.create(
                user_id=user_id,
                title=title,
                blog_description=blog_description,

            )
            new_blog.save()
            context={
                'message':'new blog created',
                'data':{
                    'user_id':new_blog.user_id,
                    'title':new_blog.title,
                    'blog_description':new_blog.blog_description,
                    'created_on':new_blog.created_on,
                    'updated_on':new_blog.updated_on

            }
            }
            return Response(context,status=status.HTTP_200_OK)
        except ValueError:
            context ={
                'message':'invalid blog data'
            }
            return Response(context,status==status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def list_blog(request):
    blogs_list=Blog.objects.all()
    blogs=[]
    if not blogs_list:
        context={
            'message':'empty.no blogs present!'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    for blog in blogs_list:
        data ={
            'user_id':blog.user_id,
            'title':blog.title,
            'blog_description':blog.blog_description,
            'created_on':blog.created_on,
            'updated_on':blog.updated_on

        }
        blogs.append(data)
    context ={
        'data':blogs
        }
    return Response(context,status=status.HTTP_200_OK)

@api_view(['PATCH'])
def update_blog(request):
    blog_id=request.POST.get('blog_id',None)
    new_blog_title=request.POST.get('new_blog_title',None)
    new_blog_description=request.POST.get('new_blog_description',None)
    if blog_id is None or new_blog_title is None or new_blog_description is None:
        context = {
            'message': 'blog_id/new_blog_title/new_blog_description/  is missing'
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            blog = Blog.objects.get(id=blog_id)
            if new_blog_title:
                blog.title = new_blog_title
            if new_blog_description:
                blog.blog_description = new_blog_description
                blog.save()

            context = {
                'message': "blog updated successfully"
            }
            return Response(context, status=status.HTTP_200_OK)

        except Blog.DoesNotExist:
            context = {
                'message': 'Invalid  blog_id'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            context = {
                'message': 'Duplicate entry or invalid blog ID'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            context = {
                'message': 'Invalid blog_id'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_blog(request):
    blog_id = request.POST.get('blog_id', None)
    if blog_id is None:
        context = {
            'message': 'blog id is missing'
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            blog= Blog.objects.get(id=blog_id)
            blog.delete()
            context = {
                'message': ' blog successfully deleted'
            }
            return Response(context, status=status.HTTP_200_OK)
        except ValueError:
            context = {
                'message': 'invalid blog id'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_comment(request):
    blog_id=request.POST.get('blog_id',None)
    user=request.POST.get('user',None)
    comment=request.POST.get('comment',None)
    if blog_id is None or user is None or comment is None:
        context={
            'message':'blog_id/user/comment is missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:

            blog=BlogComments.objects.create(
                blog_id=blog_id,
                user=user,
                comment=comment
            )
            blog.save()
            context ={
                'message':'new comment added',
                'data':{
                    'comment':blog.comment,
                    'user':user

            }
            }
            return Response(context,status=status.HTTP_200_OK)
        except ValueError:
            context ={
                'message':'invalid comment '
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def list_comments(request):
    comments_list = BlogComments.objects.all()
    comments = []
    if not comments_list:
        context = {
            'message': 'empty.no comments present!'
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    for comment in comments_list:
        data = {
            'blog_id':comment.id,
            'user':comment.user,
            'comment':comment.comment
        }
        comments.append(data)
    context = {
        'data': comments
    }
    return Response(context, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_comment(request):
    comment_id = request.POST.get('comment_id', None)
    if comment_id is None:
        context = {
            'message': 'comment id is missing'
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            comment= BlogComments.objects.get(id=comment_id)
            comment.delete()
            context = {
                'message': ' comment successfully deleted'
            }
            return Response(context, status=status.HTTP_200_OK)
        except ValueError:
            context = {
                'message': 'invalid comment id'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)