from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, FormView


from .forms import ContactForm


class HomeView(TemplateView):
    """
    View for home page
    """
    template_name = 'core/home.html'


class ClothersView(TemplateView):
    """
    View for clothers page
    """
    template_name = 'core/clojures.html'


class ContactsView(FormView):
    """
    View for contacts page
    """
    template_name = 'core/contacts.html'
    form_class = ContactForm
    success_url = reverse_lazy('core:contacts')

    def form_valid(self, form):
        form.send_mail()
        return super(ContactsView, self).form_valid(form)
