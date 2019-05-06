from django.urls import path
#from .views import All_coffeeshops, Coffeshop_detail
from .views import Coffeshop_create, All_coffeeshops, Coffeshop_detail, Coffeshop_update, Coffeshop_delete, All_user_coffeeshops, upvote


urlpatterns = [
    #path("", all_coffeeshops, name="coffeeshops"),
    path("", All_coffeeshops.as_view(), name="coffeeshops"),
    path("user/<str:user>", All_user_coffeeshops.as_view(),
         name="all_user_coffeeshops"),
    path("<int:pk>/", Coffeshop_detail.as_view(), name="coffeshop_detail"),
    path("post/new/", Coffeshop_create.as_view(), name="post_create"),
    path("<int:pk>/update", Coffeshop_update.as_view(), name="coffeshop_update"),
    path("<int:pk>/delete", Coffeshop_delete.as_view(), name="coffeshop_delete"),
    path("<int:pk>/<username>/upvote", upvote, name="upvote")
]
