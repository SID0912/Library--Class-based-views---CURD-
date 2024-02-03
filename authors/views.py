from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Author
from django.http import HttpResponseRedirect

class AuthorListView(ListView):
    model = Author
    context_object_name = "authors"
    template_name = "author_list.html"


class AuthorCreateView(CreateView):
    model = Author
    fields = "__all__"
    template_name = "author_create.html"

    def get_success_url(self):
        return "/"

    
class AuthorUpdateView(UpdateView):
    model = Author
    fields = "__all__"
    template_name = "author_update.html"

    def get_success_url(self):
        return "/"
    


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = "author_delete.html"
    context_object_name = "authorName"

    def get_success_url(self):
        return "/"
    
