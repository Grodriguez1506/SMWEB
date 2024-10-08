from .models import Company, PaymentRejected, OrderPayment, Affiliation, RejectedAffiliation

# def get_status(request):


#     if request.user.is_authenticated:

#         id = request.user.company_id

#         company = Company.objects.get(id = id)

#         return {
#             'company': company
#         }
#     else:
#         return {
#             'company' : False
#         }
    
def get_rejected_payments(request):
    
    if request.user.is_authenticated:
        company_id = request.user.company_id

        first_name = request.user.first_name

        rejected_payments = PaymentRejected.objects.filter(company = company_id).filter(in_charge = first_name.upper()).count()

        return {
            'rejected_payments': rejected_payments
        }
    
    return {
        'rejected_payments': False
        }

def get_payments(request):
    
    if request.user.is_authenticated:
        company_id = request.user.company_id

        payments = OrderPayment.objects.filter(company = company_id).count()

        return {
            'received_payments': payments
        }
    
    return {
        'received_payments': False
        }

def get_affiliations(request):
    
    if request.user.is_authenticated:
        company_id = request.user.company_id

        affiliations = Affiliation.objects.filter(company = company_id).count()

        return {
            'received_affiliations': affiliations
        }
    
    return {
        'received_affiliations': False
        }

def get_rejected_affiliations(request):
    
    if request.user.is_authenticated:
        company_id = request.user.company_id

        first_name = request.user.first_name

        rejected_affiliation = RejectedAffiliation.objects.filter(company = company_id).filter(in_charge = first_name.upper()).count()

        return {
            'rejected_affiliations': rejected_affiliation
        }
    
    return {
        'rejected_affiliations': False
        }

def get_notifies(request):

    if request.user.is_authenticated:
        user_rol = request.user.rol

        if user_rol == 'gerente':

            company_id = request.user.company_id

            payments = OrderPayment.objects.filter(company = company_id).count()

            # affiliations = Affiliation.objects.filter(company = company_id).count()
            affiliations = 0

            notifies = payments + affiliations

            return {
                'notifies': notifies
            }

        if user_rol == 'financiero':

            company_id = request.user.company_id

            payments = OrderPayment.objects.filter(company = company_id).count()

            return {
                'notifies': payments
            }

        if user_rol == 'recursos humanos':
            
            company_id = request.user.company_id

            # affiliations = Affiliation.objects.filter(company = company_id).count()
            affiliations = 0

            return {
                'notifies': affiliations
            }

        if user_rol == 'gestor':
            company_id = request.user.company_id

            first_name = request.user.first_name

            rejected_payments = PaymentRejected.objects.filter(company = company_id).filter(in_charge = first_name.upper()).count()
            # rejected_affiliation = RejectedAffiliation.objects.filter(company = company_id).filter(in_charge = first_name.upper()).count()
            rejected_affiliation = 0

            notifies = rejected_payments + rejected_affiliation

            return {
                'notifies': notifies
            }
        else:
            return {
                'notifies': False
            }
    else:
        return {
            'notifies': False
        }