from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    items_catalog = CatalogItem.objects.all()
    context = {
        'catalog_items' : items_catalog,
        'name' : 'Syifa Afra Kamila Mumtaz',
        'student_id' : '2106707151',
    }
    return render(request, "katalog.html", context)

