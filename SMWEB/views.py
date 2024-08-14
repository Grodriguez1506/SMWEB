from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.utils import timezone
from .utils import format_amount
from datetime import datetime
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth

# Create your views here.

def inicio(request):

    if request.user.is_authenticated:

        user_rol = request.user.rol

        user_company = request.user.company_id

        if user_rol == 'administrador':

            return render(request, 'index.html')

        if user_rol == 'gerente':

            orders = WorkOrder.objects.filter(company = user_company).order_by('-order_id')

            return render(request, 'index.html',{
            'orders': orders
        })

        elif user_rol == 'coordinador':

            orders = WorkOrder.objects.filter(company = user_company).order_by('-order_id')

            return render(request, 'index.html',{
            'orders': orders
        })

        elif user_rol == 'gestor':

            first_name = request.user.first_name
            
            orders = WorkOrder.objects.filter(in_charge = first_name.upper()).filter(company = user_company).order_by('-order_id')

            return render(request, 'index.html',{
            'orders': orders
        })

        elif user_rol == 'recursos humanos':
            pass
        elif user_rol == 'financiero':
            pass
        elif user_rol == 'compras':
            pass
        elif user_rol == 'facturacion':
            
            finished_orders = FinishedOrder.objects.filter(company = user_company).order_by('-order_id')

            return render(request, 'index.html',{
            'finished_orders': finished_orders
        })

    return render(request, 'index.html')

@login_required(login_url=inicio)
def invoiced_orders(request):
    
    user_rol = request.user.rol

    user_company = request.user.company_id

    if user_rol not in ['facturacion', 'gerente']:

        
        messages.warning(request, f'Tu rol de {user_rol} no te permite visualizar los casos facturados')
        return redirect('inicio')

    orders = InvoicedOrder.objects.filter(company = user_company).order_by('-order_id')

    return render(request, 'invoiced_orders.html',{
        'orders': orders
    })
    

@login_required(login_url=inicio)
def closed_orders(request):

    user_rol = request.user.rol

    user_company = request.user.company_id

    if user_rol == 'gerente' or user_rol == 'coordinador':

        orders = FinishedOrder.objects.filter(company = user_company).order_by('-order_id')

        return render(request, 'closed_orders.html', {
            'orders': orders
        })

    if user_rol == 'gestor':

        first_name = request.user.first_name

        orders = FinishedOrder.objects.filter(in_charge=first_name.upper()).filter(company = user_company).order_by('-order_id')

        return render(request, 'closed_orders.html', {
            'orders': orders
        })

    return redirect('inicio')

@login_required(login_url=inicio)
def deleted_orders(request):

    user_rol = request.user.rol

    user_company = request.user.company_id

    if user_rol == 'gerente' or user_rol == 'coordinador':

        orders = DeletedOrder.objects.filter(company = user_company).order_by('-order_id')

        return render(request, 'deleted_orders.html', {
            'orders': orders
        })

    if user_rol == 'gestor':

        first_name = request.user.first_name

        orders = DeletedOrder.objects.filter(in_charge=first_name.upper()).order_by('-order_id')

        return render(request, 'deleted_orders.html', {
            'orders': orders
        })

    return redirect('inicio')

@login_required(login_url=inicio)
def logout_user(request):

    logout(request)

    return redirect('inicio')

def login_user(request):

    if request.user.is_authenticated:

        return redirect('inicio')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                messages.warning(request, 'Usuario o contraseña inválidos')

        return render(request, 'login.html')

