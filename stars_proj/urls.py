"""stars_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from ratings.views import main_view, rate_image, MainView, file_upload_view, file_delete_view

urlpatterns = [
    path('faq', include('faq.urls')),
    path('admin/', admin.site.urls),

    # path('', main_view, name="main-view"),
    path('', MainView.as_view(), name="upload-image"),
    path('rate/', rate_image, name='rate-view'),
    path('upload/', file_upload_view, name='upload-view'),
    path('file-delete/', file_delete_view, name='file-delete-view'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)