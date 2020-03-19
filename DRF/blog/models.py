from django.db import models
from DRF import settings


def upload_loaction(instance,filename,**kwargs):
    file_path = 'blog/{author_id}/{title}-{filename}'.format(
        author_id = str(instance.author.id),title=str(instance.title),filename=filename
    )
    return file_path
# Create your models here.log
class BlogPost(models.Model):
    title = models.CharField(max_length=50,null=False,blank=False)
    body = models.TextField(max_length=5000,null=False,blank=False)
    image = models.ImageField(upload_to=upload_loaction,null=False,blank=False)
    date_published = models.DateTimeField(auto_now_add=True,verbose_name='date published')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='date published')
    #author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    slug = models.SlugField(blank=True,unique=True)

    def __str__(self):
        return self.title

