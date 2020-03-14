from django.db.models import Q
from django.urls import reverse
from django.utils.http import urlencode
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from webapp.forms import SimpleSearchForm
from webapp.models import File


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'files'
    model = File
    ordering = '-creation_date'
    paginate_by = 10
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(name__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

class FileDetailView(DetailView):
    template_name = 'file_detail.html'
    pk_url_kwarg = 'pk'
    model = File

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['form'] = TaskForm()
    #     comments = context['photo'].comments.order_by('-created_at')
    #     self.paginate_comments_to_context(comments, context)
    #     context['user'] = self.request.user
    #     return context


class FileCreateView(CreateView):
    template_name = 'file_create.html'
    model = File
    # form_class = PhotoForm
    fields = ['name', 'file']

    def form_valid(self, form):
        if str(self.request.user) != 'AnonymousUser':
            form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:index')