@login_required(login_url=inicio)
def new_user(request):

    user_rol = request.user.rol
    
    if user_rol != 'administrador':

        messages.warning(request, 'Esta función es solo del administrador del software')

        return redirect('inicio')

    user = request.user

    companies = Company.objects.all()

    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            rol = request.POST['rol']
            company_id = request.POST['company']

            company = Company.objects.get(id = company_id)

            users = CustomUser.objects.filter(company = company_id).count()

            if users == company.users_limit:

                messages.warning(request, f'Lo siento, {company.name} superó el límite de usuarios, ponte en contacto con tu proveedor de software')

            elif username and password and first_name and last_name and email and rol and company_id:
                user = CustomUser(
                username = username,
                rol = rol,
                first_name = first_name,
                last_name = last_name,
                email = email,
                is_staff = False,
                is_active = True
                )

                user.company_id = int(company_id)

                user.set_password(password)

                user.save()

                messages.success(request, 'El usuario ha sido creado de manera exitosa')

                return redirect('inicio')
            
            else:
                messages.warning(request, 'Completa los campos vacíos del formulario')
        except:
            messages.warning(request, 'Valida los campos con errores')

    return render(request, 'new_user.html',{
        'companies': companies
    })

@login_required(login_url=inicio)
def new_company_user(request):
    
    user_rol = request.user.rol
    
    if user_rol != 'recursos humanos':

        messages.warning(request, f'Tu rol de {user_rol} no te permite acceder a esta función')

        return redirect('inicio')
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            rol = request.POST['rol']

            company_id = request.user.company_id

            company = Company.objects.get(id = company_id)

            users = CustomUser.objects.filter(company = company_id).count()

            if users == company.users_limit:

                messages.warning(request, f'Lo siento, {company.name} superó el límite de usuarios, ponte en contacto con tu proveedor de software')

            elif username and password and first_name and last_name and email and rol:
                user = CustomUser(
                username = username,
                rol = rol,
                first_name = first_name,
                last_name = last_name,
                email = email,
                is_staff = False,
                is_active = True
                )

                user.company_id = company_id

                user.set_password(password)

                user.save()

                messages.success(request, 'El usuario ha sido creado de manera exitosa')

                return redirect('inicio')
            else:
                messages.warning(request, 'Completa los campos vacíos del formulario')

        except:
            messages.warning(request, 'Valida los campos con errores')

    return render(request, 'new_company_user.html')

@login_required(login_url=inicio)
def users_availables(request):

    user_rol = request.user.rol
    
    if user_rol != 'administrador':

        messages.warning(request, 'Esta función es solo del administrador del software')

        return redirect('inicio')
    else:

        users = CustomUser.objects.all()

        return render(request, 'users.html',{
            'users': users
        })

@login_required(login_url=inicio)
def users_company(request):

    user_rol = request.user.rol
    
    if user_rol not in ['recursos humanos', 'gerente']:

        messages.warning(request, f'Tu rol de {user_rol} no te permite acceder a esta función')

        return redirect('inicio')
    else:
        company = request.user.company_id

        users = CustomUser.objects.filter(company_id = company)

        return render(request, 'users_company.html',{
            'users': users
        })

@login_required(login_url=inicio)
def assign_case(request):

    user_rol = request.user.rol

    if user_rol not in ['coordinador', 'gerente']:

        messages.warning(request, f'Tu rol de {user_rol} no te permite asignar casos')

        return redirect('inicio')
    else:
        company_id = request.user.company_id

        users = CustomUser.objects.filter(company_id = company_id).filter(rol = 'gestor').order_by('first_name')

        if request.method == 'POST':
            
            order_id = request.POST['order_id']
            client = request.POST['client']
            city = request.POST['city']
            in_charge = request.POST['in_charge']
            service_description = request.POST['service_description']

            if order_id and client and city and in_charge and service_description:

                try:
                    new_order = WorkOrder(
                        order_id = order_id,
                        client = client.upper(),
                        city = city.upper(),
                        in_charge = in_charge.upper(),
                        service_description = service_description.upper(),
                        assigned_by = request.user.username,
                        company = request.user.company_id
                    )

                    new_order.save()

                    messages.success(request, f'El caso ha sigo asignado a {in_charge} satisfactoriamente')

                    return redirect('inicio')
                
                except Exception as ep:

                    messages.warning(request, f'{ep}')

                    return render(request, 'assign_case.html', {
                            'users': users
                        })
            else:

                messages.warning(request, 'Debes diligenciar todos los campos obligatorios')

                return render(request, 'assign_case.html', {
                            'users': users
                        })

        else:
            return render(request, 'assign_case.html', {
            'users': users
        })


