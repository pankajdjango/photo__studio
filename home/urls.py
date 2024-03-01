from django.urls import path
from .import views
urlpatterns = [
    path('',views.index , name='home'),
]

# Import the custom_404 view function
from .views import custom_404

# Set the custom 404 handler
handler404 = 'home.views.custom_404'
