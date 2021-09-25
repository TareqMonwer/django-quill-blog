from django_quill.fields import QuillField
from django.db import models


class Core(models.Model):
    content = QuillField()