@login_required(login_url=inicio)
def update_order(request, order_id):

    order = WorkOrder.objects.get(order_id = order_id)

    if order.sales_value and order.invesment:

        profit = float(order.sales_value) - float(order.invesment)

        formatted_profit = format_amount(profit)

        result = (int(profit) / int(order.sales_value)) * 100

        profit_percentage = round(result, 2)
    
    elif order.sales_value:

        profit = float(order.sales_value) - 0

        formatted_profit = format_amount(profit)

        result = (int(profit) / int(order.sales_value)) * 100

        profit_percentage = round(result, 2)
    
    elif order.invesment:

        profit = 0 - float(order.invesment)

        formatted_profit = format_amount(profit)

        result = int(profit) * 100

        profit_percentage = round(result, 2)

    else:
        formatted_profit = 0

        profit_percentage = 0

    if request.method == 'POST':
        invesment = request.POST['invesment']
        sales_value = request.POST['sales_value']
        status = request.POST['status']
        remarks = request.POST['remarks']

        if invesment and sales_value and status and remarks:

            order.invesment = invesment
            order.sales_value = sales_value
            order.status = status
            order.remarks = remarks.upper()

            order.save()
        elif invesment and sales_value and status:

            order.invesment = invesment
            order.status = status
            order.sales_value = sales_value

            order.save()
        elif invesment and remarks and status:

            order.invesment = invesment
            order.status = status
            order.remarks = remarks.upper()

            order.save()
        elif sales_value and remarks and status:

            order.sales_value = sales_value
            order.status = status
            order.remarks = remarks.upper()

            order.save()
        
        elif invesment and remarks and sales_value:

            order.sales_value = sales_value
            order.status = status
            order.remarks = remarks.upper()

            order.save()

        elif invesment and sales_value:

            order.invesment = invesment
            order.sales_value = sales_value

            order.save()

        elif invesment and remarks:

            order.invesment = invesment
            order.remarks = remarks

            order.save()

        elif invesment and status:

            order.invesment = invesment
            order.status = status

            order.save()

        elif sales_value and remarks:

            order.sales_value = sales_value
            order.remarks = remarks

            order.save()

        elif sales_value and status:

            order.sales_value = sales_value
            order.status = status

            order.save()

        elif remarks and status:

            order.remarks = remarks
            order.status = status

            order.save()

        elif invesment:

            order.invesment = invesment
            
            order.save()

        elif sales_value:

            order.sales_value = sales_value
            
            order.save()
        
        elif remarks:

            order.remarks = remarks.upper()
            
            order.save()
        
        elif status:

            order.status = status

            order.save()

        order = WorkOrder.objects.get(order_id = order_id)

        if order.sales_value and order.invesment:

            profit = float(order.sales_value) - float(order.invesment)

            formatted_profit = format_amount(profit)

            result = (int(profit) / int(order.sales_value)) * 100

            profit_percentage = round(result, 2)
        
        elif order.sales_value:

            profit = float(order.sales_value) - 0

            formatted_profit = format_amount(profit)

            result = (int(profit) / int(order.sales_value)) * 100

            profit_percentage = round(result, 2)
        
        elif order.invesment:

            profit = 0 - float(order.invesment)

            formatted_profit = format_amount(profit)

            result = int(profit) * 100

            profit_percentage = round(result, 2)

        else:
            formatted_profit = 0

            profit_percentage = 0

        messages.success(request, 'Actualización realizada con éxito.')

        return render(request, 'update_order.html',{
        'order': order,
        'profit': formatted_profit,
        'percentage': profit_percentage
        })

    return render(request, 'update_order.html',{
        'order': order,
        'profit': formatted_profit,
        'percentage': profit_percentage
    })


