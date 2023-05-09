from typing import Dict, Any

class AnalizadorEventos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_eventos(self) -> Dict[str, Any]:
        eventos_por_tipo = {}
        eventos_por_servidor = {}
        total_eventos = 0

        with open(self.nombre_archivo, "r", encoding="utf-8") as archivo:
            while True:
                fecha = archivo.readline().strip()
                if not fecha:
                    break
                hora = archivo.readline().strip()
                servidor_linea = archivo.readline().strip()
                servidor = servidor_linea.split(": ")[1]
                tipo_evento_linea = archivo.readline().strip()
                tipo_evento = tipo_evento_linea.split(": ")[1]
                descripcion = archivo.readline().strip()

                archivo.readline()  # Lee la línea en blanco entre registros

                total_eventos += 1

                if tipo_evento in eventos_por_tipo:
                    eventos_por_tipo[tipo_evento] += 1
                else:
                    eventos_por_tipo[tipo_evento] = 1

                if servidor in eventos_por_servidor:
                    eventos_por_servidor[servidor] += 1
                else:
                    eventos_por_servidor[servidor] = 1

        estadisticas = {
            "total_eventos": total_eventos,
            "eventos_por_tipo": eventos_por_tipo,
            "eventos_por_servidor": eventos_por_servidor,
        }
        return estadisticas


# Uso de la clase:
nombre_archivo = "eventos.txt"
analizador = AnalizadorEventos(nombre_archivo)
estadisticas = analizador.procesar_eventos()
print(estadisticas)
