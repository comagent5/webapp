from django.urls import include, path
from users import views

app_name = 'users' # для атрібута namespace

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]