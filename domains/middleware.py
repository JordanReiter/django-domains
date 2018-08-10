# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from .utils import set_thread_variable, get_installed_hooks
import warnings

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


class RequestMiddleware(MiddlewareMixin):
    """
    Stores the request object in the local thread
    """
    def process_request(self, request):
        set_thread_variable('request', request)


class DomainSettingsPatchMiddleware(MiddlewareMixin):
    def process_request(self, request):
        for attr, hook in get_installed_hooks().items():
            hook.apply(request)


class DynamicSiteMiddleware(DomainSettingsPatchMiddleware):
    """
    Define current Django Site for requested hostname
    """
    def __init__(self, *args, **kwargs):
        super(DynamicSiteMiddleware, self).__init__(*args, **kwargs)
        warnings.warn(
            "domains.middleware.DynamicSiteMiddleware is deprecated. "
            "Please use domains.middleware.DomainSettingsPatchMiddleware "
            "instead"
        )