@login_required(login_url=inicio)
def invoice_order(request, id):

    order = FinishedOrder.objects.get(order_id = id)

    profit = float(order.sales_value) - float(order.invesment)

    formatted_profit = format_amount(profit)

    result = (int(profit) / int(order.sales_value)) * 100

    profit_percentage = round(result, 2)

    if request.method == 'POST':
        invoice_id = request.POST['invoice_id']

        invoiced_order = InvoicedOrder(
            order_id = order.order_id,
            client = order.client,
            city = order.city,
            invesment = order.invesment,
            sales_value = order.sales_value,
            service_description = order.service_description,
            remarks = order.remarks,
            in_charge = order.in_charge,
            assigned_by = order.assigned_by,
            status = "Facturado",
            company = order.company,
            invoiced_by = request.user.username,
            invoice_id = invoice_id,
        )

        invoiced_order.save()
        order.delete()

        messages.success(request, f'El caso {id} ha sido facturado exitosamente')
        return redirect('inicio')

    return render(request, 'invoice_order.html',{
        'order': order,
        'profit': formatted_profit,
        'percentage': profit_percentage
    })

@login_required(login_url=inicio)
def dashboard_template(request):

    company = request.user.company_id

    if request.method == 'POST':
        report = request.POST['report']
        if report == 'ventas finalizadas':
            since = request.POST['since']
            up_to = request.POST['up_to']
            if since and up_to:
                # Convertir las cadenas de texto a objetos datetime.date
                fecha_inicio = datetime.strptime(since, '%Y-%m-%d').date()
                fecha_fin = datetime.strptime(up_to, '%Y-%m-%d').date()

                labels = []
                data = []

                queryset = FinishedOrder.objects.filter(finished_at__range=(fecha_inicio, fecha_fin)).filter(company = company)

                resultado = queryset.annotate(month=TruncMonth('finished_at')).values('month').annotate(total=Sum('sales_value')).order_by('month')

                labels = [venta['month'].strftime('%Y-%m') for venta in resultado]
                data = [float(venta['total']) for venta in resultado]

                return render(request, 'dashboard_ventas.html',{
                    'labels': labels,
                    'data': data
                })
            
        elif report == 'ventas finalizadas por gestor':
            since = request.POST['since']
            up_to = request.POST['up_to']

            if since and up_to:
                # Convertir las cadenas de texto a objetos datetime.date
                fecha_inicio = datetime.strptime(since, '%Y-%m-%d').date()
                fecha_fin = datetime.strptime(up_to, '%Y-%m-%d').date()

                labels = []
                data = []

                queryset = FinishedOrder.objects.filter(finished_at__range=(fecha_inicio, fecha_fin)).filter(company = company)

                resultado = queryset.values('in_charge').annotate(total=Sum('sales_value')).order_by('in_charge')

                labels = [venta['in_charge'] for venta in resultado]
                data = [float(venta['total']) for venta in resultado]

                return render(request, 'dashboard_ventas.html',{
                    'labels': labels,
                    'data': data
                })
        elif report == 'casos activos por gestor':
            since = request.POST['since']
            up_to = request.POST['up_to']

            if since and up_to:
                # Convertir las cadenas de texto a objetos datetime.date
                fecha_inicio = datetime.strptime(since, '%Y-%m-%d').date()
                fecha_fin = datetime.strptime(up_to, '%Y-%m-%d').date()

                queryset = WorkOrder.objects.filter(created_at__range=(fecha_inicio, fecha_fin)).filter(company = company)

                resultado = queryset.values('in_charge').annotate(total=Count('order_id'))

                gestores = [gestor['in_charge'] for gestor in resultado]
                totales = [servicio['total'] for servicio in resultado]

                return render(request, 'dashboard_casos.html',{
                    'labels': gestores,
                    'data': totales
                })
        
        elif report == 'casos finalizados por gestor':
            since = request.POST['since']
            up_to = request.POST['up_to']

            if since and up_to:
                # Convertir las cadenas de texto a objetos datetime.date
                fecha_inicio = datetime.strptime(since, '%Y-%m-%d').date()
                fecha_fin = datetime.strptime(up_to, '%Y-%m-%d').date()

                queryset = FinishedOrder.objects.filter(finished_at__range=(fecha_inicio, fecha_fin)).filter(company = company)

                resultado = queryset.values('in_charge').annotate(total=Count('order_id'))

                gestores = [gestor['in_charge'] for gestor in resultado]
                totales = [servicio['total'] for servicio in resultado]

                return render(request, 'dashboard_casos.html',{
                    'labels': gestores,
                    'data': totales
                })
             
    return render(request, 'dashboard_template.html')

