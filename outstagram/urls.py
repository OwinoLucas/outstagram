from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$',views.index,name = 'index'), 
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^profile/', views.profile, name= 'profile'),
    url(r'^comment/<int:post_id>/', views.post_comment, name= 'post_comment'),
    url(r'^upload_post/', views.upload_post, name='upload'),
    url(r'unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
    url(r'follow/<to_follow>', views.follow, name='follow')
    # url(r'^user_profile/<username>/', views.user_profile, name= 'user_profile')
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)