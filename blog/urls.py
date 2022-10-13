from django.urls import path

from . import views as blog_views

urlpatterns = [

    #blogs urls
    path('list_views_blog/',blog_views.ListViewsBlog.as_view(),name='list_blogs'),
    path('create_view_blog/' , blog_views.CreateViewBlog.as_view() , name='create_blog'),
    path('<int:pk>/update_blog/', blog_views.UpdateViewBlog.as_view() , name='update_blog'),
    path('<int:pk>/delete_blog/',blog_views.DeleteViewsBlog.as_view() , name='delete_blog'),

    #comments urls
    path('list_views_comment/',blog_views.ListCommentViews.as_view() ,name ='list_comments'),
    path('create_comment/',blog_views.CreateComment.as_view(),name='create_comment'),
    path('<int:pk>/update_comment/',blog_views.UpdateCommentViews.as_view(),name='update_comment'),
    path('<int:pk>/delete_comment/',blog_views.DeleteCommentViews.as_view() ,name='delete_comment'),
]