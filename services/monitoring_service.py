from prometheus_client import Counter

REQUEST_COUNTER = Counter(
    'app_requests_total',
    'Total App Requests'
)


def track_request():
    REQUEST_COUNTER.inc()