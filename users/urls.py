from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import include, path
from users import views

app_name = 'users' # для атрібута namespace

urlpatterns = [
    # path('login/', views.login_user, name='login'),
    path('login/', views.LoginUser.as_view(), name='login'),

    # вихід через вбудований класс, та параметр settings.LOGOUT_REDIRECT_URL
    # path('logout/', LogoutView.as_view(), name='logout'),

    # вихід через функцію відображення
    path('logout/', views.logout_user, name='logout'),

    # реєстрація через клас відображення
    path('register/', views.RegisterUser.as_view(), name='register'),

    # реєстрація через функцію відображення
    # path('register/', views.register, name='register'),

    path('profile/', views.ProfileUser.as_view(), name='profile'),

    path('password-change', views.UserPasswordChange.as_view(), name='password-change'), # форма з Django PasswordChangeView.as_view()
    
    path('password-change/done/', 
         PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), 
         name='password-change-done'),
]