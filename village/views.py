from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from . import models
from . import forms


def base(request):
    bases = models.Base.objects.all()

    return render(request,
                  'base.html',
                  {'bases': bases, })


def about_base(request, year, day, slug):
    bases = get_object_or_404(models.Base,
                              slug=slug,
                              publish__year=year,
                              publish__day=day,
                              )
    return render(request,
                  'about_base.html',
                  {'bases': bases})


def maps(request):
    mapbox_access_token = 'pk.eyJ1IjoiYmxhY2ttYW1iYTAwN3FlIiwiYSI6ImNrYzR2YTFlcjBicDgyeW51OW9wODQ0OGYifQ.IHGnBzx7Z9d-eayrzSGxtA'
    return render(request,
                  'important/maps.html',
                  {'mapbox_access_token': mapbox_access_token})


def good_job(request):
    return render(request,
                  'good_job.html')


def targeted_contributions(request):
    target = models.Целевые.objects.all()

    return render(request,
                  'important/targeted_contributions.html',
                  {'target': target}, )


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


def for_community(request):
    main = models.ForCommunity.objects.all()
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
                    login(request, user)
                    return good_job(request)
                else:
                    HttpResponse('Inactive user')
            else:
                return HttpResponse('invalid credentials')
    else:
        form = forms.LoginForm()

    return render(request,
                  'for_community.html',
                  {'main_page': main,
                   'form': form}, )


def about_news(request, year, month, day, slug):
    materials = get_object_or_404(models.ForCommunity,
                                  slug=slug,
                                  publish__year=year,
                                  publish__month=month,
                                  publish__day=day,
                                  )
    return render(request,
                  'includes/about_news.html',
                  {'materials': materials})


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


def rule(request):
    rules = models.Rule.objects.all()
    return render(request,
                  'main_documentation/rule.html',
                  {'rules': rules}, )


def leadership(request):
    leader = models.Leadership.objects.all()
    query = request.GET.get("query", '')
    if query:
        leader = leader.filter(title__icontains=query)
    else:
        leader = leader
    return render(request,
                  'important/leadership.html',
                  {'leaders': leader}, )


def debtors(request):
    debtors = models.Debtors.objects.all()
    return render(request,
                  'important/debtors.html',
                  {'debtors': debtors})


def codex_about_land(request):
    return render(request,
                  'main_documentation/codex_about_land.html')


def rule_inside(request):
    rules = models.RuleInside.objects.all()
    return render(request,
                  'main_documentation/rule_inside.html',
                  {'rules': rules}, )


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
