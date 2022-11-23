from gc import get_objects
from os import listdir
from pkgutil import get_data
from kivy.animation import Animation
from ast import arg
from cgitb import text
from statistics import mode
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivy.properties import StringProperty
from kivymd.uix.behaviors import TouchBehavior
from kivymd.app import MDApp
from kivymd.uix.list import IRightBodyTouch, TwoLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
import sys
import ctypes
from ctypes import *
from kivy.core.window import Window
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.label import MDLabel
from kivymd.uix.selectioncontrol import MDSwitch
from kivy.metrics import dp
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.menu import MDDropdownMenu
import datetime



Window.size = (470,700)



KV = '''







<TwoLineIconListItem>:
    text:
    secondary_text:
    on_release:
    IconLeftWidget:
        icon: root.icon





MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        id: toolbar
        title: "Seleccione el proceso a descargar"
        right_action_items: [["arrow-right", lambda x: app.siguiente]]
        md_bg_color: 0, 0, 0, 1

    MDTabs:
        id: tabs
        on_tab_switch: app.on_tab_switch(*args)

        Tab:
            id: one
            title: 'Procesos'



            MDScrollView:

                MDSelectionList:
                    id: scroll
                    spacing: "12dp"
                    overlay_color: app.overlay_color[:-1] + [.2]
                    icon_bg_color: app.overlay_color
                    on_selected: app.on_selected(*args)
                    on_unselected: app.on_unselected(*argstres)
                    on_selected_mode: app.set_selection_mode(*args)
        Tab:
            id: two
            lock_swiping: True
            title: 'Meses'
            
            MDBoxLayout:
                padding: 20, 20, 20, 20
                margin: 20, 20
                orientation: 'vertical'

                MDLabel:
                    id: meses
                    text: "Seleccione los meses a descargar"
                    halign: "left"
                    font_size: 14

                MDGridLayout:
                    id: gridsw
                    cols: 2
                    row_force_default:True
                    row_default_height:40
       

                    MDLabel:
                        text: "Un solo mes"
                        halign: "left"
                        width:300
                        size_hint_x:None
                        font_size: 12
                        italic: True
                    
                    MDSwitch:
                        id:messw
                        width: dp(64)
                        active: True
                        on_active: app.test_state()

                    MDLabel:
                        id: variosLB
                        text: "Mismo periodo para los procesos seleccionados"
                        halign: "left"
                        width:300
                        size_hint_x:None
                        font_size: 12
                        italic: True
    
                    MDSwitch:
                        id:varios
                        width: dp(64)
                        active: True
                        opacity: 1

                MDGridLayout:
                    id: gridsw2
                    cols: 4
                    row_force_default:True
                    row_default_height:25
                    
                    MDLabel:
                        id: mdlabelano
                        text: "Seleccione el AÑO"
                        halign: "left"
                        width:145
                        size_hint_x:None
                        font_size: 13
                        bold: True
                    
                    MDDropDownItem:
                        id: drop_item
                        pos_hint: {'center_x': .5, 'center_y': .5}
                        text: 'item 0'
                        on_release: app.menu.open()
                        font_size: 13

                    MDLabel:
                        id: mdlabelmes
                        text: "y el MES"
                        halign: "right"
                        width:90
                        size_hint_x:None
                        font_size: 13
                        bold: True
                    
                    MDDropDownItem:
                        id: drop_item2
                        pos_hint: {'center_x': .5, 'center_y': .5}
                        text: 'item 0'
                        on_release: app.menu2.open()
                        font_size: 13

                    MDLabel:
                        id: mdlabelano_fn
                        text: "Seleccione el AÑO Final"
                        halign: "left"
                        width:145
                        size_hint_x:None
                        font_size: 13
                        bold: True
                    
                    MDDropDownItem:
                        id: drop_item_fn
                        pos_hint: {'center_x': .5, 'center_y': .5}
                        text: 'item 0'
                        on_release: 
                        font_size: 13

                    MDLabel:
                        id: mdlabelmes_fn
                        text: "y el MES Final"
                        halign: "right"
                        width:90
                        size_hint_x:None
                        font_size: 13
                        bold: True
                    
                    MDDropDownItem:
                        id: drop_item2_fn
                        pos_hint: {'center_x': .5, 'center_y': .5}
                        text: 'item 0'
                        on_release: 
                        font_size: 13
                        
            
                    
        Tab:
            id: three
            title: 'Directorio'

   


        


    
'''


