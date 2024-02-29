from django.urls import path
# from django.conf.urls import url,include
from . import views
urlpatterns = [
    path(r'country_state_city_list/', views.country_state_city_list, name='country_state_city_list'),
]
