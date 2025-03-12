length = ['millimeter', 'centimeter', 'meter', 'kilometer', 'inch', 'foot', 'yard', 'mile']
weight= ['milligram', 'gram', 'kilogram', 'ounce', 'pound']
temperature= ['Celsius', 'Fahrenheit', 'Kelvin']
length_factors = {
    'millimeter': 0.001,
    'centimeter': 0.01,
    'meter': 1,
    'kilometer': 1000,
    'inch': 0.0254,
    'foot': 0.3048,
    'yard': 0.9144,
    'mile': 1609.34
}
weight_factors={
    'milligram': 0.001,
    'gram': 1,
    'kilogram': 1000,
    'ounce': 28.3495,
    'pound': 453.592
}

temperature_factors={
    'Celsius': 1,
    'Fahrenheit': 1.8,
    'Kelvin': 1
}

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return int(value) * temperature_factors['Fahrenheit'] + 32
        elif to_unit == 'Kelvin':
            return int(value) + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (int(value) - 32) / temperature_factors['Fahrenheit']
        elif to_unit == 'Kelvin':
            return (int(value) - 32) / temperature_factors['Fahrenheit'] + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return int(value) - 273.15
        elif to_unit == 'Fahrenheit':
            return (int(value) - 273.15) * temperature_factors['Fahrenheit'] + 32

    return int(value)

def counters(from_unit, from_value,to_unit):
    if from_unit in length:
        result=int(from_value)*length_factors[f"{from_unit}"]
        result = result/ length_factors[f"{to_unit}"]
        return (f"{result:.2f}")
    elif from_unit in weight:
        result=int(from_value)*weight_factors[f"{from_unit}"]
        result=result/weight_factors[f"{to_unit}"]
        return (f"{result:.2f}")
    else:
        result=convert_temperature(from_value,from_unit,to_unit)
        return (f"{result:.2f}")