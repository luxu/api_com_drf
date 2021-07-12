from django.contrib import admin
from django.urls import include, path

import secretaria

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(secretaria.urls)),
]
