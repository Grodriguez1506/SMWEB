from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Company(models.Model):
    name = models.CharField(verbose_name="Empresa", max_length=255, null=False)
    status = models.BooleanField(verbose_name="¿Activo?", default= True)
    users_limit = models.IntegerField(verbose_name="Limite de usuarios", default=10)
    created_at = models.DateField(verbose_name="Creada el", auto_now_add=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
    
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    rol = models.CharField(max_length=60, null=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

class WorkOrder(models.Model):
    order_id = models.CharField(verbose_name="Número de caso", max_length=255, primary_key = True)
    client = models.CharField(verbose_name="Cliente", max_length=255, null=False, default="")
    city = models.CharField(verbose_name="Ciudad", max_length=255, null=False)
    invesment = models.DecimalField(verbose_name="Inversión", max_digits=20, decimal_places=2, null= True)
    sales_value = models.DecimalField(verbose_name="Valor de venta", max_digits=20, decimal_places=2, null= True)
    service_description = models.TextField(verbose_name="Descripción del servicio")
    remarks = models.TextField("Observaciones del caso", null= True)
    in_charge = models.CharField(verbose_name="Encargado", max_length=255, null=False, default="")
    assigned_by = models.CharField(verbose_name="Asignado por", max_length=255, null= False, default="")
    status = models.CharField(verbose_name="Estado", max_length=50, null= False, default="Activo")
    created_at = models.DateField(verbose_name="Asignado el", auto_now_add=True)
    company = models.CharField(verbose_name="Empresa", max_length=255, null=False, default="")

    class Meta:
        verbose_name = 'Orden de trabajo'
        verbose_name_plural = 'Ordenes de trabajo'
    
    def __str__(self):
        return self.order_id
    
class FinishedOrder(models.Model):
    order_id = models.CharField(verbose_name="Número de caso", max_length=255, primary_key = True)
    client = models.CharField(verbose_name="Cliente", max_length=255, null=False, default="")
    city = models.CharField(verbose_name="Ciudad", max_length=255, null=False)
    invesment = models.DecimalField(verbose_name="Inversión", max_digits=20, decimal_places=2, null= True)
    sales_value = models.DecimalField(verbose_name="Valor de venta", max_digits=20, decimal_places=2, null= True)
    service_description = models.TextField(verbose_name="Descripción del servicio")
    remarks = models.TextField("Observaciones del caso", null= True)
    in_charge = models.CharField(verbose_name="Encargado", max_length=255, null=False, default="")
    assigned_by = models.CharField(verbose_name="Asignado por", max_length=255, null= False, default="")
    status = models.CharField(verbose_name="Estado", max_length=50, null= False, default="Activo")
    finished_at = models.DateField(verbose_name="Finalizado el", auto_now_add=True)
    company = models.CharField(verbose_name="Empresa", max_length=255, null=False, default="")
    finished_by = models.CharField(verbose_name="Finalizado por", max_length=255, null= False, default="")

    class Meta:
        verbose_name = 'Orden finalizada'
        verbose_name_plural = 'Ordenes finalizadas'
    
    def __str__(self):
        return self.order_id
    
class DeletedOrder(models.Model):
    order_id = models.CharField(verbose_name="Número de caso", max_length=255, primary_key = True)
    client = models.CharField(verbose_name="Cliente", max_length=255, null=False, default="")
    city = models.CharField(verbose_name="Ciudad", max_length=255, null=False)
    invesment = models.DecimalField(verbose_name="Inversión", max_digits=20, decimal_places=2, null= True)
    sales_value = models.DecimalField(verbose_name="Valor de venta", max_digits=20, decimal_places=2, null= True)
    service_description = models.TextField(verbose_name="Descripción del servicio")
    remarks = models.TextField("Observaciones del caso", null= True)
    in_charge = models.CharField(verbose_name="Encargado", max_length=255, null=False, default="")
    assigned_by = models.CharField(verbose_name="Asignado por", max_length=255, null= False, default="")
    status = models.CharField(verbose_name="Estado", max_length=50, null= False, default="Activo")
    deleted_at = models.DateField(verbose_name="Eliminado el", auto_now_add=True)
    company = models.CharField(verbose_name="Empresa", max_length=255, null=False, default="")
    deleted_by = models.CharField(verbose_name="Eliminado por", max_length=255, null= False, default="")

    class Meta:
        verbose_name = 'Orden eliminada'
        verbose_name_plural = 'Ordenes eliminadas'
    
    def __str__(self):
        return self.order_id

class InvoicedOrder(models.Model):
    order_id = models.CharField(verbose_name="Número de caso", max_length=255, primary_key = True)
    client = models.CharField(verbose_name="Cliente", max_length=255, null=False, default="")
    city = models.CharField(verbose_name="Ciudad", max_length=255, null=False)
    invesment = models.DecimalField(verbose_name="Inversión", max_digits=20, decimal_places=2, null= True)
    sales_value = models.DecimalField(verbose_name="Valor de venta", max_digits=20, decimal_places=2, null= True)
    service_description = models.TextField(verbose_name="Descripción del servicio")
    remarks = models.TextField("Observaciones del caso", null= True)
    in_charge = models.CharField(verbose_name="Encargado", max_length=255, null=False, default="")
    assigned_by = models.CharField(verbose_name="Asignado por", max_length=255, null= False, default="")
    status = models.CharField(verbose_name="Estado", max_length=50, null= False, default="Activo")
    company = models.CharField(verbose_name="Empresa", max_length=255, null=False, default="")
    invoiced_by = models.CharField(verbose_name="facturado por", max_length=255, null= False, default="")
    invoice_id = models.CharField(verbose_name="Número de factura", max_length=255, null= False, default="")
    invoiced_at = models.DateField(verbose_name="Fecha de factura", auto_now_add=True)

    class Meta:
        verbose_name = 'Orden facturada'
        verbose_name_plural = 'Ordenes facturadas'
    
    def __str__(self):
        return self.order_id

class OrderPayment(models.Model):
    order_id = models.CharField(verbose_name="Número de caso", max_length=255)
    client = models.CharField(verbose_name="Cliente", max_length=255, null=False, default="")
    city = models.CharField(verbose_name="Ciudad", max_length=255, null=False)
    invesment = models.DecimalField(verbose_name="Inversión", max_digits=20, decimal_places=2, null= True)
    sales_value = models.DecimalField(verbose_name="Valor de venta", max_digits=20, decimal_places=2, null= True)
    service_description = models.TextField(verbose_name="Descripción del servicio")
    in_charge = models.CharField(verbose_name="Encargado", max_length=255, null=False, default="")
    company = models.CharField(verbose_name="Empresa", max_length=255, null=False, default="")
    account_owner = models.CharField(verbose_name="Propietario de la cuenta", max_length=255, default="")
    bank_account = models.CharField(verbose_name="Banco", max_length=255, default="")
    account_number = models.CharField(verbose_name="Número de cuenta", max_length=255, default="")
    type_account = models.CharField(verbose_name="Tipo de cuenta", max_length=255, default="")
    amount = models.IntegerField(verbose_name="Pago")
    comments = models.TextField(verbose_name="Comentarios")
    made_by = models.CharField(verbose_name="Realizado por", max_length=255)
    created_at = models.DateField(verbose_name="Creado el", auto_now_add=True)

    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
    
    def __str__(self):
        return self.order_id
    
class Supplier(models.Model):
    full_name = models.CharField(verbose_name="Nombres y apellidos", max_length=255)
    type_document = models.CharField(verbose_name="Tipo de documento", max_length=255)
    document_number = models.CharField(verbose_name="Número de documento", max_length=255)
    bank_account = models.CharField(verbose_name="Banco", max_length=255)
    account_number = models.CharField(verbose_name="Número de cuenta", max_length=255)
    type_account = models.CharField(verbose_name="Tipo de cuenta", max_length=255)
    company = models.CharField(verbose_name="Empresa", max_length=255, default="")
    city = models.CharField(verbose_name="city", max_length=255, default="")
    
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
    
    def __str__(self):
        return self.full_name
    
class PaymentRejected(models.Model):
    order_id = models.CharField(verbose_name="Número de caso", max_length=255)
    client = models.CharField(verbose_name="Cliente", max_length=255, null=False, default="")
    city = models.CharField(verbose_name="Ciudad", max_length=255, null=False)
    invesment = models.DecimalField(verbose_name="Inversión", max_digits=20, decimal_places=2, null= True)
    sales_value = models.DecimalField(verbose_name="Valor de venta", max_digits=20, decimal_places=2, null= True)
    service_description = models.TextField(verbose_name="Descripción del servicio")
    in_charge = models.CharField(verbose_name="Encargado", max_length=255, null=False, default="")
    company = models.CharField(verbose_name="Empresa", max_length=255, null=False, default="")
    account_owner = models.CharField(verbose_name="Propietario de la cuenta", max_length=255, default="")
    bank_account = models.CharField(verbose_name="Banco", max_length=255, default="")
    account_number = models.CharField(verbose_name="Número de cuenta", max_length=255, default="")
    type_account = models.CharField(verbose_name="Tipo de cuenta", max_length=255, default="")
    amount = models.IntegerField(verbose_name="Pago")
    comments = models.TextField(verbose_name="Comentarios")
    made_by = models.CharField(verbose_name="Realizado por", max_length=255)
    created_at = models.DateField(verbose_name="Creado el")
    rejected_at = models.DateField(verbose_name="Rechazado el", auto_now_add=True)
    rejected_by = models.CharField(verbose_name="Rechazado por", max_length=255)

    class Meta:
        verbose_name = 'Pago rechazado'
        verbose_name_plural = 'Pagos rechazados'
    
    def __str__(self):
        return self.order_id
    
class PaymentApproved(models.Model):
    order_id = models.CharField(verbose_name="Número de caso", max_length=255)
    client = models.CharField(verbose_name="Cliente", max_length=255, null=False, default="")
    city = models.CharField(verbose_name="Ciudad", max_length=255, null=False)
    invesment = models.DecimalField(verbose_name="Inversión", max_digits=20, decimal_places=2, null= True)
    sales_value = models.DecimalField(verbose_name="Valor de venta", max_digits=20, decimal_places=2, null= True)
    service_description = models.TextField(verbose_name="Descripción del servicio")
    in_charge = models.CharField(verbose_name="Encargado", max_length=255, null=False, default="")
    company = models.CharField(verbose_name="Empresa", max_length=255, null=False, default="")
    account_owner = models.CharField(verbose_name="Propietario de la cuenta", max_length=255, default="")
    bank_account = models.CharField(verbose_name="Banco", max_length=255, default="")
    account_number = models.CharField(verbose_name="Número de cuenta", max_length=255, default="")
    type_account = models.CharField(verbose_name="Tipo de cuenta", max_length=255, default="")
    amount = models.IntegerField(verbose_name="Pago")
    comments = models.TextField(verbose_name="Comentarios")
    made_by = models.CharField(verbose_name="Realizado por", max_length=255)
    created_at = models.DateField(verbose_name="Creado el")
    approved_at = models.DateField(verbose_name="Rechazado el", auto_now_add=True)
    approved_by = models.CharField(verbose_name="Rechazado por", max_length=255)

    class Meta:
        verbose_name = 'Pago aprobado'
        verbose_name_plural = 'Pagos aprobados'
    
    def __str__(self):
        return self.order_id

class Affiliation(models.Model):
    order_id = models.CharField(verbose_name="Número de caso", max_length=255)
    client = models.CharField(verbose_name="Cliente", max_length=255, null=False, default="")
    city = models.CharField(verbose_name="Ciudad", max_length=255, null=False)
    in_charge = models.CharField(verbose_name="Encargado", max_length=255, null=False, default="")
    full_name = models.CharField(verbose_name="Nombres y Apellidos", max_length=255, null= False)
    since = models.DateField(verbose_name="Desde")
    up_to = models.DateField(verbose_name="Hasta")
    company = models.CharField(verbose_name="Empresa", max_length=255, null=False)
    created_by = models.CharField(verbose_name="Realizado por", max_length=255, null=False)
    created_at = models.DateField(verbose_name="Realizado el", auto_now_add=True)

    class Meta:
        verbose_name = 'Afiliación'
        verbose_name_plural = 'Afiliaiciones'
    
    def __str__(self):
        return self.order_id
