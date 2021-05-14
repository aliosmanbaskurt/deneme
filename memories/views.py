from django.shortcuts import render
from memories.models import Memory,Category,Tag
from django.views.generic.list import ListView
from django.shortcuts import get_list_or_404


# Create your views here.

def memo_list (request):
    memory=Memory.objects.all().order_by('date')
    categories =Category.objects.all().order_by('?')[:11]
    tags = Tag.objects.all().order_by('?')[:11]
    context={
    'memory': memory,
    'categories' : categories,
    'tags' : tags
    }
    return render (request, 'memories2.html',context)

def tag_list (request,tag_slug):
    memory=Memory.objects.all().filter(tags__slug=tag_slug)
    categories =Category.objects.all().order_by()[:11]
    tags = Tag.objects.all().order_by()[:11]
    context={
        'memory': memory,
        'categories' : categories,
        'tags' : tags
    }
    return render (request, 'memories2.html',context)

# class MemoriesListView (ListView):
#     model = Memory
#     template_name = 'memories2.html'
#     context_object_name = 'memory'
    

   
    # def get_queryset (self):
    #     return Memory.objects.all()

class MemoriesDetailView(ListView):
    model = Memory
    template_name = 'detail.html'
    context_object_name='memo'

    def get_queryset (self,*args, **kwargs):
        return Memory.objects.get(category__slug=self.kwargs['category_slug'], id=self.kwargs['memo_id'])

# class CategoryView (ListView):
#     model = Category
#     template_name = 'memories2.html'
#     context_object_name = 'categories'
#     queryset= Category.objects.all()

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['memory'] = Memory.objects.all().filter(category__slug= self.kwargs['category_slug'])
#         return context

def category_detail (request,category_slug):
     memory=Memory.objects.all().filter(category__slug=category_slug)
     categories = Category.objects.all().order_by()[:11]
     tags = Tag.objects.all().order_by()[:11]
     context = {
         'memory' : memory,
         'categories' : categories,
         'tags' : tags
     }

     return render (request,'memories2.html',context)

def search (request):
    memory = Memory.objects.all().filter(name__contains=request.GET['search'])
    categories = Category.objects.all().order_by()[:11]
    tags = Tag.objects.all().order_by()[:11]

    context = {
         'memory' : memory,
         'categories' : categories,
         'tags' : tags
     }

    return render (request,'memories2.html',context)