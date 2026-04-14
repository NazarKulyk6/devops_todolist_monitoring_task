from django.http import HttpResponse
from prometheus_client import CONTENT_TYPE_LATEST, Counter, generate_latest

HTTP_REQUESTS_TOTAL = Counter(
    "todoapp_http_requests_total",
    "Total number of HTTP requests split by method.",
    ["method"],
)


def track_http_request(method):
    if method in ("GET", "POST"):
        HTTP_REQUESTS_TOTAL.labels(method=method).inc()


def metrics_view(_request):
    return HttpResponse(generate_latest(), content_type=CONTENT_TYPE_LATEST)
