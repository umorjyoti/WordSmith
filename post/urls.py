from django.urls import path
from . import views

urlpatterns = [
    path('create',views.create,name="create"),
    path('<int:post_id>',views.detail,name="detail"),
    path('<int:post_id>/upvote',views.upvote,name="upvote"),
]
