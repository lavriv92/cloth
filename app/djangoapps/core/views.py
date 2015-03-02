from django.shortcuts import render_to_response


def home(request):
    return render_to_response('core/home.html')


def contacts(request):
    return render_to_response('core/contacts.html')


def clojures(request):
    return render_to_response('core/clojures.html')
