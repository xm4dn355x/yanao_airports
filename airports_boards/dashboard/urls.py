from django.urls import path

from . import views

urlpatterns = [
    #/dashboard/        index page of dashboard
    path('', views.index, name='index'),
    # #/dashboard/sly/    dashboard for SLY airport
    # path('sly/', views.show_sly, name="show_sly"),
    # # /dashboard/noj/   dashboard for NOJ airport
    # path('noj/', views.show_noj, name="show_noj"),
    # # /dashboard/nux/   dashboard for NUX airport
    # path('nux/', views.show_nux, name="show_nux"),
    # # /dashboard/nym/   dashboard for NYM airport
    # path('nym/', views.show_nym, name="show_nym"),
    # # /dashboard/sbt/   dashboard for SBT airport
    # path('sbt/', views.show_sbt, name="show_sbt"),
]