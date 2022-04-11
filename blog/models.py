from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# from . models import Review 
# import blog.models
# from django import forms 

# from django.contrib.contenttypes.fields import GenericRelation
# from star_ratings.models import Rating




class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pics', default='')
    link = models.URLField(max_length=200, blank=True, default='provide a Link to your cute repo')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Review(models.Model):
    author = models.CharField(max_length=40, default="anonymous")
    review_date = models.DateTimeField(default=timezone.now)
    rate_choices = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    )
    stars = models.IntegerField(choices=rate_choices)
    comment = models.TextField(max_length=4000)
    post = models.ForeignKey("blog.Review", on_delete=models.CASCADE, verbose_name="Review")

    def __str__(self):
        return self.post.title



# class ReviewForm(forms.ModelForm):

#     class Meta:
#         model = Review
#         fields = ["author","stars","comment"]



