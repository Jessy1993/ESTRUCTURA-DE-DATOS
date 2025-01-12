class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}"


class AgendaTelefonica:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono):
        self.contactos.append(Contacto(nombre, telefono))

    def mostrar_contactos(self):
        for contacto in self.contactos:
            print(contacto)

    def buscar_contacto(self, nombre):
        resultados = [c for c in self.contactos if nombre.lower() in c.nombre.lower()]
        if resultados:
            for contacto in resultados:
                print(contacto)
        else:
            print("No se encontraron contactos.")

# Ejemplo de uso
agenda = AgendaTelefonica()
agenda.agregar_contacto("Juan Perez", "0958997835")
agenda.agregar_contacto("Maria Lopez", "0987272275")
agenda.mostrar_contactos()
agenda.buscar_contacto("Maria")
