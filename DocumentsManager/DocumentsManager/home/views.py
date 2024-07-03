from django.shortcuts import render
from home.models import Document, Group
# Create your views here.

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_docs = Document.objects.all().count()
    num_groups = Group.objects.all().count()

    # The 'all()' is implied by default

    context = {
        'num_docs': num_docs,
        'num_groups': num_groups,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)