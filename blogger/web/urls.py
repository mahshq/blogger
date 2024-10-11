
from django.urls import path
from web import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name="logout"),

    path('create/', views.create, name="create"),
    path('blog/<int:id>/', views.blog, name="blog"),

    path('blog/delete/<int:id>/', views.blog_delete, name="blog_delete"),

    path('account/', views.account, name="account"),

]
