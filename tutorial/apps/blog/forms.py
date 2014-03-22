# -*- coding: utf-8 -*-
from django import forms
from apps.blog import models


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        exclude = ['last_change']
