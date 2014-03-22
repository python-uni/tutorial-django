# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from apps.blog import models
from apps.blog import forms


def home(request):
    return render_to_response(
        "blog/home.html",
        context_instance=RequestContext(request)
    )
