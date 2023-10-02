"""
URL configuration for config project.

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
from django.urls import include
from django.urls import path

from products import views as products_views
from storefront import views as storefront_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", storefront_views.storefront, name="storefront"),
    path("", include("django.contrib.auth.urls")),
    path("products/", products_views.product_list, name="product-list"),
    path("products/new/", products_views.product_create, name="product-create"),
    path(
        "products/<int:pk>/update/",
        products_views.product_update,
        name="product-update",
    ),
    path(
        "products/<int:pk>/delete/",
        products_views.product_delete,
        name="product-delete",
    ),
    path("health/", include("health_check.urls")),
]
