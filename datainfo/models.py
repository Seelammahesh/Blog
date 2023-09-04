from django.db import models
# Create your models here.
class User(models.Model):
    user_name=models.CharField(max_length=255)
    mobile_number=models.IntegerField()
    user_info=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.user_name

class Blog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=255 )
    blog_description=models.TextField(null=True,blank=True)
    created_on=models.DateTimeField(auto_now_add=True,)
    updated_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
class BlogComments(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    user=models.CharField(max_length=255,null=True)
    comment=models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.blog)