from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView

from .core import views


urlpatterns = [
    path('', views.home, name='home'),
    path('secret/', views.secret_page, name='secret'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),
    path('secret_staff/', views.secret_page_staff, name='secret-staff'),
    path('secret_super/', views.secret_page_superuser, name='secret-super'),
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(template_name="account/login.html"), name='login'),
    path('accounts/login/', LoginView.as_view(template_name="account/login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('password_change/', PasswordChangeView.as_view(template_name="account/password_change_form.html"), name='password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(template_name="account/password_change_done.html"), name='password_change_done'),
    # path('password_reset/', PasswordResetView.as_view(template_name="account/password_reset_form.html"), name='password_reset'),
]