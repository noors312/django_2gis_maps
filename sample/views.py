from django.views.generic import FormView, DetailView

from sample.forms import SampleForm
from sample.models import SampleModel


class SampleFormView(FormView):
    form_class = SampleForm
    template_name = "sample/index.html"


class SampleDetailView(DetailView):
    model = SampleModel
    template_name = 'sample/index.html'

    def get_object(self, queryset=None):
        obj = self.model.objects.first()
        return self.model.objects.first()
