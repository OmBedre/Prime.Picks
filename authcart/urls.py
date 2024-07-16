from django.urls import path
from authcart import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),  # URL for user signup
    path('login/', views.handlelogin, name='handlelogin'),  # URL for user login
    path('logout/', views.handlelogout, name='handlelogout'),  # URL for user logout
    path('activate/<uidb64>/<token>/', views.ActivateAccountView.as_view(), name='activate'),  # URL for activating user account with UID and token
    path('request-reset-email/', views.RequestResetEmailView.as_view(), name='request-reset-email'),  # URL for requesting a password reset email
    path('set-new-password/<uidb64>/<token>/', views.SetNewPasswordView.as_view(), name='set-new-password'),  # URL for setting a new password with UID and token
]
