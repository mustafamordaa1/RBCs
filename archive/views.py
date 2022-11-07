from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.template.defaulttags import register

@register.filter
def get_range(value):
    return range(value)

@register.filter
def get_url(value):
    d = value.split("/")
    dlink = "https://drive.google.com/uc?id=" + d[-2] + "&export=download"
    return dlink
# Create your views here.

def main(request):
    books = Book.objects.all()
    year2 = ['تشريح رأس و عنق', 'كيمياء حيوية', "بيولوجيا جزيئية","علم نفس سلوكي","تشريح أطراف", "علم الجنين", "النسج"]
    year3 = ['تشريح', 'كيمياء حيوية', "بيولوجيا جزيئية","علم نفس","انكليزي"]
    year4 = ['تشريح', 'كيمياء حيوية', "بيولوجيا جزيئية","علم نفس","انكليزي"]
    year5 = ['تشريح', 'كيمياء حيوية', "بيولوجيا جزيئية","علم نفس","انكليزي"]
    year6 = []
    context = {
        'books':books,
        'year2':year2,
        'year3':year3,
        'year4':year4,
        'year5':year5,
        'year6':year6,
    }
    return render(request, 'main.html', context)

def lectures(request, year, subject):
    lecture = Book.objects.all().filter(year=year, subject=subject)
    context = {
        'lectures': lecture,
        'subject':subject,
    }
    return render(request, 'lectures.html', context)

