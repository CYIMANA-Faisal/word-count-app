
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index_page'),
    path('count/', views.count, name='count_page'),
    path('about/', views.about, name='aboutus_page'),
]
