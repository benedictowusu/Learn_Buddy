from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('dashboard/', include('dashboard.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('articles.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]


urlpatterns += staticfiles_urlpatterns()