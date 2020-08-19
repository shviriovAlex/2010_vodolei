from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as au_views

app_name = 'village'
urlpatterns = [
    path('login/', au_views.LoginView.as_view(), name='login'),
    path('<int:year>/<int:day>/<slug:slug>/', views.about_base, name='about_base'),
    path('', views.for_community, name='for_community'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.about_news,
         name='about_news'),

    path('registration', views.registration, name='registration'),
    path('logout/', au_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('good_job/', views.good_job, name='good_job'),
    path('password-reset/',
         au_views.PasswordResetView.as_view(success_url=reverse_lazy('village:password_reset_confirm')),
         name='password_reset'),
    path('password-reset/done/', au_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', au_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-change/',
         au_views.PasswordChangeView.as_view(success_url=reverse_lazy('village:password_change_done')),
         name='password_change'),
    path('password-change/done/', au_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('reset/done/', au_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('rule/', views.rule, name='rule'),
    path('leadership/', views.leadership, name='leadership'),
    path('maps/', views.maps, name='maps'),
    path('debtors/', views.debtors, name='debtors'),
    path('codex_about_land/', views.codex_about_land, name='codex_about_land'),
    path('rule_inside/', views.rule_inside, name='rule_inside'),
    path('targeted_contributions', views.targeted_contributions, name='targeted_contributions'),
    path('membership_fee', views.membership_fee, name='membership_fee'),
    path('electricity', views.electricity, name='electricity'),
    path('photo', views.photo, name='photo'),

]
