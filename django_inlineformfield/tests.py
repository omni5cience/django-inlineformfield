#-*- coding: utf-8 -*-
# pylint: disable=C0111, C0103, R0904

from django.test import TestCase
from django.db import models
from django import forms

from django_inlineformfield.forms.fields import InlineFormField


class Blog(models.Model):
    active = models.BooleanField()


class BlogPost(models.Model):
    active = models.BooleanField()
    blog = models.ForeignKey(Blog)

class ChildForm(forms.Form):
    active = forms.BooleanField(default=False)

    def clean_active(self):
        if not self.cleaned_data['active']:
            raise forms.ValidationError("active must be true")
        return self.cleaned_data['active']


class ParentForm(forms.Form):
    active = forms.BooleanField(default=False)
    children = InlineFormField(ChildForm)



class InlineFormFieldTest(TestCase):
    def setUp(self):
        self.form = ParentForm()

    def test_parent_form_validates_children(self):
        self.form.is_valid()
