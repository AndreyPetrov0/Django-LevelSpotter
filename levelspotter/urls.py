"""
URL configuration for levelspotter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from spotter.views import index, page_not_found
from download_page.views import page_download
from instructions.views import instructions
from start_page.views import page_start


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', page_start, name='start_page'),
    path('/spotter', include("spotter.urls"), name='spotter'),
    path('/download', page_download, name='download'),
    path('/instructions', instructions, name='instructions'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = page_not_found