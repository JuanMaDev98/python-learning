#Creando una aplicación que convierta temperatura de Celsius a Fahrenheit a Kelvin, etc
import tempConvert as TC
#Creando un diccionario para definir las escalas (Totalmente innecesario XD, lo pusieron en el tutorial por algún  motivo)
TEMPERATURE_SCALES = {
    "Celsius": "C",
    "Fahrenheit": "F",
    "Kelvin": "K"
}

            
while True:
    # Recoger un input del usuario
    print('Enter the input temperature value:')
    value = float(input())
    print('Enter the input temperature scale (C, F, or K):')
    input_scale = input().upper()
    print('Enter the output temperature scale (C, F, or K):')
    output_scale = input().upper()

    # Convertir la temperatura y mostrar el resultado
    result = TC.convert_temperature(value, input_scale, output_scale)
    print(f'{value} {input_scale} = {result} {output_scale}')

    # preguntar al usuario si continuar o seguir
    print('Enter q to quit, or any other key to continue:')
    choice = input()
    if choice.lower() == 'q':
        break


































