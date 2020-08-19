from django.db import models
from django.urls import reverse
from django.utils import timezone


class Base(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            default='')
    body = models.TextField()
    image = models.ImageField("Изображение",
                              upload_to="media_community/")
    publish = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('village:about_base',
                       args=[self.publish.year,
                             self.publish.day,
                             self.slug])


class ForCommunity(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            default='')
    body = models.TextField()
    image = models.ImageField("Изображение",
                              upload_to="media_community/")
    publish = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('village:about_news',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

    def __str__(self):
        return self.title


class MainPage(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            default='')
    image = models.ImageField("Изображение",
                              upload_to="media_main_page/",
                              blank='True',
                              null='True', )
    text = models.TextField()

    def __str__(self):
        return self.title


class Rule(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            default='')
    document = models.FileField(name='document',
                                default='',
                                upload_to='documentation/',
                                null='True',
                                blank='True')

    def __str__(self):
        return self.title


class RuleInside(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            default='')
    document = models.FileField(name='document',
                                default='',
                                upload_to='documentation/',
                                null='True',
                                blank='True')


class Leadership(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            default='')
    photo = models.ImageField("Фото",
                              upload_to="photo_leadership/",
                              null='True',
                              blank='True')
    position = models.TextField(max_length=250)
    name = models.TextField(max_length=250)
    phone_number = models.TextField(max_length=250)

    def __str__(self):
        return self.title


class Debtors(models.Model):
    Номер_участка = models.CharField(max_length=100, blank=False)
    Сумма_долга = models.CharField(max_length=100, blank=False)

    choices = (
        ('AVAILABLE', 'Item is ready to be purchased'),
        ('SOLD', 'Item Sold'),
        ('RESTOCKING', 'Item restocking in few days')
    )
    Счетчик = models.CharField(max_length=100, default='No issues')

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type : {0} Price : {1}'.format(self.Номер_участка, self.Сумма_долга)


class Целевые(Debtors):
    pass


class Членские(Debtors):
    pass


class Электроэнергия(Debtors):
    pass


class Photo(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            default='')
    photo = models.ImageField("Изображение", upload_to="media/", default="")

    def __str__(self):
        return self.title


class AllPhoto(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            default='')
    photos = models.ManyToManyField(Photo, name='photo')

    def __str__(self):
        return self.title
