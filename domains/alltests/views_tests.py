from datetime import datetime
from domains.models import Domain
from utils import TestCase
from django.core.urlresolvers import reverse as url_reverse

class DomainStatusTests(TestCase):
    fixtures = ['domains.json']

    def test_status_of_a_sample_domain(self):
        domain_name = 'http://www.teykee.com'
        domain = Domain.objects.get(name=domain_name)
        last_pinged_timestamp = domain.last_pinged
        response = self.client.post(url_reverse('domains.views.view_check_status'),
                                    {'domain_id':domain.id})
        self.assertTrue(response)
        self.assertEquals(response.content, '200')
        self.assertTrue(Domain.objects.get(name=domain_name).last_pinged > last_pinged_timestamp)