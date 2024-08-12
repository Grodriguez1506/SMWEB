"""
URL configuration for ScrumManagerWEB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path
from SMWEB import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio/', views.inicio, name='inicio'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('new-user/', views.new_user, name='new-user'),
    path('new-company-user/', views.new_company_user, name='new-company-user'),
    path('users/', views.users_availables, name='users'),
    path('users-company/', views.users_company, name='users-company'),
    path('assign-case/', views.assign_case, name='assign-case'),
    path('update-order/<str:order_id>', views.update_order, name='update-order'),
    path('dashboard-template/', views.dashboard_template, name='dashboard-template'),
    path('finsh-order/<str:id>', views.finish_order, name='finsh-order'),
    path('delete-order/<str:id>', views.delete_order, name='delete-order'),
    path('closed-orders/', views.closed_orders, name='closed-orders'),
    path('deleted-orders/', views.deleted_orders, name='deleted-orders'),
    path('invoice-order/<str:id>', views.invoice_order, name='invoice-order'),
    path('invoiced-orders/', views.invoiced_orders, name='invoiced-orders'),
    path('make-payment/', views.make_payment, name='make-payment'),
    path('order-payments/', views.order_payments, name='order-payments'),
    path('create-supplier/', views.create_supplier, name='create-supplier'),
    path('suppliers-company/', views.suppliers_company, name='suppliers-company'),
]
