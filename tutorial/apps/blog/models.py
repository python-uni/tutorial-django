# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from apps.blog import managers
import datetime
from django.utils.timezone import utc


class Post(models.Model):
    # Relations
    user = models.ForeignKey(
        User,
        related_name="posts",
        verbose_name=_("user"),
    )
    # Attributes
    name = models.CharField(max_length=130)
    last_change = models.DateField(verbose_name=_("last change"))
    description = models.TextField(
        max_length=140,
        blank=True,
        verbose_name=_("description"),
        help_text=_("Enter the post description (optional)"),
    )
    content = models.TextField(
        verbose_name=_("description"),
        help_text=_("Enter the post"),
    )
    # Manager
    objects = managers.PostManager()

    # Functions
    def __unicode__(self):
        return _("Post %s") % self.name

    def save(self, *args, **kwargs):
        self.last_change = datetime.datetime.utcnow().replace(tzinfo=utc)
        super(Post, self).save(args, kwargs)

    # Meta
    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ["-id"]
