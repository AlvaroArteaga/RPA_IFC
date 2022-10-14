from os import listdir
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



KV = '''







<TwoLineIconListItem>:
    text:
    secondary_text:
    on_release:
        print('holaaaa')
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
                    on_unselected: app.on_unselected(*args)
                    on_selected_mode: app.set_selection_mode(*args)
        Tab:
            id: two
            title: 'Meses'
        Tab:
            id: two
            title: 'Directorio'




   


        


    
'''

class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class TwoLineIconListItem(TwoLineAvatarIconListItem):
    '''Custom list item.'''

    icon = StringProperty("android")


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''


class Example(MDApp):
    overlay_color = get_color_from_hex("#6042e4")
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def on_start(self):

        #self.root.ids.tabs.add_widget(Tab(title=f"Procesos"))
        #self.root.ids.tabs.add_widget(Tab(title=f"Meses"))
        #self.root.ids.tabs.add_widget(Tab(title=f"Directorio"))

        icons = list(md_icons.keys())
        self.root.ids.scroll.add_widget(TwoLineIconListItem(text=f"BADX", secondary_text=f"Balance de Energía en Distribución", icon=icons[1],on_release=self.seleccion_proceso))
        self.root.ids.scroll.add_widget(TwoLineIconListItem(text=f"BAEN", secondary_text=f"Balance de Energía en Transmisión", icon=icons[2]))
        self.root.ids.scroll.add_widget(TwoLineIconListItem(text=f"EFAC", secondary_text=f"Energias Facturadas", icon=icons[3]))
        self.root.ids.scroll.add_widget(TwoLineIconListItem(text=f"FETR", secondary_text=f"Factor de Equidad Tarifaria Residencial", icon=icons[4]))
        self.root.ids.scroll.add_widget(TwoLineIconListItem(text=f"PJDX", secondary_text=f"Peajes en Distribución", icon=icons[5]))
        self.root.ids.scroll.add_widget(TwoLineIconListItem(text=f"PMGD", secondary_text=f"Desconexiones de PMGD", icon=icons[6]))
        self.root.ids.scroll.add_widget(TwoLineIconListItem(text=f"RCUT", secondary_text=f"Recaudación de Cargos Únicos de Transmisión", icon=icons[7]))
        self.root.ids.scroll.selected_mode = True
        self.root.ids.toolbar.right_action_items = [[""]]
        self.root.ids.toolbar.left_action_items = [[""]]
    def set_selection_mode(self, instance_selection_list, mode):
        #mode=True
        self.root.ids.scroll.selected_mode = True
        if mode:
            md_bg_color = self.overlay_color
            left_action_items = [
                [
                    "close",
                    lambda x: self.root.ids.scroll.unselected_all(),
                ]
            ]
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
            lambda x: self.root.ids.scroll.unselected_all(),
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

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        instance_tab.ids.label.text = tab_text


    def seleccion_proceso(self, TwoLineIconListItem):
        print('Proceso Seleccionado: ', TwoLineIconListItem.text)

    def siguiente(self):
        print("siguiente")
        print("tiene: ", len(self.root.ids.scroll.get_selected_list_items()), " procesos seleccionados")
        for p in self.root.ids.scroll.get_selected_list_items() :
            i=str(p).rfind('at ')+3
            f=len(str(p))-1
            item=str(p)[i:f]
            #val_item=ctypes.cast(item, ctypes.py_object).value
            val_item=ctypes.cast(item, POINTER(kivymd.uix.selection.selection.SelectionItem)).text
            print("seleccionó: ",p)

        for item in self.root.ids.scroll.children:
            if item.text == 'test':

Example().run()