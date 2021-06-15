from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=100)
    describe = models.CharField(max_length=45500)

    def __str__(self):
        return self.title

# from django.db import models
# # Create your models here.
# class Post(models.Model):
#     title = models.CharField(max_length=500)
#     describe = models.CharField(max_length=45500)
#     create_at = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.title