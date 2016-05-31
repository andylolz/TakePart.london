import requests

from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse

from register.models import RegisteredPerson, Ward, Borough

from .forms import PostcodeLookupForm


class BaseDataView(object):

    def get_data_for_postcode(self, postcode):
        data = {}
        area_info = RegisteredPerson.objects.filter(postcode=postcode).first()
        if area_info:
            data['ward'] = area_info.ward
            data['borough'] = area_info.borough
        else:
            req = requests.get(
                "http://mapit.democracyclub.org.uk/postcode/{}".format(
                    postcode
                ))
            for area_id, area in req.json()['areas'].items():
                if area['type'] == "LBW":
                    data['ward'] = Ward.objects.get(gss=area['codes']['gss'])
                    data['borough'] = data['ward'].borough
        # TODO Postcode not in London
        return data


class HomeView(FormView):
    template_name = "home.html"
    form_class = PostcodeLookupForm

    def get_initial(self):
        initial = self.initial.copy()
        if 'invalid_postcode' in self.request.GET:
            initial['postcode'] = self.request.GET.get('postcode')
        return initial

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'autofocus': True})
        return kwargs

    def form_valid(self, form):
        postcode = form.cleaned_data['postcode']
        self.success_url = reverse(
            'postcode_view',
            kwargs={'postcode': postcode}
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_content_block'] = True
        return context


class PostcodeView(BaseDataView, TemplateView):
    template_name = "postcode.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        postcode = self.request.GET.get('postcode', 'SE22 8DJ')
        context['area_info'] = self.get_data_for_postcode(postcode)
        return context
