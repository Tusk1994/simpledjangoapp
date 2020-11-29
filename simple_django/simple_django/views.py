import json
import datetime
import pytz

from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Sum

from client.models import *


def index(request):
    """
    Home page
    """
    return render(request, 'index.html', {})


def line_chart(request):
    """
    Draw line chart
    """
    resp_dict = {
        'chart': {
            'type': 'line',
            'height': str((9 / 16 * 80)) + '%',
        },
        'title': 'Arrival of pay',
        'series': [{
            'data': [
                [
                    # Convert to timestamp for highcharts
                    (p.pay_date - datetime.datetime(1970, 1, 1, tzinfo=pytz.UTC)).total_seconds() * 1000,
                    p.amount
                ]
                for p in Payments.objects.all()
            ],
            'name': "Value of pay",
            'dataLabels': {
                'enabled': 'true',
                'format': '{point.y}'
            },
        }],
        'yAxis': {
            'title': {
                'text': 'Amount'
            }
        },

        'xAxis': {
            'type': 'datetime',

            'accessibility': {
                'rangeDescription': 'Date'
            },
            'title': {
                'text': 'Date'
            }
        },
    }
    return HttpResponse(json.dumps(resp_dict))


def column_chart(request):
    """
    Draw column chart
    """
    resp_dict = {
        'chart': {
            'type': 'column',
            'height': str((9 / 16 * 80)) + '%',
        },
        'title': 'Distribution of pay',
        'series': [{
            'data': [
                {
                    'name': '{0} {1}'.format(p.last_name, p.first_name),
                    # Get sum of payments for each Client
                    'y': p.payments_set.aggregate(Sum('amount'))['amount__sum'],
                }
                for p in Clients.objects.all().prefetch_related('payments_set')
            ],
            'dataLabels': {
                'enabled': 'true',
                'format': '{point.y}'
            },
            'colorByPoint': 'true',
            'name': "Value of pay",
        }],
        'yAxis': {
            'title': {
                'text': 'Amount'
            }
        },

        'xAxis': {
            'type': 'category',
            'title': {
                'text': 'Full name'
            }
        },
    }
    return HttpResponse(json.dumps(resp_dict))
