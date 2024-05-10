from django.urls import path
from authentication import views
from django.contrib.auth.views import LoginView

urlpatterns = [
path('', LoginView.as_view(
           template_name='authentication/login.html',
           redirect_authenticated_user=True),
        name='login'),
 path('logout/', views.LogoutView.as_view(), name='logout'),
 path('signup/', views.SignUpView.as_view(), name='signup'),

]