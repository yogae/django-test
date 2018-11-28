from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from books.models import Book, Author, Publisher

class BooksModelView(TemplateView):
    # 필수적으로 template_name을 넣어서 사용
    template_name = 'books/index.html'

    # TemplateView경우 넘겨줄 컨텍스트 변수가 있는 경우 get_context_data() 메소드를 오버라이딩해서 정의해준다.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['Book', 'Author', 'Publisher']
        return context

class BookList(ListView):
    model = Book

class AuthorList(ListView):
    model = Author

class PublisherList(ListView):
    model = Publisher

class BookDetail(DetailView):
    model = Book

class AuthorDetail(DetailView):
    model = Author

class PublisherDetail(DetailView):
    model = Publisher


