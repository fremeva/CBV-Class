# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

from cbv.forms import ExampleForm, UserModelForm
from cbv.models import UserProxy


class CBVTemplateViewExample(TemplateView):
    template_name = 'template.html'

class CBVListUsers(ListView):
    template_name = 'template.html'
    queryset = UserProxy.objects.all()
    paginate_by = 2

    def get_queryset(self):
        user = self.request.user
        qs = super(CBVListUsers, self).get_queryset()

        if user.is_superuser:
            return qs
        else:
            return qs.non_superuser()

    def get_context_data(self, **kwargs):
        context = super(CBVListUsers, self).get_context_data(**kwargs)
        print(context)
        context.update({
            'user': self.request.user
        })
        return context

class CBVDetailView(DetailView):
    model = User
    template_name = 'detail.html'
    context_object_name = 'obj'
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        user = super(CBVDetailView, self).get_object(queryset)
        if user.is_superuser and not self.request.user.is_superuser:
            raise Http404()

        return user

class CBVFormView(FormView):
    form_class = UserModelForm
    template_name = 'form.html'
    success_url = '.'

    def form_valid(self, form):
        return super(CBVFormView, self).form_valid(form)

    def get_form(self, form_class=None):
        try:
            return super(CBVFormView, self).get_form(form_class)
        except Exception as e:
            raise Http404(e.message)

    def get_form_kwargs(self):
        kwargs = super(CBVFormView, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class CBVCreateView(CreateView):
    template_name = 'create.html'
    model = User
    success_url = '.'
    fields = ('username', 'password', 'email', 'first_name', 'last_name')

class CBVUpdateView(UpdateView):
    template_name = 'update.html'
    model = User
    success_url = '.'
    fields = ('username', 'email', 'first_name', 'last_name')

class CBVDeleteView(DeleteView):
    template_name = 'delete.html'
    model = User
    success_url = reverse_lazy('list', args=())