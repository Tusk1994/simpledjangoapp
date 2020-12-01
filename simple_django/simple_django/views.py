from django.shortcuts import render
from django.db.models import Sum
import pandas as pd
from pandas_highcharts.core import serialize
from pandas_highcharts.core import json_encode

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
    df = pd.DataFrame(Payments.objects.all().values('pay_date', 'amount'))
    hc = serialize(df.set_index('pay_date'), render_to="container", title="Arrival of pay", output_type="dict")

    hc['chart']['type'] = 'line'
    hc['chart']['height'] = str((9 / 16 * 80)) + '%'
    hc['credits'] = {
        'enabled': 'false'
    },

    hc['legend'] = {
        'enabled': 'false'
    },

    hc['yAxis'][0]['title'] = {
        'text': 'Amount',
    }

    hc['xAxis']['type'] = 'datetime'
    hc['xAxis']['accessibility'] = {
        'rangeDescription': 'Date',
    }
    hc['xAxis']['title'] = {
        'text': 'Date',
    }

    hc['series'][0]['name'] = "Value of pay"
    hc['series'][0]['dataLabels'] = {
        'enabled': 'true',
        'format': '{point.y}'
    }

    return render(request, 'graph.html', {"graph": "Highcharts.chart(%s);" % json_encode(hc)})


def column_chart(request):
    """
    Draw column chart
    """

    data_clients = []
    for client in Clients.objects.all().prefetch_related('payments_set'):
        data_clients.append({
            'name': '{0} {1}'.format(client.last_name, client.first_name),
            'y': client.payments_set.aggregate(Sum('amount'))['amount__sum']
        })

    df = pd.DataFrame(data_clients)
    hc = serialize(df.set_index('name'), render_to="container", title="Distribution of pay", output_type="dict")

    hc['chart']['type'] = 'column'
    hc['chart']['height'] = str((9 / 16 * 80)) + '%'
    hc['credits'] = {
        'enabled': 'false'
    },

    hc['legend'] = {
        'enabled': 'false'
    },

    hc['yAxis'][0]['title'] = {
        'text': 'Amount',
    }

    hc['xAxis']['type'] = 'category'
    hc['xAxis']['title'] = {
        'text': 'Full name',
        'title': {
            'text': 'Full name'
        }
    }

    hc['series'][0]['name'] = "Value of pay"
    hc['series'][0]['colorByPoint'] = "true"
    hc['series'][0]['dataLabels'] = {
        'enabled': 'true',
        'format': '{point.y}'
    }

    return render(request, 'graph.html', {"graph": "Highcharts.chart(%s);" % json_encode(hc)})
