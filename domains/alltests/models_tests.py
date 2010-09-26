from datetime import datetime
from domains.models import Domain
from utils import TestCase

class DomainCreationTests(TestCase):
    fixtures = ['domains.json']

    def test_create_a_sample_domain(self):
        domain_name = 'www.xyz.com'
        Domain.objects.create_domain(domain=domain_name)
        domain = Domain.objects.latest()
        self.assertTrue(domain)
        self.assertEquals(domain.name, domain_name)
        self.assertEquals(domain.last_pinged.minute, datetime.now().minute)

    def test_duplicate_domain_creation(self):
        domains = ['www.google.com', 
                   'www.gmail.com', 
#                   'http://www.google.com', 
#                   'https://google.com'
                   ]
        for domain in domains:
            existing_domains_count = Domain.objects.count()
            Domain.objects.create_domain(domain=domain)
            self.assertEquals(Domain.objects.count(), existing_domains_count)