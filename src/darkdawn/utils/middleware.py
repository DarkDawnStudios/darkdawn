from django.shortcuts import redirect
from django.templatetags.static import static


class URLMapMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.map = {
            "/favicon.ico": static("assets/img/favicon.ico"),
        }

    def __call__(self, request):
        url = self.map.get(request.path)
        if url is not None:
            return redirect(url)
        response = self.get_response(request)
        return response
