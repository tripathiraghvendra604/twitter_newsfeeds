from django.views.generic import FormView, ListView, TemplateView
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from .forms import CountryForm
from .models import Country, News


class CountryFormView(FormView):
    form_class = CountryForm
    template_name = 'newsfeeds/index.html'

    def form_valid(self, form):
        data = form.cleaned_data
        country = Country.objects.filter(code=data['country']).first()
        return redirect('/news/' + country.name.lower())


class CountryNewsView(ListView):
    template_name = 'newsfeeds/news.html'
    model = News

    def get_queryset(self):
        country = self.kwargs['country']
        all_news = News.objects.filter(
            country=Country.objects.filter(
                name=country
            ).first()
        ).all()
        sorted_news = sorted(all_news, key=lambda x: x.time)
        query_set = sorted_news[: 10]
        return query_set


class ArticleView(TemplateView):
    template_name = 'newsfeeds/article.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        print(self.kwargs['country'], ': ', self.kwargs['article'])
        context['article'] = News.objects.filter(id=self.kwargs['article']).first()
        print(context['article'].heading)
        return context