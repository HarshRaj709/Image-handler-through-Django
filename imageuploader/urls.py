from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('del/<int:id>/',views.delete1,name='del'),   
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  #isko add kiya h media file dekhne ke

# print(static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT))
