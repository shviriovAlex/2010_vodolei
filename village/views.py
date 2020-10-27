from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from . import models
from . import forms

""" main page """


def hunger(request):
    return render(request,
                  'hunger/hunger.html')


def codex_about_land(request):
    return render(request,
                  'juridical_inf/codex_about_land.html')


def rule_inside(request):
    return render(request,
                  'juridical_inf/rule_inside.html')


def rule(request):
    return render(request,
                  'juridical_inf/rule.html')


def order_of_the_president(request):
    return render(request,
                  'juridical_inf/order_of_the_president.html')


def for_community(request):
    main = models.Главная.objects.all()
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['Логин'],
                password=cd['Пароль'],
            )
            if user is not None:
                if user.is_active:
                    hello = 'Добро пожаловать на Водолей 2010!'
                    login(request, user)
                    return render(request,
                                  'for_community.html',
                                  {'main_page': main,
                                   'form': form,
                                   'hello': hello}, )
                else:
                    HttpResponse('Inactive user')
            else:
                error = 'Неверный логин или пароль!'
                return render(request,
                              'for_community.html',
                              {'main_page': main,
                               'form': form,
                               'error': error}, )
    else:
        form = forms.LoginForm()

    return render(request,
                  'for_community.html',
                  {'main_page': main,
                   'form': form}, )


def about_news(request, year, month, day, slug):
    materials = get_object_or_404(models.Главная,
                                  slug=slug,
                                  publish__year=year,
                                  publish__month=month,
                                  publish__day=day,
                                  )
    return render(request,
                  'includes/about_news.html',
                  {'materials': materials})


""" Debtors"""


def targeted_contributions(request):
    target = models.Целевые.objects.all()

    return render(request,
                  'important/targeted_contributions.html',
                  {'targets': target}, )


def membership_fee(request):
    target = models.Членские.objects.all()

    return render(request,
                  'important/membership_fee.html',
                  {'targets': target}, )


def electricity(request):
    target = models.Электроэнергия.objects.all()

    return render(request,
                  'important/electricity.html',
                  {'targets': target}, )


""" payments """


def how_to_pay(request):
    return render(request,
                  'payments/how_to_pay.html', )


def members(request):
    return render(request,
                  'payments/members.html')


def target(request):
    return render(request,
                  'payments/target.html')


""" electricity and gas price"""


def elect_and_gas_price(request):
    elect_gas_prices = models.Тарифы_Электр_Газ.objects.all()
    return render(request,
                  'elect_and_gas_price/elect_and_gas_price.html',
                  {'elect_gas_prices': elect_gas_prices}, )


def maps(request):
    mapbox_access_token = 'pk.eyJ1IjoiYmxhY2ttYW1iYTAwN3FlIiwiYSI6ImNrYzR2YTFlcjBicDgyeW51OW9wODQ0OGYifQ.IHGnBzx7Z9d-eayrzSGxtA'
    return render(request,
                  'maps/maps.html',
                  {'mapbox_access_token': mapbox_access_token})


""" How to connect """


def electricity_connect(request):
    return render(request,
                  'how_to_connect/electricity_connect.html')


def gas_connect(request):
    return render(request,
                  'how_to_connect/gas_connect.html')


def water_connect(request):
    return render(request,
                  'how_to_connect/water_connect.html')


def refresher(request):
    return render(request,
                  'how_to_connect/refresher.html')


def good_job(request):
    return render(request,
                  'good_job.html')


def shames(request):
    shames = models.ДоскаПозора.objects.all()
    return render(request,
                  'includes/shames.html',
                  {'shames': shames}, )


def about_shame(request, slug, year, month):
    shame = get_object_or_404(models.ДоскаПозора,
                              slug=slug,
                              publish__year=year,
                              publish__month=month,
                              )
    return render(request,
                  'includes/about_shame.html',
                  {'shame': shame})


def registration(request):
    if request.method == 'POST':
        first_name = request.POST['name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2 and len(password1) != 0:
            if User.objects.filter(username=username).exists():
                print('Username taken')
            elif User.objects.filter(email=email).exists():
                print('Email taken')
            else:
                user = User.objects.create_user(username=username,
                                                password=password1,
                                                first_name=first_name,
                                                email=email, )
                new_user = user.save()
                print('user created')
                return render(request,
                              'register_done.html',
                              {'new_user': new_user})

        else:
            print('password not matching')
        return redirect('/registration/')
    else:
        return render(request,
                      'registration.html')


def user_logout(request):
    return render(request,
                  'logout.html')


def administration(request):
    leader = models.АдминистрацияСТ.objects.all()
    return render(request,
                  'governance/administration.html',
                  {'leaders': leader}, )


def government(request):
    leader = models.Правление.objects.all()
    return render(request,
                  'governance/government.html',
                  {'leaders': leader}, )


def in_commission(request):
    leader = models.Уполномоченные.objects.all()
    return render(request,
                  'governance/in_commission.html',
                  {'leaders': leader}, )


def revision(request):
    leader = models.РевизионнаяКомиссия.objects.all()
    return render(request,
                  'governance/revision.html',
                  {'leaders': leader}, )


#
#
def counting_commission(request):
    leader = models.СчетнаяКомиссия.objects.all()
    return render(request,
                  'governance/counting_commission.html',
                  {'leaders': leader}, )


def all_photo(request):
    photos = models.AllPhoto.objects.all()
    return render(request,
                  'all_photo.html',
                  {'photos': photos}, )


def photo(request):
    images = models.Photo.objects.all()
    return render(request,
                  'photo.html',
                  {'images': images}, )


def entry_in_community(request):
    return render(request,
                  'of_and_reg/entry_in_community.html', )


def reg_ownership(request):
    return render(request,
                  'of_and_reg/reg_ownership.html', )


def application_to_the_board(request):
    return render(request,
                  'of_and_reg/application_to_the_board.html', )


def reg_house(request):
    return render(request,
                  'of_and_reg/reg_house.html', )


def statement_to_the_rec(request):
    return render(request,
                  'of_and_reg/statement_to_the_rec.html', )


def protocols(request):
    protocols = models.Протоколы_Собраний.objects.all()
    return render(request,
                  'protocols.html',
                  {'protocols': protocols})