mes_sel = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
          'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class TwoLineIconListItem(TwoLineAvatarIconListItem):
    '''Custom list item.'''

    icon = StringProperty("android")


class IconListItem(OneLineIconListItem):
    icon = StringProperty()

class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''

proceso_estado= [False,False,False,False,False,False,False]

class Example(MDApp):
    overlay_color = get_color_from_hex("#6042e4")
    
  



    
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def set_item(self, text_item):
        self.root.ids.drop_item.set_item(text_item)
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = int(date.strftime("%Y"))
        mes = int(date.strftime("%m"))

        
        mes_inicial=13
        mes_ini=13
        for pro_sgte in range(0,7):
            match pro_sgte:
                case 0:
                    if proceso_estado[pro_sgte]:
                        if int(text_item) > 2020: mes_inicial=1
                        elif int(text_item) == 2020: mes_inicial=3
                        mes_ini=min(mes_ini,mes_inicial)
                case 1:
                    if proceso_estado[pro_sgte]:
                        if int(text_item) == 2019: mes_inicial=5
                        else: mes_inicial=1
                        mes_ini=min(mes_ini,mes_inicial)
                case 2:
                    if proceso_estado[pro_sgte]:
                        if int(text_item) == 2021: mes_inicial=4
                        mes_ini=min(mes_ini,mes_inicial)
                case 3:
                    if proceso_estado[pro_sgte]:
                        if int(text_item) >= 2021: mes_inicial=1
                        mes_ini=min(mes_ini,mes_inicial)

                case 4:
                    if proceso_estado[pro_sgte]:
                         if int(text_item) == 2022: mes_inicial=4
                         mes_ini=min(mes_ini,mes_inicial)

                case 5:
                    if proceso_estado[pro_sgte]:
                        if int(text_item) == 2019: mes_inicial=5
                        else: mes_inicial=1
                        mes_ini=min(mes_ini,mes_inicial)

                case 6:
                    if proceso_estado[pro_sgte]:
                        if int(text_item) == 2019: mes_inicial=5
                        else: mes_inicial=1
                        mes_ini=min(mes_ini,mes_inicial)
    
        if int(text_item)<year: mes_fin=12
        else: mes_fin= mes-1

        menu_items2 = [
                {
                    "viewclass": "OneLineListItem",
                    "text": f"{mes_sel[i-1]}",
                    "height": dp(56),
                    "on_release": lambda x=f"{mes_sel[i-1]}": self.set_item2(x),
                } for i in range(mes_ini,mes_fin+1)
            ]
        self.menu2 = MDDropdownMenu(
                caller= self.root.ids.drop_item2,
                items=menu_items2,
                position="center",
                width_mult=4,
            )
        self.menu2.bind()

        #print("Se selecionó el MES "+str(mes))
        self.menu.dismiss()

    def set_item2(self, text_item):
        self.root.ids.drop_item2.set_item(text_item)
        self.menu2.dismiss()


    def on_start(self):

        #self.root.ids.tabs.add_widget(Tab(title=f"Procesos"))
        #self.root.ids.tabs.add_widget(Tab(title=f"Meses"))
        #self.root.ids.tabs.add_widget(Tab(title=f"Directorio"))


        self.root.ids.mdlabelano_fn.disabled = True
        self.root.ids.drop_item_fn.disabled = True
        self.root.ids.mdlabelmes_fn.disabled = True
        self.root.ids.drop_item2_fn.disabled = True

        self.root.ids.mdlabelano_fn.opacity = 0
        self.root.ids.drop_item_fn.opacity = 0
        self.root.ids.mdlabelmes_fn.opacity = 0
        self.root.ids.drop_item2_fn.opacity = 0



        icons = list(md_icons.keys())
        #self.root.ids.tabs.add_widget(CalculaCompra(tab_label_text='Calculadora'))
    
        #self.iter_list_objects = iter(list(self.root.ids.tabs.get_tab_list()))
        self.root.ids.tabs.children[0].disabled = True
        
        self.root.ids.scroll.add_widget(TwoLineIconListItem(text=f"BADX", secondary_text=f"Balance de Energía en Distribución", icon=icons[1],on_release=self.seleccion_proceso))
        self.root.ids.scroll.add_widget(TwoLineIconListItem(text=f"BAEN", secondary_text=f"Balance de Energía en Transmisión", icon=icons[2],on_release=self.seleccion_proceso))
        self.root.ids.scroll.add_widget(TwoLineIconListItem(text=f"EFAC", secondary_text=f"Energias Facturadas", icon=icons[3],on_release=self.seleccion_proceso))
        self.root.ids.scroll.add_widget(TwoLineIconListItem(text=f"FETR", secondary_text=f"Factor de Equidad Tarifaria Residencial", icon=icons[4],on_release=self.seleccion_proceso))
        self.root.ids.scroll.add_widget(TwoLineIconListItem(text=f"PJDX", secondary_text=f"Peajes en Distribución", icon=icons[5],on_release=self.seleccion_proceso))
        self.root.ids.scroll.add_widget(TwoLineIconListItem(text=f"PMGD", secondary_text=f"Desconexiones de PMGD", icon=icons[6],on_release=self.seleccion_proceso))
        self.root.ids.scroll.add_widget(TwoLineIconListItem(text=f"RCUT", secondary_text=f"Recaudación de Cargos Únicos de Transmisión", icon=icons[7],on_release=self.seleccion_proceso))
        self.root.ids.scroll.selected_mode = True
        self.root.ids.toolbar.right_action_items = [[""]]
        self.root.ids.toolbar.left_action_items = [[""]]




    def set_selection_mode(self, instance_selection_list, mode):
        #mode=True
        self.root.ids.scroll.selected_mode = True
        if mode:
            md_bg_color = self.overlay_color
            left_action_items = [[
                    "close",
                    lambda x: self.deseleccion(),
            ]]
            right_action_items = [["arrow-right", lambda x: self.siguiente(),]]
        else:
            self.root.ids.scroll.selected_mode = True
            #md_bg_color = (1, 1, 1, 1)
            md_bg_color = self.overlay_color
            #left_action_items = [["menu"]]
            left_action_items = [[""]]
            right_action_items = [[""]]
            self.root.ids.toolbar.title = "Seleccione el proceso a descargar"


        Animation(md_bg_color=md_bg_color, d=0.2).start(self.root.ids.toolbar)
        self.root.ids.toolbar.left_action_items = left_action_items
        self.root.ids.toolbar.right_action_items = right_action_items
    def on_selected(self, instance_selection_list, instance_selection_item):
        if len(instance_selection_list.get_selected_list_items())>1:
            self.root.ids.toolbar.title = str(
                len(instance_selection_list.get_selected_list_items())
            ) + " procesos seleccionados"
        else:
            self.root.ids.toolbar.title = str(
                len(instance_selection_list.get_selected_list_items())
            ) + " proceso seleccionado"
        self.root.ids.toolbar.left_action_items = [[
            "close",
            lambda x: self.deseleccion(),
        ]]
        self.root.ids.toolbar.right_action_items = [[
            "arrow-right",
            lambda x: self.siguiente(),
        ]]

    def on_unselected(self, instance_selection_list, instance_selection_item):
        if instance_selection_list.get_selected_list_items():
            if len(instance_selection_list.get_selected_list_items())>1:
                self.root.ids.toolbar.title = str(
                    len(instance_selection_list.get_selected_list_items())
                ) + " procesos seleccionados"
            else:
                self.root.ids.toolbar.title = str(
                    len(instance_selection_list.get_selected_list_items())
                ) + " proceso seleccionado"
        if len(instance_selection_list.get_selected_list_items())==0:
            self.root.ids.toolbar.title = "Seleccione el proceso a descargar"
            self.root.ids.toolbar.right_action_items = [[""]]
            self.root.ids.toolbar.left_action_items = [[""]]
        #print("PRUEBAA--AAA>   ",instance_selection_item)
        
            

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
       #instance_tab.ids.label.text = tab_text
       #print(tab_text)
       if tab_text=='Procesos':
        self.root.ids.tabs.children[0].disabled = True
        self.root.ids.meses.text ="Seleccione los meses a descargar"


    def seleccion_proceso(self, TwoLineIconListItem):
        #print('Proceso Seleccionado: ', TwoLineIconListItem.text)
        match TwoLineIconListItem.text:
            case "BADX":
                proceso_estado[0]=not(proceso_estado[0])
            case "BAEN":
                proceso_estado[1]=not(proceso_estado[1])
            case "EFAC":
                proceso_estado[2]=not(proceso_estado[2])
            case "FETR":
                proceso_estado[3]=not(proceso_estado[3])
            case "PJDX":
                proceso_estado[4]=not(proceso_estado[4])
            case "PMGD":
                proceso_estado[5]=not(proceso_estado[5])
            case "RCUT":
                proceso_estado[6]=not(proceso_estado[6])
        
    def deseleccion(self):
        proceso_estado[0]=proceso_estado[1]=proceso_estado[2]=proceso_estado[3]=proceso_estado[4]=proceso_estado[5]=proceso_estado[6]=False
        self.root.ids.scroll.unselected_all()

    def siguiente(self):
        #print("siguiente")
        #print("tiene: ", len(self.root.ids.scroll.get_selected_list_items()), " procesos seleccionados")
        #for p in self.root.ids.scroll.get_selected_list_items() :
        #    i=str(p).rfind('at ')+3
        #    f=len(str(p))-1
        #    item=str(p)[i:f]
        #    #val_item=ctypes.cast(item, ctypes.py_object).value
        #    val_item=ctypes.cast(item, POINTER(kivymd.uix.selection.selection.SelectionItem)).text
        siguientex = " ( "
        i=0
        anno=2022
        for pro_sgte in range(0,7):
            match pro_sgte:
                case 0:
                    if proceso_estado[pro_sgte]:
                        siguientex = siguientex + "  BADX  "
                        i=i+1
                        if anno > 2020: anno=2020

                case 1:
                    if proceso_estado[pro_sgte]:
                        siguientex = siguientex + "  BAEN  "
                        i=i+1
                        if anno > 2019: anno=2019

                case 2:
                    if proceso_estado[pro_sgte]:
                        siguientex = siguientex + "  EFAC  "
                        i=i+1
                        if anno > 2021: anno=2021

                case 3:
                    if proceso_estado[pro_sgte]:
                        siguientex = siguientex + "  FETR  "
                        i=i+1
                        if anno > 2021: anno=2021

                case 4:
                    if proceso_estado[pro_sgte]:
                        siguientex = siguientex + "  PJDX  "
                        i=i+1
                        if anno > 2022: anno=2022

                case 5:
                    if proceso_estado[pro_sgte]:
                        siguientex = siguientex + "  PMGD  "
                        i=i+1
                        if anno > 2019: anno=2019

                case 6:
                    if proceso_estado[pro_sgte]:
                        siguientex = siguientex + "  RCUT  "
                        i=i+1
                        if anno > 2019: anno=2019
        
        #for pro_sgte in range(0,7):
        #    if proceso_estado[pro_sgte]: i=i+1
        

        print(siguientex+" "+str(i))

        if i==1:
            self.root.ids.meses.text = self.root.ids.meses.text+" del proceso seleccionado"+siguientex+" ) para continuar "
            self.root.ids.variosLB.disabled = True
            self.root.ids.variosLB.opacity = 0
            self.root.ids.varios.disabled = True
            self.root.ids.varios.opacity = 0
        elif i>1:
            self.root.ids.meses.text = self.root.ids.meses.text+" de los procesos seleccionados"+siguientex+" ) para continuar "
            self.root.ids.variosLB.disabled = False
            self.root.ids.variosLB.opacity = 1
            self.root.ids.varios.disabled = False
            self.root.ids.variosLB.opacity = 1
            self.root.ids.variosLB.text ="Mismo periodo para los "+str(i)+" procesos seleccionados"

        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = int(date.strftime("%Y"))
        mes = int(date.strftime("%m"))
 


        menu_items2 = [
                {
                    "viewclass": "OneLineListItem",
                    "text": f"{mes_sel[i-1]}",
                    "height": dp(56),
                    "on_release": lambda x=f"{mes_sel[i-1]}": self.set_item2(x),
                } for i in range(1,mes)
            ]
        self.menu2 = MDDropdownMenu(
                caller= self.root.ids.drop_item2,
                items=menu_items2,
                position="center",
                width_mult=4,
            )
        self.menu2.bind()



        j=year-anno+1
        #print(" años a revisar: "+str(j))
        menu_items = [
                {
                    "viewclass": "OneLineListItem",
                    "text": f"{year-i}",
                    "height": dp(56),
                    "on_release": lambda x=f"{year-i}": self.set_item(x),
                } for i in range(j)
            ]
        self.menu = MDDropdownMenu(
                caller= self.root.ids.drop_item,
                items=menu_items,
                position="center",
                width_mult=4,
            )
        self.menu.bind()

        if mes>1:

            self.root.ids.drop_item.text = str(year)
            self.root.ids.drop_item2.text = mes_sel[mes-2]
            self.set_item(str(year))
            self.set_item2(mes_sel[mes-2])
        else:
            self.root.ids.drop_item.text = str(year-1)
            self.root.ids.drop_item2.text = mes_sel[11]
            self.set_item(str(year-1))
            self.set_item2(mes_sel[11])
    






        self.root.ids.tabs.children[0].disabled = False

        self.root.ids.tabs.switch_tab('Meses')

        #MDApp.get_running_app().root.ids.tabs.carousel.load_next('CalculaCompra')
            
        
        #print('testttt  ', self.root.ids.scroll.children)
        
        #for p in self.root.ids.scroll.get_selected_list_items() :
        #    i=str(p).rfind('at ')+3
        #    f=len(str(p))-1
        #    item=str(p)[i:f]
        #    print("seleccionó: ",item)
            #ActualValue = ctypes.cast(item, ctypes.py_object)[1]
            #print('aqui:   ', ActualValue)
        #    pointer = get_objects(p)
        #    print(pointer)
            
        
            
        #for item in self.root.ids.scroll.children:
        #    if item.text == 'test':
    def test_state(self):



        #if mes>1:
        #    self.root.ids.drop_item.text = str(year)
        #    self.root.ids.drop_item2.text = mes_sel[mes-2]
        #else:
        #    self.root.ids.drop_item.text = str(year-1)
        #    self.root.ids.drop_item2.text = mes_sel[11]


        if self.root.ids.messw.active:

            self.root.ids.mdlabelano_fn.disabled = True
            self.root.ids.drop_item_fn.disabled = True
            self.root.ids.mdlabelmes_fn.disabled = True
            self.root.ids.drop_item2_fn.disabled = True

            self.root.ids.mdlabelano_fn.opacity = 0
            self.root.ids.drop_item_fn.opacity = 0
            self.root.ids.mdlabelmes_fn.opacity = 0
            self.root.ids.drop_item2_fn.opacity = 0

            self.root.ids.mdlabelano.text = "Seleccione el AÑO"
            self.root.ids.mdlabelmes.text = "y el MES"

        else:

            self.root.ids.mdlabelano.text = "Seleccione el AÑO Inicial"
            self.root.ids.mdlabelmes.text = "y el MES Inicial"

            self.root.ids.mdlabelano_fn.disabled = False
            self.root.ids.drop_item_fn.disabled = False
            self.root.ids.mdlabelmes_fn.disabled = False
            self.root.ids.drop_item2_fn.disabled = False

            self.root.ids.mdlabelano_fn.opacity = 1
            self.root.ids.drop_item_fn.opacity = 1
            self.root.ids.mdlabelmes_fn.opacity = 1
            self.root.ids.drop_item2_fn.opacity = 1
        

            currentDateTime = datetime.datetime.now()
            date = currentDateTime.date()
            year = date.strftime("%Y")
            mes = int(date.strftime("%m"))

            print(self.root.ids.drop_item2.text)
            print(mes_sel[mes-2])
            print(self.root.ids.drop_item.text)
            print(str(year))

            if self.root.ids.drop_item2.text == mes_sel[mes-2] and self.root.ids.drop_item.text == str(year):
                self.root.ids.drop_item2.text = mes_sel[mes-3]
                self.root.ids.drop_item2_fn.text = mes_sel[mes-2]
            elif mes_sel.index(self.root.ids.drop_item2.text)==11:
                self.root.ids.drop_item2_fn.text=mes_sel[0]
            else:
                self.root.ids.drop_item2_fn.text=mes_sel[mes_sel.index(self.root.ids.drop_item2.text)+1]


            if mes_sel.index(self.root.ids.drop_item2.text)==11:
                self.root.ids.drop_item_fn.text=str(int(self.root.ids.drop_item.text)+1)
            else:
                self.root.ids.drop_item_fn.text=self.root.ids.drop_item.text

            print(mes_sel.index(self.root.ids.drop_item2.text))
            print(self.root.ids.drop_item2.text)

        


  
            

#class CalculaCompra(MDFloatLayout, MDTabsBase):
#    def __init__(self, **kwargs):
#        super().__init__(**kwargs)

      

Example().run()