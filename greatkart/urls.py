
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from greatkart.settings import MEDIA_ROOT
from .import views
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('store/',include('store.urls')),
    path('cart/', include('carts.urls')),
    path ('accounts/', include('accounts.urls')),
] + static (settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
