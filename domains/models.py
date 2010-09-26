from django.db import models
from common.models import BaseModel, BaseModelManager
from datetime import datetime

class DomainManager(BaseModelManager):
    def create_domain(self, domain):
        existing_domain = self.exists(domain)
        if existing_domain:
            return existing_domain
        domain = Domain(name=domain, last_pinged=datetime.now())
        domain.save()
        return domain
    
    def exists(self, domain_name):
        #TODO:domain_name = self.clean_domain_name(domain_name)
        try:
            return self.get(name=domain_name)
        except Domain.DoesNotExist:
            return None
        
    def clean_domain_name(self, domain_name):
        #TODO:Remove https,http
        #TODO:If www doesn't exist, prefix the domain with it. Store in the db with always a subdomain(atleast www)
        raise NotImplementedError
        
class Domain(BaseModel):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    last_pinged = models.DateTimeField()
    objects = DomainManager()
    
    def __unicode__(self):
        return self.name