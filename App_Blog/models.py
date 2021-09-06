from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    author=models.ForeignKey(User,related_name='author_post',on_delete=models.CASCADE)
    blog_title=models.CharField(max_length=250,verbose_name="Type Blog title")
    slug=models.SlugField(max_length=265,unique=True)
    blog_content=models.TextField(verbose_name="Write Your content")
    blog_image=models.ImageField(upload_to="blog_image",verbose_name="BlogImage")
    publish_date=models.DateField(auto_now_add=True)
    update_date=models.DateField(auto_now=True)

    class Meta:
        ordering=['-publish_date']

    def __str__(self):
      return self.blog_title
  





class Comment(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="blog_comment")
    user=models.ForeignKey(User,related_name="user_commnent",on_delete=models.CASCADE)
    comment=models.TextField()
    comment_date=models.DateField(auto_now_add=True)
 
    class Meta:
        ordering=['-comment_date']

    def __str__(self):
      return self.comment

class Like(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="Like")
    user=models.ForeignKey(User,related_name="user_like",on_delete=models.CASCADE)
