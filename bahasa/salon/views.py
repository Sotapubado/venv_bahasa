from pdb import post_mortem
from re import template
from django.views import generic
from .forms import SalonCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
import salon

from salon.models import Salon  #Loginしてないとアクセスできない 

class Salon_indexView(generic.TemplateView):
    template_name = "salon_index.html"

class Salon_listView(LoginRequiredMixin, generic.ListView):
    model = Salon
    template_name = 'salon_list.html'
    pagenate_by=2

    def  get_queryset(self):
        salons = Salon.objects.filter(user=self.request.user).order_by('-created_at')
        return salons

class Salon_DetailView(LoginRequiredMixin, generic.DetailView):
    model = Salon
    template_name = 'salon_detail.html'
    slug_field = "user"
    slug_url_kwarg = "user"
   

class Salon_CreateView(LoginRequiredMixin, generic.CreateView):
    model = salon
    template_name = 'salon_create.html'
    form_class = SalonCreateForm
    success_url = reverse_lazy('salon:salon_list')

    def form_valid(self, form):
        salon = form.save(commit=False)
        salon.user = self.request.user
        salon.save()
        messages.success(self.request, 'Creste post.')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, "failed to create post.")
        return super().form_invalid(form)

class Salon_EditView(LoginRequiredMixin, generic.UpdateView):
    model = Salon
    template_name = 'salon_edit.html'
    form_class = SalonCreateForm

    def get_success_url(self):
        return reverse_lazy('salon:salon_detail', kwargs={'pk':self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, 'Update Your Post')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Failed to update post')
        return super().form_invalid(form)

class Salon_DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Salon
    template_name = 'salon_delete.html'
    success_url = reverse_lazy('salon:salon_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Delete Post")
        return super().delete(request, *args, **kwargs)