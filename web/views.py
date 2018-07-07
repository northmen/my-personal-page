# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View


class TestView(View):
    def get(self, request):
        # TODO взять что-то из базы
        return render(request, 'web/test.html', {
            'hui1': 'value_hui1',
            'hui2': 'value_hui2',
        })
