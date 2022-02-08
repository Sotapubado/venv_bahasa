import logging

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from after.models import After

from .forms import AfterInquiryForm

logger = logging.getLogger(__name__)


class After_indexViews(generic.TemplateView):
    template_name = "after_index.html"

    
class After_MypageViews(LoginRequiredMixin, generic.ListView):
    model = After
    template_name = "after_mypage.html"

    def get_queryset(self):
        return After.objects.filter(user=self.request.user)
    

class After_InquiryView(generic.FormView):
    template_name = "after_inquiry.html"
    form_class = AfterInquiryForm
    success_url = reverse_lazy('after:after_inquiry')

    def form_valid(self, form):
        form.send_email()
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)


