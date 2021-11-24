from faker import Faker

class Generacion:

    faker = Faker()

    def __init__(self):
        pass

    def generar_nombres(self):
        nombres = self.faker.name()
        return nombres
        
    def generar_correos(self):
        correos = self.faker.email()
        return correos

    def generar_genero(self):
        generos = self.faker.random_element(elements=("female", "male"))
        return generos


    def generar_estados(self):
        estados = self.faker.random_element(elements=("Active", "Inactive"))
        return estados

    def generar_edades(self):
        edades = self.faker.random_int(0,80)
        return edades
