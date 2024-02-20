from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from . import models, forms, parser_imdb


class ParserFormView(generic.FormView):
    template_name = 'parser_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('Succesfuly get data')
        else:
            return super(ParserFormView).post(request, *args, **kwargs)
