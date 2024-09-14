from django.db import models
from typing import Any

class Post(models.Model):

    CATEGORIES = [
        ('CHAN', 'Changes'),
        ('TIPS', 'Tips'),
        ('NEWS', 'News')
    ]

    date: str = models.DateField()
    title: str = models.CharField(max_length= 300, verbose_name= 'Title')
    category: str = models.TextField(max_length= 4, choices= CATEGORIES, verbose_name= 'Category')
    heading: str = models.TextField(verbose_name= 'Heading', null= True, blank= True)
    reason: str = models.TextField(verbose_name= 'Reason', null= True, blank= True)
    affected: str = models.TextField(verbose_name= 'Who is affected', null= True, blank= True)
    consecuences: str = models.TextField(verbose_name= 'Consecuences', null= True, blank= True)
    image: Any = models.ImageField(upload_to= 'blog')

    class Meta:

        verbose_name: str = 'Post'
        verbose_name_plural: str = 'Posts'
        ordering = ['date']