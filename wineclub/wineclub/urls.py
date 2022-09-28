"""wineclub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
    path('admin-site/', admin.site.urls),
    # Accounts
    path('', include('accounts.guest.urls')),
    path('customer/accounts/', include('accounts.customer.urls')),
    # Manage Accounts
    path('administrator/', include('accounts.administrator.urls')),
    # Categories
    path('categories/', include('categories.guest.urls')),
    path('admin/categories/', include('categories.administrator.urls')),
    #Subscription Packages
    path('admin/subscription-package/', include('subscriptions.administrator.urls')),
    path('subscription-package/', include('subscriptions.guest.urls')),
    path('business/subscription-package/', include('subscriptions.business.urls')),
    
    # winery
    path('', include('wineries.guest.urls')),
    path('business/wineries/', include('wineries.business.urls')),
    # winery
    
    # Coupon
    path('admin/coupons/', include('coupons.administrator.urls')),
    path('business/coupons/', include('coupons.business.urls')),
    # path('', include('wineries.guest.urls')),
    # path('', include('wineries.guest.urls')),
    # Coupon
    # cart
    path('customer/carts/', include('carts.customer.urls')),
    # cart
    
    # path('customer/addresses/', include('addresses.customer.urls')),

    #Addresses
    path('customer/addresses/', include('addresses.customer.urls')),

    #Wine
    path('wines/', include('wines.guest.urls')),
    path('business/wines/', include('wines.business.urls')),
    path('admin/wines/', include('wines.administrator.urls')),
    
    #Shipping Unit
    path('administrator/shipping/', include('shipping.administrator.urls')),
    path('shippings/', include('shipping.guest.urls')),
    path('wineries/shippings/', include('shipping.business.urls')),

    #notification and add device FCM
    path('customer/notifications/', include('notifications.customer.urls')),
    
    #Payments
    path('customer/payments/', include('payments.customer.urls')),

    #Webhook Stripe
    path('webhook/', include('payments.urls')),

    #transaction
    path('admin/transactions/', include('transactions.administrator.urls')),

    #business connect account
    path('business/connect-account/', include('accounts.business.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

