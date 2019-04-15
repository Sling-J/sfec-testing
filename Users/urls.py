from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
   path('sign-in/', LoginView.as_view(template_name='Users/sign_in.html'), name='sign_in_url'),
   path('sign-out/', LogoutView.as_view(template_name='Users/sign_out.html'), name='sign_out_url'),
]