@login_required(login_url=inicio)
def finish_order(request, id):

    order = WorkOrder.objects.get(order_id = id)

    finished_order = FinishedOrder(
        order_id = order.order_id,
        client = order.client,
        city = order.city,
        invesment = order.invesment,
        sales_value = order.sales_value,
        service_description = order.service_description,
        remarks = order.remarks,
        in_charge = order.in_charge,
        assigned_by = order.assigned_by,
        status = "Finalizado",
        company = order.company,
        finished_by = request.user.username
        )
    
    finished_order.save()
    order.delete()

    messages.success(request, f'El caso {id} ha sido finalizado con éxito')
    return redirect('inicio')

@login_required(login_url=inicio)
def delete_order(request, id):

    order = WorkOrder.objects.get(order_id = id)

    deleted_order = DeletedOrder(
        order_id = order.order_id,
        client = order.client,
        city = order.city,
        invesment = order.invesment,
        sales_value = order.sales_value,
        service_description = order.service_description,
        remarks = order.remarks,
        in_charge = order.in_charge,
        assigned_by = order.assigned_by,
        status = "Eliminado",
        company = order.company,
        deleted_by = request.user.username
        )
    
    deleted_order.save()
    order.delete()

    messages.success(request, f'El caso {id} ha sido eliminado con éxito')
    return redirect('inicio')

@login_required(login_url=inicio)
def order_payments(request):

    user_rol = request.user.rol

    user_company = request.user.company_id

    if user_rol not in ['gerente', 'financiero', 'coordinador']:

        messages.warning(request, f'Tu rol de {user_rol} no te permite acceder a los pagos recibidos')
        return redirect('inicio')
    
    payments = OrderPayment.objects.filter(company = user_company).order_by('-created_at')

    return render(request, 'order_payments.html',{
        'payments': payments
    })

@login_required(login_url=inicio)
def user_order_payments(request):

    user_rol = request.user.rol

    user_company = request.user.company_id

    first_name = request.user.first_name

    if user_rol != 'gestor':

        messages.warning(request, f'Tu rol de {user_rol} no te permite acceder a los pagos enviados')
        return redirect('inicio')
    
    payments = OrderPayment.objects.filter(company = user_company).filter(in_charge = first_name.upper()).order_by('-created_at')

    return render(request, 'user_order_payments.html',{
        'payments': payments
    })

@login_required(login_url=inicio)
def rejected_payments(request):

    user_rol = request.user.rol

    user_company = request.user.company_id

    if user_rol not in ['gerente', 'financiero', 'coordinador']:

        messages.warning(request, f'Tu rol de {user_rol} no te permite acceder a los pagos rechazados')
        return redirect('inicio')
    
    payments = PaymentRejected.objects.filter(company = user_company).order_by('-created_at')

    return render(request, 'rejected_payments.html',{
        'payments': payments
    })

@login_required(login_url=inicio)
def user_rejected_payments(request):

    user_rol = request.user.rol

    user_company = request.user.company_id

    first_name = request.user.first_name

    if user_rol != 'gestor':

        messages.warning(request, f'Tu rol de {user_rol} no te permite acceder a los pagos rechazados')
        return redirect('inicio')
    
    payments = PaymentRejected.objects.filter(company = user_company).filter(in_charge = first_name.upper()).order_by('-created_at')

    return render(request, 'user_rejected_payments.html',{
        'payments': payments
    })

