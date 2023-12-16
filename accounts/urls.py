from django.contrib.auth.views import LogoutView
from django.urls import path
from accounts.views import user_profile, user_register, user_login, user_update, user_update_avatar

urlpatterns = [
    path('signup/', user_register),
    path('login/', user_login),
    path('logout/', LogoutView.as_view(template_name="accounts/logout.html")),
    path('update/', user_update),
    path('avatar/', user_update_avatar),
    path('profile/', user_profile)
    ]