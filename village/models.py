from django.db import models
from django.urls import reverse
from django.utils import timezone


class Главная(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            default='')
    body = models.TextField()
    image = models.ImageField("Изображение",
                              upload_to="media_community/",
                              null="True",
                              blank="True")
    image2 = models.ImageField("Изображение",
                               upload_to="media_community/",
                               null="True",
                               blank="True")
    image3 = models.ImageField("Изображение",
                               upload_to="media_community/",
                               null="True",
                               blank="True")
    image4 = models.ImageField("Изображение",
                               upload_to="media_community/",
                               null="True",
                               blank="True")
    image5 = models.ImageField("Изображение",
                               upload_to="media_community/",
                               null="True",
                               blank="True")
    document = models.FileField("Файл",
                                upload_to="media_community/",
                                null="True",
                                blank="True", )
    document_2 = models.FileField("Файл",
                                  upload_to="media_community/",
                                  null="True",
                                  blank="True", )
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


class Тарифы_Электр_Газ(models.Model):
    дата_от = models.CharField(max_length=250)
    электроэнергия = models.CharField(max_length=250)
    газ = models.CharField(max_length=250)
    прежний_электроэнергия = models.CharField(max_length=250)
    прежний_газ = models.CharField(max_length=250)


class Протоколы_Собраний(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            default='')
    document = models.FileField(name='document',
                                default='',
                                upload_to='media',
                                null='True',
                                blank='True')
    publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Governance(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            default='')
    Должность = models.TextField(max_length=250)
    ФИО = models.TextField(max_length=250)
    Номер_телефона = models.TextField(max_length=250)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class АдминистрацияСТ(Governance):
    pass


class Правление(Governance):
    pass


class Уполномоченные(Governance):
    pass


class РевизионнаяКомиссия(Governance):
    pass


class СчетнаяКомиссия(Governance):
    pass


class Debtors(models.Model):
    Адрес = models.CharField(max_length=100, blank=False)
    ФИО = models.CharField(max_length=100, blank=False)

    choices = (
        ('AVAILABLE', 'Item is ready to be purchased'),
        ('SOLD', 'Item Sold'),
        ('RESTOCKING', 'Item restocking in few days')
    )
    Задолженность = models.CharField(max_length=100, default='No issues')

    опубликовано = models.DateTimeField(default=timezone.now)

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
