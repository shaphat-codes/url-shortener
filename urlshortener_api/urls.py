
from django.contrib import admin
from django.urls import path
from shortener import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('post-link', views.PostLink, name="post-link"),
    path('<str:encoded>/', views.redirect_view, name="redirect"),
]
