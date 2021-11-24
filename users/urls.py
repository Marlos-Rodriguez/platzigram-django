"""User URLs"""

# Django
from django.urls import path

from users import views

urlpatterns = [
    path(
        'login/',
        views.LoginView.as_view(),
        name='login'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

    path(
        'signup/',
        views.singup_view,
        name='signup'
    ),

    path(
        'me/profile/',
        views.update_profile,
        name='update_profile'
    ),

    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
]
