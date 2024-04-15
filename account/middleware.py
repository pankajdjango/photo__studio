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
            # url_visited = request.path
            full_url = request.build_absolute_uri()
            if '/restapi' not in full_url or '/admin' not in full_url:
                UrlHistory.objects.create(userid=user, url_visited=full_url)
        return None
