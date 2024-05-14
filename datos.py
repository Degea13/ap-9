from typing import Tuple

class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        with open(self.nombre_archivo, 'r') as file:
            # Inicializar variables para calcular promedios
            total_temp = 0
            total_hum = 0
            total_pres = 0
            total_vel_viento = 0
            num_records = 0

            # Inicializar variables para calcular dirección predominante del viento
            directions = {'N': 0, 'NNE': 0, 'NE': 0, 'ENE': 0, 'E': 0, 'ESE': 0, 'SE': 0, 'SSE': 0, 'S': 0,
                          'SSW': 0, 'SW': 0, 'WSW': 0, 'W': 0, 'WNW': 0, 'NW': 0, 'NNW': 0}

            for line in file:
                if line.startswith('Temperatura'):
                    _, temp = line.split(':')
                    total_temp += float(temp.strip())
                elif line.startswith('Humedad'):
                    _, hum = line.split(':')
                    total_hum += float(hum.strip())
                elif line.startswith('Presion'):
                    _, pres = line.split(':')
                    total_pres += float(pres.strip())
                elif line.startswith('Viento'):
                    _, viento = line.split(':')
                    vel, dir_viento = viento.strip().split(',')
                    total_vel_viento += float(vel)
                    # Actualizar conteo de direcciones
                    directions[dir_viento] += 1

                num_records += 1

            # Calcular promedios
            avg_temp = total_temp / num_records
            avg_hum = total_hum / num_records
            avg_pres = total_pres / num_records
            avg_vel_viento = total_vel_viento / num_records

            # Calcular dirección predominante del viento
            max_dir = max(directions, key=directions.get)
            return avg_temp, avg_hum, avg_pres, avg_vel_viento, max_dir

# Ejemplo de uso
datos = DatosMeteorologicos('datos.txt')
avg_temp, avg_hum, avg_pres, avg_vel_viento, max_dir = datos.procesar_datos()
print(f'Temperatura promedio: {avg_temp}')
print(f'Humedad promedio: {avg_hum}')
print(f'Presión promedio: {avg_pres}')
print(f'Velocidad promedio del viento: {avg_vel_viento}')
print(f'Dirección predominante del viento: {max_dir}')
