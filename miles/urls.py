from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = 'miles'
urlpatterns = [
    path('', views.index, name='index'),
    path('(?P<album_id>[0-9]+)/', views.details, name="details"),
    path('add_album', views.add_album, name="add_album"),
    path('(?P<album_id>[0-9]+)/add-song', views.add_song, name='add-song'),
    path('(?P<album_id>[0-9]+)/delete-album', views.delete_album, name='delete-album'),
    path('signup', views.signup, name='signup'),
    #path('login', auth_views.LoginView.as_view(), name='login'),
    #path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)