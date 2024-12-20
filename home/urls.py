from django.urls import path
from .import views


urlpatterns = [
    path('',views.index , name='home'),
    path('booknow/',views.booknow , name='booknow'),
    path('about/',views.about , name='about'),
    path('photoshoot/',views.photoshoot , name='photoshoot'),
    path('gallery/',views.gallery , name='gallery'),
    path('booking_stats/',views.booking_stats , name='booking_stats'),
    path('update_booking_request/<int:id>/', views.update_booking_request , name='update_booking_request'),
    path('biodata/', views.biodata, name='biodata'),
    path('amt/', views.amt, name='amt'),
]
