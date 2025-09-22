"""
URL configuration for blog_project project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),           # ホーム、About、Resume
    path('projects/', include('projects.urls')),  # プロジェクト
    path('blog/', include('blog.urls')),      # ブログ記事
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
