from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def show_html(request):
    data = MyWatchList.objects.all()
    data_sudah_ditonton = MyWatchList.objects.filter(watched=True).count()
    data_belum_ditonton = MyWatchList.objects.filter(watched=False).count()

    if (data_sudah_ditonton >= data_belum_ditonton):
        message = "Selamat, kamu sudah banyak menonton!"
    else:
        message = "Wah, kamu masih sedikit menonton!"

    context = {
        'list_movie': data,
        'name': 'Syifa Afra Kamila Mumtaz',
        'student_id': 2106707151,
        'message': message
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")