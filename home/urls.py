from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    # nav components
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('offers', views.offers, name="offers"),
    path('special', views.special, name="special"),
    path('order', views.order, name="order"),

    # Product detail components
    path('detail', views.detail, name="detail"),
    path('cetegories_detail/<slug:cat_slug>/', views.cetegories_detail, name="cetegories_detail"),

    #login views
    path('register/', views.Signup, name="register"),
    path('login/', views.Login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('authentication/<slug:token>/',views.account_verify, name="account_verify"),

    #actions 
    path('addtolist/', views.addtolist, name="addtolist"),
    path('buynow/', views.buynow, name="buynow"),

    # costum order 
    path('upload/', views.upload_image, name='upload_image'),




]
if settings.DEBUG:          
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)