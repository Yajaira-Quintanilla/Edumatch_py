from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

Window.size = (400, 600)
 
backgroundColor = (0.68, 0.83, 0.95, 1)
textColor = (0, 0, 0, 1)
MainButonColor = (0.3, 0.55, 0.75, 1)
AlertButonColor = (0.95, 0.6, 0.2, 1)
SecondButonColor = (0.95, 0.6, 0.2, 1)
 
usuarios = {
    "Lisseth": "2008",
    "user": "abcd"
    "claudia": "2009"
}
 
def redondear_boton(boton, color):
    with boton.canvas.before:
        Color(*color)
        boton.bg_rect = RoundedRectangle(size=boton.size, pos=boton.pos, radius=[15])
    boton.bind(size=lambda *x: setattr(boton.bg_rect, 'size', boton.size))
    boton.bind(pos=lambda *x: setattr(boton.bg_rect, 'pos', boton.pos))
    boton.background_normal = ''
    boton.background_down = ''
    boton.background_color = (0, 0, 0, 0)
 
class BienvenidaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(*backgroundColor)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)
 
        layout = BoxLayout(orientation='vertical', spacing=40, padding=60)
 
        try:
            layout.add_widget(Image(source='shared image.jpg', size_hint=(1.5, 1), allow_stretch=True))
        except:
            layout.add_widget(Label(text="(Logo)", size_hint=(1, 0.6), color=textColor))
 
        layout.add_widget(Label(text="¡Bienvenidos!", font_size=30, size_hint=(1, 0.17), color=(0, 0, 0, 1)))
 
        btn_ingresar = Button(text="Ingresar", size_hint=(1, 0.15), font_size=25, color=textColor)
        redondear_boton(btn_ingresar, MainButonColor)
        btn_ingresar.bind(on_press=self.ir_a_login)
 
        layout.add_widget(btn_ingresar)
        self.add_widget(layout)
 
    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
 
    def ir_a_login(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = 'login'
 
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
 
        with self.canvas.before:
            Color(*backgroundColor)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)
 
        self.layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        self.layout.add_widget(Label(text="Iniciar sesión", font_size=26, size_hint=(1, 0.2), color=textColor))
 
        self.usuario = TextInput(hint_text="Usuario", multiline=False, size_hint=(1, 0.1), font_size=18,
                                 foreground_color=textColor, background_color=(0.9, 0.9, 0.9, 1),
                                 cursor_color=textColor)
        self.clave = TextInput(hint_text="Contraseña", password=True, multiline=False, size_hint=(1, 0.1),
                               font_size=18, foreground_color=textColor, background_color=(0.9, 0.9, 0.9, 1),
                               cursor_color=textColor)
 
        self.layout.add_widget(self.usuario)
        self.layout.add_widget(self.clave)
 
        btn_ingresar = Button(text="Ingresar", size_hint=(1, 0.15), font_size=20, color=textColor)
        redondear_boton(btn_ingresar, MainButonColor)
        btn_ingresar.bind(on_press=self.validar_login)
 
        btn_registrar = Button(text="Registrar", size_hint=(1, 0.15), font_size=20, color=textColor)
        redondear_boton(btn_registrar, MainButonColor)
        btn_registrar.bind(on_press=self.ir_registrar)
 
        btn_volver = Button(text="Volver", size_hint=(1, 0.15), font_size=20, color=textColor)
        redondear_boton(btn_volver, SecondButonColor)
        btn_volver.bind(on_press=self.volver)
 
        self.layout.add_widget(btn_ingresar)
        self.layout.add_widget(btn_registrar)
        self.layout.add_widget(btn_volver)
 
        self.add_widget(self.layout)
 
    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
 
    def validar_login(self, instance):
        user = self.usuario.text.strip()
        pwd = self.clave.text.strip()
        if user in usuarios and usuarios[user] == pwd:
            self.manager.get_screen('usuario').usuario = user
            self.manager.transition.direction = 'left'
            self.manager.current = 'usuario'
            self.usuario.text = ''
            self.clave.text = ''
        else:
            popup = Popup(title="Error",
                          content=Label(text="La contraseña es incorrecta, verifique que esta correctamente escrita.", color=(1, 1, 1, 1)),
                          size_hint=(0.6, 0.3))
            popup.open()
 
    def volver(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'bienvenida'
 
    def ir_registrar(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = 'registrar'
 
class RegistrarScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*backgroundColor)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)
 
        self.layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        self.layout.add_widget(Label(text="Registrar", font_size=24, color=textColor))
 
        # Campo: user's name
        self.new_usuario = TextInput(hint_text="Nuevo usuario", multiline=False, size_hint=(1, 0.2), font_size=18,
                                     foreground_color=textColor, background_color=(0.9, 0.9, 0.9, 1),
                                     cursor_color=textColor)
 
        self.new_email = TextInput(hint_text="Nuevo correo", multiline=False, size_hint=(1, 0.2), font_size=18,
                                     foreground_color=textColor, background_color=(0.9, 0.9, 0.9, 1),
                                     cursor_color=textColor)
        
        self.new_clave = TextInput(hint_text="Nueva contraseña", password=True, multiline=False, size_hint=(1, 0.2),
                                   font_size=18, foreground_color=textColor, background_color=(0.9, 0.9, 0.9, 1),
                                   cursor_color=textColor)
 
        self.layout.add_widget(self.new_usuario)
        self.layout.add_widget(self.new_email)
        self.layout.add_widget(self.new_clave)
 
        btn_guardar = Button(text="Guardar", size_hint=(1, 0.30), font_size=20, color=textColor)
        redondear_boton(btn_guardar, MainButonColor)
        btn_guardar.bind(on_press=self.guardar_usuario)
 
        btn_volver = Button(text="Volver", size_hint=(1, 0.30), font_size=20, color=textColor)
        redondear_boton(btn_volver, SecondButonColor)
        btn_volver.bind(on_press=self.volver)
 
        self.layout.add_widget(btn_guardar)
        self.layout.add_widget(btn_volver)
 
        self.add_widget(self.layout)
 
    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
 
    def guardar_usuario(self, instance):
        user = self.new_usuario.text.strip()
        pwd = self.new_clave.text.strip()
 
        if not user or not pwd:
            self.mostrar_popup("Error", "Completa todos los campos.")
        elif user in usuarios:
            self.mostrar_popup("Error", "Este usuario ya existe.")
        else:
            usuarios[user] = pwd
            self.mostrar_popup("Éxito", "Usuario registrado con éxito.")
            self.new_usuario.text = ''
            self.new_clave.text = ''
            self.manager.transition.direction = 'right'
            self.manager.current = 'login'
 
    def volver(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login'
 
    def mostrar_popup(self, titulo, mensaje):
        popup = Popup(title=titulo,
                      content=Label(text=mensaje, color=(1, 1, 1, 1)),
                      size_hint=(0.6, 0.3))
        popup.open()

class UsuarioScreen(Screen):
    usuario = StringProperty('')
 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
 
        with self.canvas.before:
            Color(*backgroundColor)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)
 
        self.layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        self.saludo = Label(text="", font_size=24, size_hint=(1, 0.2), markup=True, color=textColor)
        self.descripcion = Label(text="Aquí encontraras las carreras",
                                 font_size=16, size_hint=(1, 0.2), color=textColor)
 
        btn_salud = Button(text="Salud", size_hint=(1, 0.15), font_size=18, color=textColor)
        redondear_boton(btn_salud, MainButonColor)
        btn_salud.bind(on_press=self.ir_salud)

        btn_ingenieria = Button(text="Ingenieria", size_hint=(1, 0.15), font_size=18, color=textColor)
        redondear_boton(btn_ingenieria, MainButonColor)
        btn_ingenieria.bind(on_press=self.ir_ingenieria)

        btn_leyes = Button(text="Leyes", size_hint=(1, 0.15), font_size=18, color=textColor)
        redondear_boton(btn_leyes, MainButonColor)
        btn_leyes.bind(on_press=self.ir_leyes)

        btn_humanidades = Button(text="Humanidades", size_hint=(1, 0.15), font_size=18, color=textColor)
        redondear_boton(btn_humanidades, MainButonColor)
        btn_humanidades.bind(on_press=self.ir_humanidades)

        btn_arquitectura = Button(text="Arquitectura", size_hint=(1, 0.15), font_size=18, color=textColor)
        redondear_boton(btn_arquitectura, MainButonColor)
        btn_arquitectura.bind(on_press=self.ir_arquitectura)
 
        btn_salir = Button(text="Cerrar sesión", size_hint=(1, 0.15), font_size=18, color=textColor)
        redondear_boton(btn_salir, AlertButonColor)
        btn_salir.bind(on_press=self.cerrar_sesion)
 
        self.layout.add_widget(self.saludo)
        self.layout.add_widget(self.descripcion)
        self.layout.add_widget(btn_salud)
        self.layout.add_widget(btn_ingenieria)
        self.layout.add_widget(btn_leyes)
        self.layout.add_widget(btn_humanidades)
        self.layout.add_widget(btn_arquitectura)
        self.layout.add_widget(btn_salir)
 
        self.add_widget(self.layout)
 
    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
 
    def on_usuario(self, instance, value):
        self.saludo.text = f"[b]Bienvenido, {value}[/b]"
 
    def ir_salud(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = 'salud'

    def ir_ingenieria(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = 'ingenieria'
    
    def ir_leyes(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = 'leyes'

    def ir_humanidades(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = 'humanidades'

    def ir_arquitectura(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = 'arquitectura'
 
    def cerrar_sesion(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'bienvenida'
 
class SaludScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(*backgroundColor)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)

        # ScrollView con contenido vertical
        scroll = ScrollView(size_hint=(1, 1))
        contenido = GridLayout(cols=1, padding=40, spacing=20, size_hint_y=None)
        contenido.bind(minimum_height=contenido.setter('height'))

        contenido.add_widget(Label(
            text="Universidad de El Salvador",
            font_size=20,
            color=textColor,
            size_hint=(1, None),
            height=30
        ))

        contenido.add_widget(Image(
            source='universidad-de-el-salvador.jpg',
            size_hint=(1, None),
            height=150
        ))

        # Universidad de El Salvador
        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="Universidad de El Salvador (UES) ofrece en las áreas de salud: Medicina, Enfermería, Odontología, Nutrición y Dietética, Fonoaudiología, Kinesiología, y Medicina Veterinaria.",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=200,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)

        contenido.add_widget(Label(
            text="Universidad José Matías Delgado", 
            font_size=20, 
            color=textColor, 
            size_hint=(1, None), 
            height=30
            ))
        
        contenido.add_widget(Image(
            source='5238492159_ddded0da58_b.jpg', 
            size_hint=(1, None), 
            height=150
            ))
        
        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="Licenciatura en Medicina, Enfermería, Odontología, Psicología Clínica y más.",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=200,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)

        contenido.add_widget(Label(
            text="Universidad Evangélica de El Salvador", 
            font_size=20, 
            color=textColor, 
            size_hint=(1, None), 
            height=30
            ))
        
        contenido.add_widget(Image(
            source='Multimedia (1).jpeg', 
            size_hint=(1, None), 
            height=150
            ))
        
        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="La Universidad Evangélica de El Salvador (UEES) ofrece carreras en Medicina, Enfermería, Psicología y Nutrición, algunas de las cuales están acreditadas internacionalmente ",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=150,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)

        contenido.add_widget(Label(
            text="Universidad Dr. Andrés Bello", 
            font_size=20, 
            color=textColor, 
            size_hint=(1, None), 
            height=30
            ))
        
        contenido.add_widget(Image(
            source='unab.jpg', 
            size_hint=(1, None), 
            height=150
            ))
        
        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="La Universidad Dr. Andrés Bello (UNAB) en El Salvador ofrece varias carreras en el área de la salud, incluyendo: Licenciatura en Enfermería, Licenciatura en Laboratorio Clínico, Licenciatura en Radiología e Imágenes, Técnico en Enfermería y Técnico en Optometría. También ofrecen carreras como Licenciatura en Nutrición y Tecnólogo en Enfermería ",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=200,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)

        contenido.add_widget(Label(
            text="Universidad Tecnológica de El Salvador", 
            font_size=20, 
            color=textColor, 
            size_hint=(1, None), 
            height=30
            ))
        
        contenido.add_widget(Image(
            source='utec.jpeg', 
            size_hint=(1, None), 
            height=150
            ))
        
        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="La Universidad Tecnológica de El Salvador (UTEC) ofrece las siguientes carreras en el área de salud: Licenciatura en Química y Farmacia. Además, aunque no son específicamente carreras de salud, la UTEC también ofrece carreras relacionadas con la salud desde una perspectiva más tecnológica, como: Ingeniería en Biotecnología y Licenciatura en Ciencia y Tecnología de Lácteos. ",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=200,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)

        contenido.add_widget(Label(
            text="Universidad Católica de El Salvador ", 
            font_size=20, 
            color=textColor, 
            size_hint=(1, None), 
            height=30
            ))
        
        contenido.add_widget(Image(
            source='uca.jpeg', 
            size_hint=(1, None), 
            height=150
            ))
        
        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="La Universidad Católica de El Salvador (UNICAES) ofrece las siguientes carreras en el área de salud: Doctorado en Medicina, Licenciatura en Enfermería, y Técnico en Enfermería. Además, ofrece la Licenciatura en Nutrición y Dietética  ",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=200,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)

        contenido.add_widget(Label(
            text="Universidad de Oriente", 
            font_size=20, 
            color=textColor, 
            size_hint=(1, None), 
            height=30
            ))
        
        contenido.add_widget(Image(
            source='uo.jpg', 
            size_hint=(1, None), 
            height=150
            ))
        
        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="La Universidad de Oriente (UNIVO) ofrece las siguientes carreras en el área de salud: Doctorado en Medicina, Licenciatura en Enfermería, Licenciatura en Laboratorio Clínico, y Técnico en Optometría. También se ofrece la Licenciatura en Nutrición y la Licenciatura en Psicología, aunque no se especifica si son parte de la Facultad de Ciencias de la Salud. ",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=200,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)
        
        btn_regresar = Button(text="Regresar", size_hint=(1, None), height=50, font_size=20, color=textColor)
        redondear_boton(btn_regresar, SecondButonColor)
        btn_regresar.bind(on_press=self.regresar)
        contenido.add_widget(btn_regresar)

        scroll.add_widget(contenido)
        self.add_widget(scroll)

    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def regresar(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'usuario'
 
class IngenieriaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(*backgroundColor)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)

        # ScrollView con contenido vertical
        scroll = ScrollView(size_hint=(1, 1))
        contenido = GridLayout(cols=1, padding=40, spacing=20, size_hint_y=None)
        contenido.bind(minimum_height=contenido.setter('height'))
        
        contenido.add_widget(Label(
            text="Universidad de El Salvador",
            font_size=20,
            color=textColor,
            size_hint=(1, None),
            height=30
        ))

        contenido.add_widget(Image(
            source='universidad-de-el-salvador.jpg',
            size_hint=(1, None),
            height=150
        ))

        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="La Universidad de El Salvador (UES) ofrece diversas carreras en el área de ingeniería, como Ingeniería Civil, Ingeniería Eléctrica, Ingeniería Industrial, Ingeniería de Sistemas Informáticos, Ingeniería Química, entre otras.",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=200,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)

        contenido.add_widget(Label(
            text="Universidad Tecnológica de El Salvador",
            font_size=20,
            color=textColor,
            size_hint=(1, None),
            height=30
        ))

        contenido.add_widget(Image(
            source='utec.jpeg',
            size_hint=(1, None),
            height=150
        ))

        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="La Universidad Tecnológica de El Salvador (UTEC) ofrece varias carreras de ingeniería. Las opciones incluyen: Ingeniería Civil, Ingeniería Ambiental, Ingeniería Química, Ingeniería Mecatrónica, Ingeniería Industrial, Ingeniería Electrónica, Ingeniería Mecánica e Ingeniería de la Energía ",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=200,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)

        contenido.add_widget(Label(
            text="Universidad Dr. José Matías Delgado",
            font_size=20,
            color=textColor,
            size_hint=(1, None),
            height=30
        ))

        contenido.add_widget(Image(
            source='5238492159_ddded0da58_b.jpg',
            size_hint=(1, None),
            height=150
        ))

        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="La Universidad Dr. José Matías Delgado (UJMD) ofrece las siguientes carreras de ingeniería: Ingeniería Agroindustrial, Ingeniería en Gestión Ambiental, Ingeniería en Alimentos, Ingeniería en Agrobiotecnología, Ingeniería en Electrónica y Comunicaciones, Ingeniería en Logística y Distribución, e Ingeniería Industrial",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=200,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)

        contenido.add_widget(Label(
            text="Universidad Don Bosco", 
            font_size=20,
            color=textColor,
            size_hint=(1, None),
            height=30
        ))
 
        contenido.add_widget(Image(
            source='undb.jpg',
            size_hint=(1, None),
            height=150
        ))
 
        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="La Universidad Don Bosco (UDB) ofrece varias carreras de ingeniería. Entre ellas se encuentran Ingeniería Mecánica, Ingeniería Industrial, Ingeniería Biomédica, Ingeniería en Ciencias de la Computación, Ingeniería Eléctrica, Ingeniería Mecatrónica, Ingeniería en Aeronáutica, e Ingeniería Electrónica y Automatización. También ofrecen Ingeniería en Telecomunicaciones y Redes, según la página de la universidad.", #información de la universidad que está en el documento
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=400,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)

        contenido.add_widget(Label(
            text="Universidad Politécnica de El Salvador", 
            font_size=20,
            color=textColor,
            size_hint=(1, None),
            height=30
        ))
 
        contenido.add_widget(Image(
            source='upoes.jpg',
            size_hint=(1, None),
            height=150
        ))
 
        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text=" La Universidad Politécnica de El Salvador (UPES) ofrece las siguientes carreras de ingeniería: Ingeniería Civil, Ingeniería en Ciencias de la Computación, Ingeniería Eléctrica, e Ingeniería Industrial. También ofrecen un Técnico en Sistemas de Computación. ", #información de la universidad que está en el documento
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=400,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)

        contenido.add_widget(Label(
            text="Universidad Francisco Gavidia", 
            font_size=20,
            color=textColor,
            size_hint=(1, None),
            height=30
        ))
 
        contenido.add_widget(Image(
            source='ufga.jpg',
            size_hint=(1, None),
            height=150
        ))

        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="La Universidad Francisco Gavidia (UFG) ofrece varias carreras de ingeniería, incluyendo Ingeniería Industrial, Ingeniería en Telecomunicaciones, Ingeniería en Control Eléctrico, Ingeniería en Ciencias de la Computación, Ingeniería en Gestión de Base de Datos, e Ingeniería en Desarrollo de Software. También ofrece carreras como Ingeniería en Diseño y Desarrollo de Videojuegos. ", #información de la universidad que está en el documento
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=400,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)

        btn_regresar = Button(
            text="Regresar",
            size_hint=(1, None),
            height=60,
            font_size=20,
            color=textColor
        )
        redondear_boton(btn_regresar, SecondButonColor)
        btn_regresar.bind(on_press=self.regresar)
        contenido.add_widget(btn_regresar)

        scroll.add_widget(contenido)
        self.add_widget(scroll)

    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def regresar(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'usuario'

class LeyesScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(*backgroundColor)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)

        # ScrollView con contenido vertical
        scroll = ScrollView(size_hint=(1, 1))
        contenido = GridLayout(cols=1, padding=40, spacing=20, size_hint_y=None)
        contenido.bind(minimum_height=contenido.setter('height'))
        
        contenido.add_widget(Label(
            text="Universidad de El Salvador",
            font_size=20,
            color=textColor,
            size_hint=(1, None),
            height=30
        ))

        contenido.add_widget(Image(
            source='universidad-de-el-salvador.jpg',
            size_hint=(1, None),
            height=150
        ))

        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="La Universidad de El Salvador (UES) ofrece formación en el área de leyes a través de la carrera de Licenciatura en Ciencias Jurídicas, la cual capacita a los estudiantes en derecho penal, civil, constitucional, laboral y otras ramas fundamentales para el ejercicio profesional del derecho.",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=200,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)

        contenido.add_widget(Label(
            text="Universidad Tecnológica de El Salvador ",
            font_size=20,
            color=textColor,
            size_hint=(1, None),
            height=30
        ))

        contenido.add_widget(Image(
            source='utec.jpeg',
            size_hint=(1, None),
            height=150
        ))

        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text=" La Universidad Tecnológica de El Salvador (UTEC) ofrece la Licenciatura en Ciencias Jurídicas. Esta carrera prepara a los estudiantes para desenvolverse en diversas áreas del derecho, como el derecho civil, penal, mercantil, constitucional, tributario y laboral",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=400,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)

        contenido.add_widget(Label(
            text="Universidad Dr. Andrés Bello ",
            font_size=20,
            color=textColor,
            size_hint=(1, None),
            height=30
        ))

        contenido.add_widget(Image(
            source='unab.jpg',
            size_hint=(1, None),
            height=150
        ))

        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="La Universidad Dr. Andrés Bello (UNAB) en El Salvador ofrece la Licenciatura en Ciencias Jurídicas como carrera en el área de derecho. Esta licenciatura está enfocada en formar profesionales capacitados para abordar las problemáticas legales del país, brindándoles herramientas teóricas, técnicas, prácticas y científicas, con énfasis en el servicio, la justicia y la conciencia social",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=400,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)

        contenido.add_widget(Label(
            text="Universidad Modular Abierta",
            font_size=20,
            color=textColor,
            size_hint=(1, None),
            height=30
        ))

        contenido.add_widget(Image(
            source='uma.jpeg',
            size_hint=(1, None),
            height=150
        ))

        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="La Universidad Modular Abierta (UMA) en El Salvador ofrece la Licenciatura en Ciencias Jurídicas, también conocida como Derecho. Además, cuenta con una Maestría en Derecho Procesal Civil y Mercantil",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=400,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)

        contenido.add_widget(Label(
            text="Universidad Dr. José Matías Delgado",
            font_size=20,
            color=textColor,
            size_hint=(1, None),
            height=30
        ))

        contenido.add_widget(Image(
            source='5238492159_ddded0da58_b.jpg',
            size_hint=(1, None),
            height=150
        ))

        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="La Universidad Dr. José Matías Delgado (UJMD) ofrece la Licenciatura en Ciencias Jurídicas y la Licenciatura en Relaciones Internacionales dentro de su Facultad de Jurisprudencia y Ciencias Sociales. Además, cuenta con una Maestría en Derecho Administrativo y se espera que pronto ofrezca un Doctorado en Derecho Privado, según información de la universidad. ",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=400,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)        

        contenido.add_widget(Label(
            text="Universidad Pedagógica de El Salvador",
            font_size=20,
            color=textColor,
            size_hint=(1, None),
            height=30
        ))

        contenido.add_widget(Image(
            source='uped.jpg',
            size_hint=(1, None),
            height=150
        ))

        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="La Universidad Pedagógica de El Salvador ofrece la Licenciatura en Ciencias Jurídicas. Algunas de las áreas donde los graduados pueden desenvolverse incluyen: Asesoría legal en el sector público y privado.Ejercicio de la profesión como abogado.Participación en la función legislativa.Desarrollo de funciones en el ámbito empresarial, económico y financiero",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=400,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto) 

        btn_regresar = Button(
            text="Regresar",
            size_hint=(1, None),
            height=60,
            font_size=20,
            color=textColor
        )
        redondear_boton(btn_regresar, SecondButonColor)
        btn_regresar.bind(on_press=self.regresar)
        contenido.add_widget(btn_regresar)

        scroll.add_widget(contenido)
        self.add_widget(scroll)

    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def regresar(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'usuario'

class HumanidadesScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(*backgroundColor)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)

        # ScrollView con contenido vertical
        scroll = ScrollView(size_hint=(1, 1))
        contenido = GridLayout(cols=1, padding=40, spacing=20, size_hint_y=None)
        contenido.bind(minimum_height=contenido.setter('height'))
        
        contenido.add_widget(Label(
            text="Universidad de El Salvador",
            font_size=20,
            color=textColor,
            size_hint=(1, None),
            height=30
        ))

        contenido.add_widget(Image(
            source='universidad-de-el-salvador.jpg',
            size_hint=(1, None),
            height=150
        ))

        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="Universidad de El Salvador (UES) ofrece formación en el área de Humanidades a través de la carrera de Licenciatura en Humanidades y Ciencias Sociales, la cual capacita a los estudiantes en disciplinas como Historia, Literatura, Filosofía, Sociología y Antropología. Esta carrera prepara a los futuros profesionales para analizar, interpretar y contribuir al desarrollo cultural y social del país, fomentando un pensamiento crítico y una profunda comprensión de la realidad nacional e internacional.",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=400,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)

        contenido.add_widget(Label(
            text="Universidad Tecnológica de El Salvador",
            font_size=20,
            color=textColor,
            size_hint=(1, None),
            height=30
        ))

        contenido.add_widget(Image(
            source='utec.jpeg',
            size_hint=(1, None),
            height=150
        ))

        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="La Universidad Tecnológica de El Salvador (UTEC) ofrece varias carreras dentro del área de humanidades, principalmente a través de su Facultad de Ciencias Sociales. Estas incluyen: Licenciatura en Idioma Inglés, Licenciatura en Psicología, Licenciatura en Comunicaciones, y Técnico en Relaciones Públicas",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=400,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)

        contenido.add_widget(Label(
            text="Universidad Dr. José Matías Delgado ",
            font_size=20,
            color=textColor,
            size_hint=(1, None),
            height=30
        ))

        contenido.add_widget(Image(
            source='5238492159_ddded0da58_b.jpg',
            size_hint=(1, None),
            height=150
        ))

        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="La Universidad Dr. José Matías Delgado (UJMD) ofrece varias carreras dentro del área de Humanidades, incluyendo Licenciatura en Ciencias de la Comunicación, Licenciatura en Diseño Gráfico, Licenciatura en Psicología, Licenciatura en Lenguas Extranjeras y Arquitectura",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=400,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)

        contenido.add_widget(Label(
            text="Universidad Don Bosco",
            font_size=20,
            color=textColor,
            size_hint=(1, None),
            height=30
        ))

        contenido.add_widget(Image(
            source='undb.jpg',
            size_hint=(1, None),
            height=150
        ))

        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="La Universidad Don Bosco (UDB) ofrece las siguientes carreras de humanidades: Licenciatura en Ciencias de la Comunicación, Licenciatura en Diseño Gráfico, Licenciatura en Idiomas con especialidad en la Adquisición de Lenguas Extranjeras, Licenciatura en Idiomas con especialidad en Turismo, Técnico en Diseño Gráfico, Técnico en Multimedia, Profesorado en Teología Pastoral, y Profesorado en Educación Básica para Primero y Segundo Ciclos",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=400,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)

        contenido.add_widget(Label(
            text="Universidad Católica de El Salvador",
            font_size=20,
            color=textColor,
            size_hint=(1, None),
            height=30
            ))

        contenido.add_widget(Image(
            source='uca.jpeg',
            size_hint=(1, None),
            height=150
        ))

        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="La Universidad Católica de El Salvador (UNICAES) ofrece varias carreras dentro de la facultad de Ciencias y Humanidades. Entre ellas se encuentran: Licenciatura en Idioma Inglés, Licenciatura en Ciencias de la Educación con Especialidad en Educación Básica, y Licenciatura en Periodismo y Comunicación Audiovisual",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=400,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto) 

        contenido.add_widget(Label(
            text="Universidad Dr. Andrés Bello",
            font_size=20,
            color=textColor,
            size_hint=(1, None),
            height=30
        ))

        contenido.add_widget(Image(
            source='unab.jpg',
            size_hint=(1, None),
            height=150
        ))

        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="La Universidad Dr. Andrés Bello (UNAB) ofrece varias carreras dentro del área de humanidades, incluyendo Licenciatura en Comunicaciones, Licenciatura en Ciencias Jurídicas, Licenciatura en Psicología, y Licenciatura en Trabajo Social",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=400,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)               

        contenido.add_widget(Label(
            text="Universidad de Oriente",
            font_size=20,
            color=textColor,
            size_hint=(1, None),
            height=30
        ))

        contenido.add_widget(Image(
            source='uo.jpg',
            size_hint=(1, None),
            height=150
        ))

        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="La Universidad de Oriente (UNIVO) ofrece las siguientes carreras dentro del área de humanidades: Licenciatura en Psicología, Licenciatura en Psicopedagogía, Licenciatura en Educación (con especialización en Idioma Inglés), Licenciatura en Idioma Inglés, y Licenciatura en Ciencias de la Comunicación (con énfasis en Periodismo y Comunicación Social",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=400,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto) 

        contenido.add_widget(Label(
            text="Universidad Modular Abierta",
            font_size=20,
            color=textColor,
            size_hint=(1, None),
            height=30
        ))

        contenido.add_widget(Image(
            source='uma.jpeg',
            size_hint=(1, None),
            height=150
        ))

        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="La Universidad Modular Abierta (UMA) ofrece las siguientes carreras de humanidades: Licenciatura en Psicología, Licenciatura en Ciencias de la Educación con especialidad en Idioma Inglés, Licenciatura en Ciencias de la Educación con especialidad en Lenguaje y Literatura, Profesorado y Licenciatura en Educación Inicial y Parvularia, Profesorado en Ciencias Sociales para tercer ciclo de Educación Básica y Educación Media, y Profesorado en Lenguaje y Literatura para tercer ciclo de Educación Básica y Educación Media",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=400,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)

        btn_regresar = Button(
            text="Regresar",
            size_hint=(1, None),
            height=60,
            font_size=20,
            color=textColor
        )
        redondear_boton(btn_regresar, SecondButonColor)
        btn_regresar.bind(on_press=self.regresar)
        contenido.add_widget(btn_regresar)

        scroll.add_widget(contenido)
        self.add_widget(scroll)

    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def regresar(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'usuario'

class ArqitecturaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(*backgroundColor)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)

        # ScrollView con contenido vertical
        scroll = ScrollView(size_hint=(1, 1))
        contenido = GridLayout(cols=1, padding=40, spacing=20, size_hint_y=None)
        contenido.bind(minimum_height=contenido.setter('height'))

        # Universidad José Matías Delgado (UJMD)
        contenido.add_widget(Label(
            text="Universidad José Matías Delgado",
            font_size=20,
            color=textColor,
            size_hint=(1, None),
            height=30
        ))

        contenido.add_widget(Image(
            source='5238492159_ddded0da58_b.jpg',
            size_hint=(1, None),
            height=150
        ))