@login_required(login_url=inicio)
def approved_payments(request):

    user_rol = request.user.rol

    user_company = request.user.company_id

    if user_rol != 'gestor':

        messages.warning(request, f'Tu rol de {user_rol} no te permite acceder a los pagos realizados')
        return redirect('inicio')
    
    payments = PaymentApproved.objects.filter(company = user_company).order_by('-created_at')

    return render(request, 'approved_payments.html',{
        'payments': payments
    })

@login_required(login_url=inicio)
def user_approved_payments(request):

    user_rol = request.user.rol

    user_company = request.user.company_id

    first_name = request.user.first_name

    if user_rol != 'gestor':

        messages.warning(request, f'Tu rol de {user_rol} no te permite acceder a los pagos realizados')
        return redirect('inicio')
    
    payments = PaymentApproved.objects.filter(company = user_company).filter(in_charge = first_name.upper()).order_by('-created_at')

    return render(request, 'user_approved_payments.html',{
        'payments': payments
    })

@login_required(login_url=inicio)
def make_payment(request):

    user_rol = request.user.rol

    user_company = request.user.company_id

    suppliers = Supplier.objects.filter(company = user_company).order_by('full_name')

    if user_rol != 'gestor':

        messages.warning(request, f'Tu rol de {user_rol} no te permite realizar pagos')
        return redirect('inicio')
    
    if request.method == 'POST':
        
        order_id = request.POST['order_id']
        full_name = request.POST['full_name']
        amount = request.POST['amount']
        comments = request.POST['comments']
        first_name = request.user.first_name

        order = WorkOrder.objects.filter(in_charge = first_name.upper()).filter(order_id = order_id).first()
        
        if order is not None:

            if full_name:

                supplier = Supplier.objects.get(full_name = full_name)

                client = order.client
                city = order.city
                invesment = order.invesment
                sales_value = order.sales_value
                service_description = order.service_description
                in_charge = order.in_charge
                company = order.company
                account_owner = full_name
                bank_account = supplier.bank_account
                account_number = supplier.account_number
                type_account = supplier.type_account

                payment = OrderPayment(
                    order_id = order_id,
                    client = client,
                    city = city,
                    invesment = invesment,
                    sales_value = sales_value,
                    service_description = service_description,
                    in_charge = in_charge,
                    company = company,
                    account_owner = account_owner,
                    bank_account = bank_account,
                    account_number = account_number,
                    type_account = type_account,
                    amount = amount,
                    comments = comments.upper(),
                    made_by = request.user.username
                )

                payment.save()
                messages.success(request, f'El pago para la orden {order} se ha registrado exitosamente')
            else:
                messages.warning(request, 'No se ha registrado un destinatario para el pago')
        else:
            messages.warning(request, f'El caso ingresado no existe en la base de datos de {first_name.capitalize()}')

    return render(request, 'make_payment.html',{
        'suppliers': suppliers
    })

@login_required(login_url=inicio)
def create_supplier(request):
    
    user_rol = request.user.rol

    if user_rol != 'financiero':
        messages.warning(request, f'Tu rol de {user_rol} no te permite crear proveedores')

    if request.method == 'POST':
        full_name = request.POST['full_name']
        type_document = request.POST['type_document']
        document_number = request.POST['document_number']
        bank_account = request.POST['bank_account']
        account_number = request.POST['account_number']
        type_account = request.POST['type_account']
        city = request.POST['city']

        supplier = Supplier(
            full_name = full_name.upper(),
            type_document = type_document,
            document_number = document_number,
            bank_account = bank_account.upper(),
            account_number = account_number,
            type_account = type_account,
            company = request.user.company_id,
            city = city.upper()
        )

        supplier.save()
        messages.success(request, f'El proveedor {full_name} ha sido creado exitosamente')
        return redirect('inicio')

    return render(request, 'create_supplier.html')


@login_required(login_url=inicio)
def suppliers_company(request):

    user_rol = request.user.rol
    
    if user_rol != 'financiero':

        messages.warning(request, f'Tu rol de {user_rol} no te permite acceder a esta función')

        return redirect('inicio')
    else:
        company = request.user.company_id

        suppliers = Supplier.objects.filter(company = company)

        return render(request, 'suppliers.html',{
            'suppliers': suppliers
        })
    
