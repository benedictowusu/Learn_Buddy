from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('accounts/', include('accounts.urls')),
    path('articles/', include('articles.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]


urlpatterns += staticfiles_urlpatterns()