from django.urls import path
from .import views
# from .views import 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[

    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.userPage,name='user-page'),
    path('user/',views.logoutUser,name='logout'),
    path('profile/', views.profile, name='profile'),
    path('',views.home, name="home"),
    path('new/', views.create_post, name='post'),
    path('<int:pk>/photo/',views.viewPhoto, name ='photo'),

   

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    