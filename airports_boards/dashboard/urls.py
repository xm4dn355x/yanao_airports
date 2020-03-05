from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sly/', views.show_sly, name="show_sly"),
    path('noj/', views.show_noj, name="show_noj"),
    path('nux/', views.show_nux, name="show_nux"),
    path('nym/', views.show_nym, name="show_nym"),
    path('sbt/', views.show_sbt, name="show_sbt"),
]