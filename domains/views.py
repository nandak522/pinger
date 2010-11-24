from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from domains.models import Domain
from django.utils import simplejson as json
from utils import response, post_data
import urllib2
from django.conf import settings

def view_homepage(request, homepage_template):
    return response(request, homepage_template, {'domains':Domain.objects.all()})

def _ping_domain(domain):
    headers = {'User-Agent':'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.10) Gecko/20100915 Ubuntu/10.04 (lucid) Firefox/3.6'}
    _build_request_opener()
    request = urllib2.Request(url=domain.name,
                              headers=headers)
    try:
        response = urllib2.urlopen(request)
        response_code = response.code
    except urllib2.URLError,e:
        response_code = 600
    domain.last_pinged = datetime.now()
    domain.save()
    return response_code

def _build_request_opener():
    if hasattr(settings, 'IS_PROXY_CONNECTION') and settings.IS_PROXY_CONNECTION:
        proxy_info = {'user' : settings.PROXY_SETTINGS['username'],
                      'pass' : settings.PROXY_SETTINGS['password'],
                      'host' : settings.PROXY_SETTINGS['host'],
                      'port' : settings.PROXY_SETTINGS['port']}
        proxy_support = urllib2.ProxyHandler({"http" : "http://%(user)s:%(pass)s@%(host)s:%(port)d" % proxy_info})
        opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
    else:
        pass

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