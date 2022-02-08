from django.shortcuts import render
from django.views import generic

from accounts.forms import AccountForm
from .models import Account

from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

class AccountView(generic.CreateView):
    model = Account
    template_name = "accounts_signup.html"
    form = AccountForm
    success_url = reverse_lazy('accounts:accounts_signup')

    def form_valid(self, form):
        account = form.save(commit=False)
        account.user = self.request.user
        account.save()
        messages.success(self.request, 'Creste post.')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, "failed to create post.")
        return super().form_invalid(form)
