from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django import views

from .forms import UrlForm
from .models import ShortUrl


# @csrf_exempt

class IndexView(views.View):

    class_form = UrlForm
    template_name = 'shortener.html'

    def post(self, request):
        form = self.class_form(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            short_url = ShortUrl.objects.create(target=url)
            short_url.save()
            return render(request, self.template_name, {'url': short_url})

    def get(self, request):
            form = self.class_form
            return render(request, self.template_name, {'form': form})


class redirectView(views.View):

    def get(self, request, key):
        target = get_object_or_404(ShortUrl, key=key)
        return HttpResponseRedirect(target.target)