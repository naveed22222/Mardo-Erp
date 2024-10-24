"""MardoSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Mardo-ERP/', include('AppAccount.urls')),
    path('Mardo-ERP/', include('AppAdmin.urls')),
    path('Mardo-ERP/HRM/', include('AppEmployee.urls')),
    path('Mardo-ERP/Purchase/', include('AppPurchase.urls')),
    path('Mardo-ERP/Supplier/', include('AppSupplier.urls')),
    path('Mardo-ERP/ChartAccount', include('AppChartAccount.urls')),
    path('Mardo-ERP/AppProduct', include('AppProduct.urls')),
    path('Mardo-ERP/Expense', include('AppExpenditure.urls')),
    path('Mardo-ERP/Inventory', include('AppInventory.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

