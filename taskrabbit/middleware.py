from django.core.urlresolvers import resolve
from django.http.response import HttpResponseForbidden


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
