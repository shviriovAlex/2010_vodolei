from django.db import models
from django.urls import reverse
from django.utils import timezone


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


class ДоскаПозора(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            default='')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    photo1 = models.ImageField("Изображение1",
                               upload_to="media_shame",
                               null="True",
                               blank="True")
    photo2 = models.ImageField("Изображение2",
                               upload_to="media_shame",
                               null="True",
                               blank="True")
    photo3 = models.ImageField("Изображение3",
                               upload_to="media_shame",
                               null="True",
                               blank="True")

    def get_absolute_url(self):
        return reverse('village:about_shame',
                       args=[self.publish.year,
                             self.publish.month,
                             self.slug])

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


class Протоколы_Собраний(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            default='')
    document = models.FileField(name='document',
                                default='',
                                upload_to='media',
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
    Адрес = models.CharField(max_length=100, blank=False)
    ФИО = models.CharField(max_length=100, blank=False)

    choices = (
        ('AVAILABLE', 'Item is ready to be purchased'),
        ('SOLD', 'Item Sold'),
        ('RESTOCKING', 'Item restocking in few days')
    )
    Задолженность = models.CharField(max_length=100, default='No issues')

    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type : {0} Price : {1}'.format(self.Адрес, self.ФИО)


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
