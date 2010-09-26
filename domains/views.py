from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from domains.models import Domain
from utils import response, get_data, post_data

def view_all_domains(request, all_domains_template):
    return response(request, all_domains_template, {'domains':Domain.objects.all()})

def view_domain_profile(request, domain_id, domain_profile_template):
    domain = get_object_or_404(Domain, id=domain_id)
    return response(request, domain_profile_template, {'domain':domain})
