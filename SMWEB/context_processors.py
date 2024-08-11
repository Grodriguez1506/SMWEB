from .models import Company

def get_status(request):
    
    if request.user.is_authenticated:

        id = request.user.company_id

        company = Company.objects.get(id = id)

        return {
            'company': company
        }
    else:
        return {
            'company' : False
        }