from django.contrib import admin
from home.models import Document
# Register your models here.

#admin.site.register(Document)

class DocumentAdmin(admin.ModelAdmin):
   list_display = ["doc_name", "doc_last_alteration"]
   list_filter = ["doc_tag"]
   #fields = ['doc_name','doc_description', ('doc_tag', 'doc_last_alteration')]
   fieldsets = (
      ("Description info",{
         "fields": ("doc_name", "doc_description")
      }),
      ("Localization info",{
         "fields": ("doc_tag", "doc_last_alteration")
      }),
   )

admin.site.register(Document, DocumentAdmin)