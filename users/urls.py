from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import include, path, reverse_lazy
from users import views

app_name = 'users' # для атрібута namespace

urlpatterns = [
    # path('login/', views.login_user, name='login'),
    path('login/', views.LoginUser.as_view(), name='login'),

    # вихід через вбудований класс, та параметр settings.LOGOUT_REDIRECT_URL
    path('logout/', LogoutView.as_view(), name='logout'),

    # вихід через функцію відображення
    # path('logout/', views.logout_user, name='logout'),

    # реєстрація через клас відображення
    path('register/', views.RegisterUserView.as_view(), name='register'),

    # реєстрація через функцію відображення
    # path('register/', views.register, name='register'),

    path('profile/', views.ProfileUser.as_view(), name='profile'),

    path('password-change', views.UserPasswordChange.as_view(), name='password-change'),
    
    path('password-change/done/', 
         PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), 
         name='password-change-done'),

    path('password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset/complete/', views.UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

'''
path('password-reset/',
     PasswordResetView.as_view(
         template_name='users/password_reset_form.html',
         email_template_name='users/password_reset_email.html',
         success_url=reverse_lazy('users:password_reset_done')),
     name='password_reset'),
path('password-reset/done/',
     PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
     name='password_reset_done'),
path('password-reset/<uidb64>/<token>/',
     PasswordResetConfirmView.as_view(
         template_name='users/password_reset_confirm.html',
         success_url=reverse_lazy('users:password_reset_complete')),
     name='password_reset_confirm'),
path('password-reset/complete/',
     PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
     name='password_reset_complete'),
'''