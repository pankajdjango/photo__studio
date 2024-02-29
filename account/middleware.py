# In your_app/middleware.py

from datetime import datetime
from django.utils.deprecation import MiddlewareMixin
from .models import Log  # Import your Log model

class LogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Log the request details
        Log.objects.create(
            url=request.path,
            method=request.method,
            user=request.user if request.user.is_authenticated else None,
            timestamp=datetime.now()
        )
        return None
