from django.shortcuts import render
from main.func.counter import counters
# Create your views here.
def length(request):
    result=None
    selected_from=None
    selected_to=None
    if request.method == 'POST':
        from_unit = request.POST.get('from_unit')
        from_value = request.POST.get('from_value')
        to_unit = request.POST.get('to_unit')
        selected_from=from_unit
        selected_to=to_unit
        if not from_value:
            result = 'Please input value'
        else:    
            result=counters(from_unit,from_value,to_unit)
    
    context={'items':["millimeter","centimeter",
                      "meter","kilometer","inch", "foot", "yard", "mile"],'result':result,'status':'Length','selected_from':selected_from,'selected_to':selected_to}
    return render(request,'main/base.html',context)
def weight(request):
    result=None
    selected_from=None
    selected_to=None
    if request.method == 'POST':
        from_unit = request.POST.get('from_unit')
        from_value = request.POST.get('from_value')
        to_unit = request.POST.get('to_unit')
        selected_from=from_unit
        selected_to=to_unit
        if not from_value:
            result = 'Please input value'
        else:    
            result=counters(from_unit,from_value,to_unit)
    
    context={'items':['milligram', 'gram', 'kilogram', 'ounce', 'pound'],'result':result,'status':'Weight','selected_from':selected_from,'selected_to':selected_to}
    return render(request,'main/base.html',context)
def temperature(request):
    result=None
    selected_from=None
    selected_to=None
    if request.method == 'POST':
        from_unit = request.POST.get('from_unit')
        from_value = request.POST.get('from_value')
        to_unit = request.POST.get('to_unit')
        selected_from=from_unit
        selected_to=to_unit
        if not from_value:
            result = 'Please input value'
        else:    
            result=counters(from_unit,from_value,to_unit)
    context={'items':['Celsius', 'Fahrenheit', 'Kelvin'],'result':result,'status':'Temperature','selected_from':selected_from,'selected_to':selected_to}
    return render(request,'main/base.html',context)