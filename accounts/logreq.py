from django.http import HttpResponseRedirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))  # يعيد توجيه المستخدم إلى صفحة تسجيل الدخول إذا لم يكن مسجلاً الدخول
        response = self.get_response(request)
        return response
