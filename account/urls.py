from django.urls import path
from . import views

urlpatterns = [
    # path('login/', views.login, name='login'),
    path('login.html/', views.signup_login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', views.home, name='home'),
    # path('photographer/<int:photographer_id>/', views.photographer_profile, name='photographer_profile'),
    # path('client/<int:client_id>/', views.client_profile, name='client_profile'),
    # path('event/<int:event_id>/', views.event_details, name='event_details'),
    # path('event/<int:event_id>/book/', views.book_event, name='book_event'),
    # path('booking/<int:booking_id>/payment/', views.make_payment, name='make_payment'),
    # path('booking/<int:booking_id>/confirmation/', views.booking_confirmation, name='booking_confirmation'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    # path('booking/<int:booking_id>/cancel/', views.cancel_booking, name='cancel_booking'),
    # path('events/search/', views.search_events, name='search_events'),
    # path('events/filter/', views.filter_events, name='filter_events'),
    # path('booking/history/', views.booking_history, name='booking_history'),
    # # Add more URLs as needed
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    # path('faq/', views.faq, name='faq'),
    # path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    # path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),
]
