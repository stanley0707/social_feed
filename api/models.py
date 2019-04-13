from django.db import models
from django.core.cache import cache
#from solo.models import SingletonModel


class SingletonModel(models.Model):
    """ Одиночная модель 
    """
    class Meta:
        abstract = True
    
    def set_cache(self):
        cache.set(self.__class__.__name__, self)
    
    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)
        self.set_cache()

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)
    
    def delete(self, *args, **kwargs):
         pass
    
    # забираем одну единственную модель с
    # неизменных primary_key == 1
    @classmethod
    def get_singl(cls): 
        obj, created = cls.objects.get_or_create(pk=1)
        obj.set_cache()
        return obj



class VkUser(SingletonModel):
    """  Одиночная модель пользовательских данных:
    логин и пароль основного пользователя,
    необходим для авторизации vk api. """
    
    login = models.CharField(max_length=12, blank=True, verbose_name='логинг')
    password = models.CharField(max_length=100, blank=True, verbose_name='пароль')
    
    def __str__(self):
        return '{}, {}'.format(self.login, self.password)


class Media(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name="media")
    url = models.CharField(max_length=500, blank=True, null=True)
    content_type = models.CharField(max_length=5, blank=True, null=True)
    
    def __str__(self):
        return "id альбома: {},  id публикации: {}.".format(self.id, self.post.postid)
    
    def get_url(self):
        return self.url
    
    def get_content_type(self):
        return self.content_type
 

class Post(models.Model):
    user = models.ForeignKey(VkUser, on_delete=models.CASCADE)
    postid = models.CharField(max_length=40, blank=True)
    date = models.CharField(max_length=20, blank=True)
    likes = models.IntegerField()
    title = models.CharField(max_length=4000, blank=True)
    
    def __str__(self):
        return "id публикации   {},     лайков:  {}".format(self.postid, self.likes)

# class LoadSession(models.Model):
#     date_load = models.DateTimeField(auto_now=True)
#     session_id = models.CharField(max_length=40, blank=True)