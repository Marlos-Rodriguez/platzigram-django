"""User Views"""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse

# Models
from django.contrib.auth.models import User
from posts.models import Post

# Forms
from users.forms import ProfileForm, SignupForm


class UserDetailView(LoginRequiredMixin, TemplateView):
    """User Detail view"""
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        print(self.kwargs['username'])
        user = get_object_or_404(User, username=self.kwargs['username'])
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


class LoginView(auth_views.Loginview):
    """Login View"""

    template_name = 'users/login.html'
    redirect_authenticated_user = True

# def login_view(request):
#     """Login View"""
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('posts:feed')
#         else:
#             return render(request, 'users/login.html', {'error': 'Invalid username or password'})
#     return render(request, 'users/login.html')


def singup_view(request):
    """Sign Up view"""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()
    print(form)
    return render(request=request, template_name='users/signup.html', context={'form': form})


@login_required
def logout_view(request):
    """LogOut User"""
    logout(request)
    return redirect('users:login')


@login_required
def update_profile(request):
    """Update User Profile"""
    # Get Profile
    profile = request.user.profile

    if request.method == 'POST':
        # Create Form
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # Get data from form
            data = form.cleaned_data

            # Asign Profile info
            profile.website = data['website']
            profile.biography = data['biography']
            profile.phone_number = data['phone_number']
            profile.picture = data['picture']

            # Save profile changes
            profile.save()

            url = reverse('users:detail', kwargs={
                          'username': request.user.username})
            return redirect(url)

    else:
        form = ProfileForm()

    context = {'profile': profile, 'user': request.user, 'form': form}
    return render(request, 'users/update_profile.html', context=context)
