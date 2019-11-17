from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Book
# Create your views here.


def index(request):
    return HttpResponse("Hello world!!")


def detail(request):
    book_list = Book.objects.order_by('-pub_date')[:5]
    context = {'book_list': book_list}
    return render(request, 'detail.html', context)


def addBook(request):
    if request.method == 'POST':
        name = request.POST['name']
        author = request.POST['author']
        pub_house = request.POST['pub_house']

    from django.utils import timezone
    book = Book(name=name, author=author, pub_house=pub_house, pub_date=timezone.now())
    book.save()

    return HttpResponseRedirect(reverse('lib:detail'))


def delBook(request, book_id):
    Book.objects.filter(id=book_id).delete()
    return HttpResponseRedirect(reverse('lib:detail'))
