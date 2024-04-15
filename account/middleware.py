from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin
from ps_webapp.models import UrlHistory,AccountProfile

class Custom404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404:
            return render(request, '404.html', status=404)
        return response


class URLHistoryMiddleware(MiddlewareMixin):
    def process_request(self, request):
        userid=request.session.get("userid")
        if userid:
            user = AccountProfile.objects.get(userid=userid)
            url_visited = request.path
            if not url_visited.startswith('/restapi'):
                UrlHistory.objects.create(userid=user, url_visited=url_visited)
        return None
    

from django.utils.deprecation import MiddlewareMixin

class SafariCsrfMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # Set the CSRF token cookie's SameSite attribute to 'None' for Safari
        if 'csrftoken' in request.COOKIES and 'Set-Cookie' in response:
            response['Set-Cookie'] = response['Set-Cookie'].replace('; SameSite=Lax', '')
        return response

