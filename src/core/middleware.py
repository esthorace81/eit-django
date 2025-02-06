from contextvars import ContextVar

from django.utils.deprecation import MiddlewareMixin

request_context = ContextVar('request')


class RequestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request_context.set(request)

    def process_response(self, request, response):
        request_context.set(None)
        return response
