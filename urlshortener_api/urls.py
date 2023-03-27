
from django.contrib import admin
from django.urls import path
from shortener import views
from django.views.generic import TemplateView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),

    path('post-link', views.PostLink, name="post-link"),
    path('<str:encoded>/', views.redirect_view, name="redirect"),
]
