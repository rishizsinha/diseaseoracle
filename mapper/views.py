from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader


def index(request):
    # template = loader.get_template("../html/DiseaseOracle.html")
    # return HttpResponse(template.render())
    return render(request, "pingexample.html")

