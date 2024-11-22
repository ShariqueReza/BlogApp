from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_image=models.ImageField(null=True,blank=True,upload_to="images/")
    slug=models.SlugField(max_length=200,unique=True)
    bio=models.CharField(max_length=200)

    def save(self,*args, **kwargs):
        if not self.id:
            self.slug=slugify(self.user.username)
        return super(Profile,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.user.first_name

class Subscribe(models.Model):
    email=models.EmailField(max_length=100)
    date=models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    slug=models.SlugField(max_length=200,unique=True)

    def save(self,*args, **kwargs):
        if not self.id:
            self.slug=slugify(self.name)
        return super(Tag,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    last_updates=models.DateTimeField(auto_now=True)
    slug=models.SlugField(max_length=200,unique=True)
    image=models.ImageField(null=True,blank=True,upload_to="images/")
    tags=models.ManyToManyField(Tag,blank=True,related_name='post')
    view_count=models.IntegerField(null=True,blank=True)
    is_featured=models.BooleanField(default=False)
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    bookmarks=models.ManyToManyField(User,related_name="booksmarks",default=None,blank=True)

class Comments(models.Model):
    content=models.TextField()
    date=models.DateTimeField(auto_now=True)
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    website=models.CharField(max_length=200)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    #for reply of the particular comment
    parent=models.ForeignKey('self',on_delete=models.DO_NOTHING,null=True,blank=True,related_name='replies')

class WebsiteMeta(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=500)
    about=models.TextField()
