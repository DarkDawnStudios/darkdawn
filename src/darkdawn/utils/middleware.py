from django.conf import settings
from django.shortcuts import redirect
from django.templatetags.static import static


class URLMapMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        url = settings.URL_MAPPING.get(request.path)
        if url is not None:
            target = url.value
            if url.is_static:
                target = static(target)
            return redirect(target)
        response = self.get_response(request)
        return response
