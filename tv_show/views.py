from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic

class TVShowListView(generic.ListView):
    model = models.TVShow
    template_name = 'tv_shows/tv_shows_list.html'
    context_object_name = 'tvshows'

    def get_queryset(self):
        tv_shows = self.model.objects.all()
        for tv_show in tv_shows:
            tv_show.review_count = tv_show.tvshow_reviews.count()
        return tv_shows


class TVShowDetailView(generic.DetailView):
    template_name = 'tv_shows/tv_show_detail.html'
    context_object_name = 'tvshow_id'

    def get_object(self, **kwargs):
        tvshow_id = self.kwargs.get('id')
        return get_object_or_404(models.TVShow, id=tvshow_id)


class TVShowCreateView(generic.CreateView):
    template_name = 'tv_shows/crud/create_tvshow.html'
    form_class = forms.TVShowForm
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(TVShowCreateView, self).form_valid(form=form)


class DeleteTVShowView(generic.DeleteView):
    template_name = 'tv_shows/crud/confirm_delete.html'
    success_url = '/'

    def get_object(self, **kwargs):
        tvshow_id = self.kwargs.get('id')
        return get_object_or_404(models.TVShow, id=tvshow_id)


class EditTVShowView(generic.UpdateView):
    template_name = 'tv_shows/crud/edit_tvshow.html'
    form_class = forms.TVShowForm
    success_url = '/'
    queryset = models.TVShow.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(EditTVShowView, self).form_valid(form=form)

    def get_object(self, **kwargs):
        tvshow_id = self.kwargs.get('id')
        return get_object_or_404(models.TVShow, id=tvshow_id)


def add_review_view(request):
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('The review was successfully added <a href="/">Main page</a>')
    else:
        form = forms.ReviewForm()
        return render(request, 'tv_shows/add_review.html', {'form': form})


class SearchTVShowView(generic.ListView):
    template_name = 'tv_shows/tv_shows_list.html'
    context_object_name = 'tvshows'
    paginate_by = '5'

    def get_queryset(self):
        return models.TVShow.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context