@login_required(login_url=inicio)
def handle_payment(request, id):
    
    payment = OrderPayment.objects.get(id = id)

    return render(request, 'handle_payment.html',{
        'payment': payment
    })

@login_required(login_url=inicio)
def handle_rejected_payment(request, id):
    
    payment_rejected = PaymentRejected.objects.get(id = id)

    user_company = request.user.company_id

    suppliers = Supplier.objects.filter(company = user_company).order_by('full_name')

    if request.method == 'POST':
        
        full_name = request.POST['full_name']
        amount = request.POST['amount']
        comments = request.POST['comments']
        first_name = request.user.first_name

        order = WorkOrder.objects.filter(in_charge = first_name.upper()).filter(order_id = payment_rejected.order_id).first()
        
        if order is not None:

            if full_name:

                supplier = Supplier.objects.get(full_name = full_name)

                client = order.client
                city = order.city
                invesment = order.invesment
                sales_value = order.sales_value
                service_description = order.service_description
                in_charge = order.in_charge
                company = order.company
                account_owner = full_name
                bank_account = supplier.bank_account
                account_number = supplier.account_number
                type_account = supplier.type_account

                payment = OrderPayment(
                    order_id = payment_rejected.order_id,
                    client = client,
                    city = city,
                    invesment = invesment,
                    sales_value = sales_value,
                    service_description = service_description,
                    in_charge = in_charge,
                    company = company,
                    account_owner = account_owner,
                    bank_account = bank_account,
                    account_number = account_number,
                    type_account = type_account,
                    amount = amount,
                    comments = comments.upper(),
                    made_by = request.user.username
                )

                payment.save()
                payment_rejected.delete()
                messages.success(request, f'El pago para la orden {order} se ha reenviado exitosamente')
                return redirect('inicio')
            
            messages.warning(request, 'No se ha registrado un destinatario para el pago')
        else:
            messages.warning(request, f'El caso ingresado no existe en la base de datos de {first_name.capitalize()}')

    return render(request, 'handle_rejected_payment.html',{
        'payment': payment_rejected,
        'suppliers': suppliers
    })

@login_required(login_url=inicio)
def reject_payment(request, id):

    payment = OrderPayment.objects.get(id= id)

    payment_rejected = PaymentRejected(
        order_id = payment.order_id,
        client = payment.client,
        city = payment.city,
        invesment = payment.invesment,
        sales_value = payment.sales_value,
        service_description = payment.service_description,
        in_charge = payment.in_charge,
        company = payment.company,
        account_owner = payment.account_owner,
        bank_account = payment.bank_account,
        account_number = payment.account_number,
        type_account = payment.type_account,
        amount = payment.amount,
        comments = payment.comments,
        made_by = payment.made_by,
        created_at = payment.created_at,
        rejected_by = request.user.username
    )

    payment_rejected.save()
    payment.delete()

    messages.warning(request, f'El pago {payment_rejected.order_id} ha sido rechazado satisfactoriamente')
    return redirect('inicio')

@login_required(login_url=inicio)
def approve_payment(request, id):

    payment = OrderPayment.objects.get(id= id)

    payment_approved = PaymentApproved(
        order_id = payment.order_id,
        client = payment.client,
        city = payment.city,
        invesment = payment.invesment,
        sales_value = payment.sales_value,
        service_description = payment.service_description,
        in_charge = payment.in_charge,
        company = payment.company,
        account_owner = payment.account_owner,
        bank_account = payment.bank_account,
        account_number = payment.account_number,
        type_account = payment.type_account,
        amount = payment.amount,
        comments = payment.comments,
        made_by = payment.made_by,
        created_at = payment.created_at,
        approved_by = request.user.username
    )

    payment_approved.save()
    payment.delete()

    messages.success(request, f'El pago {payment_approved.order_id} ha sido aprobado satisfactoriamente')
    return redirect('inicio')
