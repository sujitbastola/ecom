from django.conf import settings
from django.conf.urls.static import static 
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    # path('l', views.admin_login, name='admin_login'),
    path('', views.admin_home, name='adminhome'),

    # Categories Section 
    path('cadmincategories/', views.admin_categories, name="cadmincategories"),
    path('createcategories/', views.create_category, name="createcategories"),
    path('updatecategories/<str:cat_slug>/', views.update_category, name="updatecategories"),
    path('deletecategories/<str:cat_slug>/', views.delete_category, name="deletecategories"),

    #Product Section
    path('cadminproducts/', views.admin_products, name="cadminproducts"),
    path('createproducts/', views.create_product, name="createproducts"),
    path('updateproducts/<slug:prod_slug>/', views.update_product, name="updateproducts"),
    path('deleteproducts/<slug:prod_slug>/', views.delete_product, name="deleteproducts"),

 


]
if settings.DEBUG:          
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)