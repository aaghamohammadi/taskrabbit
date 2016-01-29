from django.core.urlresolvers import resolve
from django.http.response import HttpResponseForbidden
from django.core.cache import cache


class OnlineNowMiddleware(object):
    @staticmethod
    def process_request(request):

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            user_ip = x_forwarded_for.split(',')[0]
        else:
            user_ip = request.META.get('REMOTE_ADDR')

        online = cache.get('online_now')

        if online:
            online = [ip for ip in online if cache.get(ip)]
        else:
            online = []

        cache.set(user_ip, user_ip, 600)

        if user_ip not in online:
            online.append(user_ip)

        cache.set('online_now', online)

        request.__class__.online_now = len(online)


class CommonMiddleWare:
    @staticmethod
    def process_view(request, view_func, view_args, view_kwargs):
        cls = Root
        # todo age chizi base hame bayad anjam beshe inja bayad ejra she vali baide
        resolved = resolve(request.path)
        names = resolved.namespaces + [resolved.url_name]
        for name in names:
            camel = ''.join(x.capitalize() for x in name.split('_'))
            if hasattr(cls, camel):
                cls = getattr(cls, camel)
            else:
                break
            if hasattr(cls, "process_view"):
                result = getattr(cls, 'process_view')(request, view_func, view_args, view_kwargs)
                if result:
                    return result


class Root:
    class Service:
        @staticmethod
        def process_view(request, view_func, view_args, view_kwargs):
            if not request.user.is_authenticated():
                return HttpResponseForbidden()

        class EditSkill:
            @staticmethod
            def process_view(request, view_func, view_args, view_kwargs):
                pass  # hafeze zaife yadam mire :))
