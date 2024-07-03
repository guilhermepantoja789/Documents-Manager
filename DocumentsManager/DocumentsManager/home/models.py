from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
# Create your models here.

class Document(models.Model):
    doc_name = models.CharField(max_length=100, help_text="Name this document")
    doc_priority = models.IntegerField(help_text="Give this document a number between 1 and 10 to describe its priority")
    doc_tag = models.CharField(max_length=100, help_text="Give this document a tag")
    doc_description = models.TextField(max_length=750, help_text="Give this document a short description")
    doc_last_alteration = models.DateField(help_text="Date from the last alteration made in this document")
   
    class Meta:
        ordering = ["doc_name", "-doc_tag", "-doc_last_alteration"]

    #def get_absolute_url(self):
    #    return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.doc_name
    
class Group(models.Model):
    doc_group_name = models.CharField(max_length=100, help_text="Give this group of documents a name")

    class Meta:
        ordering = ["doc_group_name"]

    def __str__(self):
        return self.doc_group_name
    
