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
    path('user-order-payments/', views.user_order_payments, name='user-order-payments'),
    path('handle-payment/<int:id>', views.handle_payment, name='handle-payment'),
    path('handle-rejected-payment/<int:id>', views.handle_rejected_payment, name='handle-rejected-payment'),
    path('delete-rejected-payment/<int:id>', views.delete_rejected_payment, name='delete-rejected-payment'),
    path('reject-payment/<int:id>', views.reject_payment, name='reject-payment'),
    path('approve-payment/<int:id>', views.approve_payment, name='approve-payment'),
    path('rejected-payments/', views.rejected_payments, name='rejected-payments'),
    path('user-rejected-payments/', views.user_rejected_payments, name='user-rejected-payments'),
    path('approved-payments/', views.approved_payments, name='approved-payments'),
    path('user-approved-payments/', views.user_approved_payments, name='user-approved-payments'),
    path('create-supplier/', views.create_supplier, name='create-supplier'),
    path('suppliers-company/', views.suppliers_company, name='suppliers-company'),
    path('make-affiliation/', views.make_affiliattion, name='make-affiliation'),
    path('order-affiliations/', views.order_affiliations, name='order-affiliations'),
    path('user-order-affiliations/', views.user_order_affiliations, name='user-order-affiliations'),
    path('reject-affiliation/<int:id>', views.reject_affiliation, name='reject-affiliation'),
    path('approve-affiliation/<int:id>', views.approve_affiliation, name='approve-affiliation'),
    path('handle-affiliation/<int:id>', views.handle_affiliation, name='handle-affiliation'),
    path('rejected-affiliations/', views.rejected_affiliations, name='rejected-affiliations'),
    path('user-rejected-affiliations/', views.user_rejected_affiliations, name='user-rejected-affiliations'),
    path('approved-affiliations/', views.approved_affiliations, name='approved-affiliations'),
    path('user-approved-affiliations/', views.user_approved_affiliations, name='user-approved-affiliations'),
    path('select-user/<int:user_id>', views.select_user, name='select-user'),
    path('delete-user/<int:user_id>', views.delete_user, name='delete-user'),
]
