
from django.urls.conf import path
from . import views

app_name="App_Blog"

urlpatterns = [
    path('',views.BlogList.as_view(),name="bloglist"),
    
    path('write/',views.CreateBlog.as_view(),name="CreateBlog"),
    path('blog_details/?P<slug>[-a-zA-Z0-9_]+)$>',views.BlogDetails,name="blog_details"),
    path('my-Blog/',views.myblog.as_view(),name="myblog"),
    path('Edit/<pk>/',views.UpdateBlog.as_view(),name="edit_blog"),
]
