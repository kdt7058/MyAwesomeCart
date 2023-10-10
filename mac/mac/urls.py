from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.index, name="shop name"),
                  path('shop/', include('shop.urls'), name="shop name"),
                  path('blog/', include('blog.urls'), name="blog name"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
