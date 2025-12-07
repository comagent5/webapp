from django.contrib.auth.views import LogoutView
from django.urls import include, path
from users import views

app_name = 'users' # для атрібута namespace

urlpatterns = [
    # path('login/', views.login_user, name='login'),
    path('login/', views.LoginUser.as_view(), name='login'),

    # вихід через вбудований класс, та параметр settings.LOGOUT_REDIRECT_URL
    path('logout/', LogoutView.as_view(), name='logout'),

    # вихід через функцію відображення
    # path('logout/', views.logout_user, name='logout'),
]