# Scroll individual para el cuadro de texto
        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="Universidad José Matías Delgado (UJMD) ofrece formación en el área de Arquitectura a través de la carrera de Licenciatura en Arquitectura, que prepara a los estudiantes en el diseño, planificación y construcción de espacios habitables y funcionales. El programa incluye estudios en urbanismo, diseño sostenible, tecnología de la construcción y teoría arquitectónica, con el fin de formar profesionales capaces de contribuir al desarrollo urbano y arquitectónico del país.",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint_y=None,
            height=400,  # contenido más largo que el contenedor
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1)
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)

        contenido.add_widget(Label(
            text="Universidad Politécnica de El Salvador",
            font_size=20,
            color=textColor,
            size_hint=(1, None),
            height=30
        ))

        contenido.add_widget(Image(
            source='upoes.jpg',
            size_hint=(1, None),
            height=150
        ))

# Scroll individual para el cuadro de texto
        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="Ingeniería Civil, Ingeniería Eléctrica, Ingeniería Industrial",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint_y=None,
            height=200,  # contenido más largo que el contenedor
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1)
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)
        
        contenido.add_widget(Label(
            text="Universidad Tecnológica de El Salvador",
            font_size=20,
            color=textColor,
            size_hint=(1, None),
            height=30
        ))

        contenido.add_widget(Image(
            source='utec.jpeg',
            size_hint=(1, None),
            height=150
        ))

        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="La carrera de Arquitectura en la Universidad Tecnológica de El Salvador (UTEC) se enfoca en diseño arquitectónico, planificación urbana, sostenibilidad ambiental, tecnología aplicada, diseño de interiores, supervisión de obras, patrimonio cultural y administración de proyectos, integrando herramientas digitales como AutoCAD y Revit, y promoviendo una formación práctica y multidisciplinaria que prepara a los estudiantes para enfrentar retos técnicos, sociales y creativos en el entorno construido.",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=400,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)

        contenido.add_widget(Label(
            text='Universidad Centoamericana José Simeón Cañas',
            font_size=20,
            color=textColor,
            size_hint=(1, None),
            height=60,  # Aumenta la altura para permitir varias líneas
            text_size=(300, None),  # 👈 Esto activa el ajuste automático al ancho del contenedor
            halign='center',      # Centra el texto horizontalmente
            valign='middle'       # Centra el texto verticalmente
        ))


        contenido.add_widget(Image(
            source='cañas.jpeg',
            size_hint=(1, None),
            height=150
        ))

        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="La carrera de Arquitectura en la Universidad Centroamericana José Simeón Cañas (UCA) se basa en tres pilares: diseño arquitectónico, tecnología y teoría histórica. Está orientada a formar profesionales con pensamiento crítico, creatividad y compromiso social, capaces de intervenir en el entorno urbano y rural con propuestas sostenibles y contextualizadas. Los estudiantes se preparan en áreas como diseño, planificación urbana, construcción, supervisión, docencia y administración pública, utilizando herramientas digitales y metodologías actualizadas",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=400,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)
        contenido.add_widget(Label(
            text="Universidad de El Salvador",
            font_size=20,
            color=textColor,
            size_hint=(1, None),
            height=30
        ))

        contenido.add_widget(Image(
            source='universidad-de-el-salvador.jpg',
            size_hint=(1, None),
            height=150
        ))

        scroll_texto = ScrollView(size_hint=(1, None), height=200)
        caja_descriptiva = TextInput(
            text="La carrera de Arquitectura en la Universidad de El Salvador (UES) se imparte en la Facultad de Ingeniería y Arquitectura. Está orientada a formar profesionales con capacidad técnica, científica y humanística, capaces de mejorar el entorno físico urbano y rural. El plan de estudios abarca áreas como teoría e historia, comunicación arquitectónica, urbanismo, tecnología de la construcción y proyectación arquitectónica. Los estudiantes desarrollan habilidades para diseñar, construir, supervisar y administrar proyectos arquitectónicos, con una visión crítica y compromiso social",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint=(1, None),
            height=400,
            cursor_color=textColor,
            foreground_color=textColor,
            background_color=(0.95, 0.95, 0.95, 1),
        )
        scroll_texto.add_widget(caja_descriptiva)
        contenido.add_widget(scroll_texto)

        # Botón de regreso integrado al scroll
        btn_regresar = Button(
            text="Regresar",
            size_hint=(1, None),
            height=60,
            font_size=20,
            color=textColor
        )
        redondear_boton(btn_regresar, SecondButonColor)
        btn_regresar.bind(on_press=self.regresar)
        contenido.add_widget(btn_regresar)

        # Agregar todo al ScrollView
        scroll.add_widget(contenido)
        self.add_widget(scroll)

    def actualizar_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def regresar(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'usuario'

class LoginApp(App):
    def build(self):
        self.title = "App de Login"
        sm = ScreenManager(transition=FadeTransition(duration=0.3))
        sm.add_widget(BienvenidaScreen(name='bienvenida'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(UsuarioScreen(name='usuario'))
        sm.add_widget(RegistrarScreen(name='registrar'))
        sm.add_widget(SaludScreen(name='salud'))
        sm.add_widget(IngenieriaScreen(name='ingenieria'))
        sm.add_widget(LeyesScreen(name='leyes'))
        sm.add_widget(HumanidadesScreen(name='humanidades'))
        sm.add_widget(ArqitecturaScreen(name='arquitectura'))
        return sm
 
if __name__ == '__main__':
    LoginApp().run()