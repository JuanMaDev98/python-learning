# Función para convertir entre las diferentes notaciones de temperatura
def convert_temperature(value, input_scale, output_scale):
    if input_scale == 'C':
        if output_scale == 'F':
            return value * 1.8 + 32
        elif output_scale == 'K':
            return value + 273.15
        else:
            return value
    elif input_scale == 'F':
        if output_scale == 'C':
            return (value - 32) / 1.8
        elif output_scale == 'K':
            return (value + 459.67) * 5 / 9
        else:
            return value
    elif input_scale == 'K':
        if output_scale == 'C':
            return value - 273.15
        elif output_scale == 'F':
            return value * 9 / 5 - 459.67
        else:
            return value
    else:
        return value