import wx
import requests
from components import Ventana
from components.generacion import Generacion


class Usuarios:

    __url_api = 'https://gorest.co.in/public/v1/users?access-token=55219badb97cd1f82835b0421de3962f326f9705d93f45fdf99f4519c2f6ec65'
    __endpoint = 'users'
    __ventana = None
    pagina_actual = 1


    def __init__(self, titulo):
        data = self.crear_usuarios()
        self.__iniciar_ventana(titulo,data)
        pass

    def __iniciar_ventana(self, titulo, data):
        ventana = Ventana(titulo)
        ventana.titulo("Cargar usuarios Random")
        ventana.botones("Cargar", 350, 120)
        ventana.cargar_tabla(data, 50, 220)
        ventana.iniciar()

    def __consultar_usuarios(self):
        url = '{}/{}?page={}'.format(self.__url_api, self.__endpoint, self.pagina_actual)
        r = requests.get(url)
        usuarios_request = r.json()
        self.usuarios = usuarios_request['data']
        self.paginacion = usuarios_request['pagination'] if 'pagination' in usuarios_request else {}

    def crear_usuarios(self):
        usuarios = Generacion()
        count_user_add = 0
        usuariosList = []

        while count_user_add < 10:

            if(usuarios.generar_edades() > 18):

                usuario_add = {
                    'name': usuarios.generar_nombres(),
                    'gender': usuarios.generar_genero(),
                    'email': usuarios.generar_correos(),
                    'status': usuarios.generar_estados()
                    }
                
                usuariosList.append(usuario_add)

                count_user_add +=1
                print(usuario_add)
                apiRequest = requests.post(self.__url_api, data = usuario_add)
                print(apiRequest)
        pass
        
        return usuariosList
