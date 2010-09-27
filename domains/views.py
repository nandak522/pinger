from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from domains.models import Domain
from django.utils import simplejson as json
from utils import response, post_data
import urllib2

def view_homepage(request, homepage_template):
    return response(request, homepage_template, {'domains':Domain.objects.all()})

def _ping_domain(domain):
    try:
        response = urllib2.urlopen(domain.name)
        response_code = response.code
    except urllib2.URLError:
        response_code = 600
    domain.last_pinged = datetime.now()
    domain.save()
    return response_code

def view_check_status(request):
    domain_id = post_data(request).get('domain_id')
    domain = get_object_or_404(Domain, id=domain_id)
    response_code = _ping_domain(domain)
    return HttpResponse(str(response_code))

def view_check_all(request):
    domains = Domain.objects.all()
    statuses = {}
    for domain in domains:
        response_code = _ping_domain(domain)
        statuses[domain.id] = str(response_code)
    return HttpResponse(json.dumps(statuses),
                        mimetype='application/json')        