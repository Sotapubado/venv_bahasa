from pdb import post_mortem
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
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
    pk_url_kwarg = 'id'

class Salon_createView(LoginRequiredMixin, generic.CreateView):
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
        return supre().form_invalid(form)