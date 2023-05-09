from typing import Dict, Any


class AnalizadorEventos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_eventos(self) -> Dict[str, Any]:
        total_eventos = 0
        eventos_por_tipo = {}
        eventos_por_servidor = {}

        with open(self.nombre_archivo, 'r') as file:
            while True:
                linea_fecha = file.readline()
                if not linea_fecha:
                    break

                total_eventos += 1

                file.readline()  # Salta la línea de la hora

                linea_servidor = file.readline().strip()
                nombre_servidor = linea_servidor.split(': ')[1]
                if nombre_servidor in eventos_por_servidor:
                    eventos_por_servidor[nombre_servidor] += 1
                else:
                    eventos_por_servidor[nombre_servidor] = 1

                linea_tipo_evento = file.readline().strip()
                tipo_evento = linea_tipo_evento.split(': ')[1]
                if tipo_evento in eventos_por_tipo:
                    eventos_por_tipo[tipo_evento] += 1
                else:
                    eventos_por_tipo[tipo_evento] = 1

                file.readline()  # Salta la línea de la descripción
                file.readline()  # Salta la línea en blanco entre registros

        return {
            'total_eventos': total_eventos,
            'eventos_por_tipo': eventos_por_tipo,
            'eventos_por_servidor': eventos_por_servidor
        }


# Ejemplo de uso:
analizador = AnalizadorEventos('eventos.txt')
resultados = analizador.procesar_eventos()
print(resultados)
