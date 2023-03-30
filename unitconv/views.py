from django.shortcuts import render
from django.http import JsonResponse
from .models import Operator


def convert(request):
    supportedUnits = ['T', 'g', 't_oz', 'kg', 'lb', 'oz']
    if 'value' not in request.GET or 'from' not in request.GET or 'to' not in request.GET:
        response = {'error': 'You must include the from=, to= and value= parameters'}
    else:
        try:
            value = float(request.GET['value'])
            convertFrom = request.GET['from']
            convertTo = request.GET['to']
            if convertFrom in supportedUnits and convertTo in supportedUnits:
                result = doConversion(convertFrom, convertTo, value)
                response = {'value': result, "units": convertTo}
            else:
                response = {'error': 'from= and to= must use one of the supported units'}
        except ValueError:
            response = {'error': 'Value must be a floating point number!'}

    return JsonResponse(response)


def doConversion(c_from, to, value):
    troy = 0
    result = 0
    if c_from == "T":
        troy = Operator.objects.filter(pk=1).get().tonsToTroy * value
    elif c_from == "g":
        troy = Operator.objects.filter(pk=1).get().gramsToTroy * value
    elif c_from == "t_oz":
        troy = Operator.objects.filter(pk=1).get().troyToTroy * value
    elif c_from == "kg":
        troy = Operator.objects.filter(pk=1).get().kiloToTroy * value
    elif c_from == "lb":
        troy = Operator.objects.filter(pk=1).get().poundToTroy * value
    elif c_from == "oz":
        troy = Operator.objects.filter(pk=1).get().ounceToTroy * value
    if to == "T":
        result = troy / Operator.objects.filter(pk=1).get().tonsToTroy
    elif to == "g":
        result = troy / Operator.objects.filter(pk=1).get().gramsToTroy
    elif to == "t_oz":
        result = troy / Operator.objects.filter(pk=1).get().troyToTroy
    elif to == "kg":
        result = troy / Operator.objects.filter(pk=1).get().kiloToTroy
    elif to == "lb":
        result = troy / Operator.objects.filter(pk=1).get().poundToTroy
    elif to == "oz":
        result = troy / Operator.objects.filter(pk=1).get().ounceToTroy
    return result
