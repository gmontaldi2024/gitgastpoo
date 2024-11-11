"""
Nombre y apellido: Gaston Montaldi

Crear un programa de python que permita guardar un registro de alumnos en archivo de texto utilizando el POO.

Estrucutrar correctamente la clase alumno:

Esta podria tener, ademas de los parametros que alamacenaran la infomacion del alumno (nombre, apellido, notas, cantidad de faltas, cantidad de amonestaciones, dirección), metodos que le permitan ingresar una nueva nota, asignar una falta, asignar una amonestacion, cambiar domicilio (puede considerar agregar otros datos relevantes) .

Subir el repositorio en github y adjuntar el link

"""

class Alumnos:
    def __init__(self,nombre,apellido,direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.cant_faltas = 0
        self.cant_amonestaciones = 0
        self.notas = []
        self.direccion = direccion

    def faltas (self):
        self.cant_faltas +=1

    def amonestaciones (self):
        self.cant_amonestaciones +=1

    def nota (self,nota):
        self.notas.append(nota)

    def __str__(self):
        return f"Alumno: {self.nombre} {self.apellido}, Faltas: {self.cant_faltas}, Amonestaciones: {self.cant_amonestaciones}, Notas: {self.notas}, Dirección: {self.direccion}"

alumno1 = Alumnos("Gaston","Montaldi","Los Ceibos 350 13")
alumno1.faltas()
alumno1.amonestaciones()
alumno1.nota(9)
print(alumno1)
