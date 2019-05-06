
from django.urls import path
from . import views
from .views import Blog_detail, All_blogs

urlpatterns = [

    
    path("", All_blogs.as_view(), name="allblogs"),
    path("<int:pk>/", Blog_detail.as_view(), name="detail"),
    
]
