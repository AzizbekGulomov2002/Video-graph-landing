from django.db import models

class Slide(models.Model):
    name = models.CharField(max_length=100)
    title = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    title = models.TextField(null=True, blank=True)
    icon = models.ImageField(upload_to='service_icons/', null=True, blank=True)
    def __str__(self):
        return self.name

class Statistic(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField()
    icon = models.ImageField(upload_to='statistics_icons/', null=True, blank=True)

    def __str__(self):
        return self.name



class Team(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_images/')
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    internet = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.full_name



class Blog(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    def __str__(self):
        return self.name

class AboutUs(models.Model):
    text = models.TextField()
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    internet = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    def __str__(self):
        return "About us"
    class Meta:
        verbose_name = "About us"
        verbose_name_plural = "About us"
    
class TypePortfolio(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Portfolio(models.Model):
    type = models.ForeignKey(TypePortfolio, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    video = models.FileField(upload_to='videos', null=True,  blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    def __str__(self):
        return self.name


class Message(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    website = models.URLField(null=True, blank=True)
    message = models.TextField()
    def __str__(self):
        return self.full_name


class Gallery(models.Model):
    VIDEO_TYPE_CHOICES = [
        ('eCommerce', 'eCommerce'),
        ('Magento', 'Magento'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=200, blank=True, null=True)
    video_url = models.URLField()
    image = models.ImageField(upload_to='gallery_images/')
    size_class = models.CharField(max_length=50, choices=[
        ('small__item', 'Small'),
        ('wide__item', 'Wide'),
        ('large__item', 'Large'),
    ])
    video_type = models.CharField(max_length=50, choices=VIDEO_TYPE_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.title if self.title else "Gallery Item"