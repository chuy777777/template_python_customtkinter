import numpy as np
import customtkinter  as ctk
import tkinter as tk

from components.create_frame import CreateFrame
from components.create_scrollable_frame import CreateScrollableFrame
from components.grid_frame import GridFrame

class FrameApplication(CreateFrame):
    def __init__(self, master, name, **kwargs):
        CreateFrame.__init__(self, master=master, name=name, grid_frame=GridFrame(dim=(3,2), arr=np.array([["0,0","0,1"],["0,0","1,1"],["2,0","2,0"]])), **kwargs)
       
        label_00=ctk.CTkLabel(master=self, text="Component 00", bg_color="lightcoral")
        label_01=ctk.CTkLabel(master=self, text="Component 01", bg_color="lightcoral")
        label_11=ctk.CTkLabel(master=self, text="Component 11", bg_color="lightcoral")
        label_20=ctk.CTkLabel(master=self, text="Component 20", bg_color="lightcoral")
        
        self.insert_element(cad_pos="0,0", element=label_00, padx=5, pady=5, sticky="nsew")
        self.insert_element(cad_pos="0,1", element=label_01, padx=5, pady=5, sticky="nsew")
        self.insert_element(cad_pos="1,1", element=label_11, padx=5, pady=5, sticky="nsew")
        self.insert_element(cad_pos="2,0", element=label_20, padx=5, pady=5, sticky="nsew")

class App(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(self)

        # Configuramos nuestra aplicacion
        self.geometry("1366x768")
        self.title("Plantilla")

        # Configuramos el sistema de cuadricula
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Creamos un frame root
        self.frame_root=CreateFrame(master=self, name="FrameRoot", grid_frame=GridFrame(dim=(1,1), arr=None))
        
        # Colocamos el frame root en la cuadricula
        self.frame_root.grid(row=0, column=0, padx=5, pady=5, sticky="nsew") # Al agregar sticky='nsew' el frame pasa de widthxheight a abarcar todo el espacio disponible

        # Creamos el elemento principal 
        self.frame_application=FrameApplication(master=self.frame_root, name="FrameApplication")

        # Insertamos el elemento principal
        self.frame_root.insert_element(cad_pos="0,0", element=self.frame_application, padx=5, pady=5, sticky="nsew")

        # Configuramos el cerrado de la ventana
        self.protocol("WM_DELETE_WINDOW", self.destroy)

    def destroy(self):
        ctk.CTk.quit(self)
        ctk.CTk.destroy(self)

if __name__ == "__main__":
    # Configuramos e iniciamos la aplicacion
    ctk.set_appearance_mode("Light")
    ctk.set_default_color_theme("green")
    app=App()
    app.mainloop()