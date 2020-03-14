from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from webapp.models import File


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'files'
    model = File
    ordering = '-creation_date'
    # paginate_by = 10
    # paginate_orphans = 1

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