from django.shortcuts import render
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def index(request):
    return render(request, "index.html", {})
