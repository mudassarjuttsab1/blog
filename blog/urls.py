from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('blog/',views.CreateBlog.as_view(),name='blog'),
    path('listBlog/',views.BlogListing.as_view(),name='blogList')
]
