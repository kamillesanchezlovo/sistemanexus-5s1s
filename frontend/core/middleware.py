import time
import json
from typing import Any
from django.utils.deprecation import MiddlewareMixin

REDACT_KEYS = {"authorization", "token", "password"}

def _redact(obj: Any):
    try:
        if isinstance(obj, dict):
            return {k: ("***" if k.lower() in REDACT_KEYS else _redact(v)) for k, v in obj.items()}
        if isinstance(obj, list):
            return [_redact(x) for x in obj]
    except Exception:
        pass
    return obj

class RequestLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request._start_time = time.time()
        if request.method in {"POST", "PUT", "PATCH"}:
            try:
                body_bytes = request.body or b""
                if body_bytes:
                    request._logged_json = _redact(json.loads(body_bytes.decode("utf-8")))
                else:
                    request._logged_json = None
            except Exception:
                request._logged_json = None

    def process_response(self, request, response):
        try:
            dur_ms = (time.time() - getattr(request, "_start_time", time.time())) * 1000
            path = getattr(request, "path", "?")
            method = getattr(request, "method", "?")
            status = getattr(response, "status_code", 0)
            if hasattr(request, "_logged_json") and request._logged_json is not None:
                print(f"[API IN ] {method} {path} body={request._logged_json}")
            print(f"[API OUT] {method} {path} -> {status} in {dur_ms:.1f} ms")
        except Exception:
            pass
        return response
