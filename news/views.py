from django.shortcuts import render, redirect
from .models import Arcticles
from .forms import ArcticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.

# Вывод записей из БД
def news_home(request):
    news = Arcticles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

# динамически изменяемые страницы: развернутые новости
class NewsDatailView(DetailView):
    model = Arcticles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

# редактирование записи
class NewsUpdateView(UpdateView):
    model = Arcticles
    template_name = 'news/create.html'

    form_class = ArcticlesForm

# удаление записи
class NewsDeleteView(DeleteView):
    model = Arcticles
    success_url = '/news' # переадресация после удаления
    template_name = 'news/news-delete.html'

# форма для добавления записей в БД
def create(request):
    error = ''
    if request.method == 'POST':
        form = ArcticlesForm(request.POST) # Данные заполненные в форме
        if form.is_valid(): # метод: проверка корректно ли заполнены данные
            form.save() # сохраняем данные
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = ArcticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)