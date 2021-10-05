from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.urls import reverse


class ProfileCompletionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_anonymous:
            try:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('update_profile'), reverse('logout')]:
                        return redirect('update_profile')
            except:
                print('no profile')
                logout(request)
                return render(request, 'users/login.html', {'error': 'User has no profile'})

        response = self.get_response(request)
        return response
