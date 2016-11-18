from django.shortcuts import render

from .forms import contactForm

# Responsible for displaying home view


def home(request):
    context = locals()
    template = 'home.html'
    return render(request, template, context)


# Display page to add new contact
def add(request):
    form = contactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data['email'])
    context = locals()
    template = 'add.html'
    return render(request, template, context)


# Display list of contacts saved
def list(request):
    context = locals()
    template = 'list.html'
    return render(request, template, context)
