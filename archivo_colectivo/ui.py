import sys
import os
import subprocess
import ctypes
import logging
from packaging.version import parse, Version

import requests
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from paress2 import Paress

os.makedirs("logs", exist_ok=True)

logging.basicConfig(filename='logs/paress2.log', level=logging.ERROR,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')


ASSETS_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")


class App(tk.Tk):

    app_restarting = False

    def __init__(self):
        super().__init__()

        # Setting up Initial Things
        self.title(
            "PARESS2: Un descargador de imágenes del Portal de Archivos Españoles Pares")
        self.geometry("720x550")
        self.resizable(True, True)
        self.iconphoto(False, tk.PhotoImage(
            file=self.resource_path(os.path.join(ASSETS_FOLDER, "icon.png"))))
        self.configure(bg="white")

        # create a widget in the top of the window with the logo image an a title label
        self.top_frame = tk.Frame(self, bg="white")
        self.top_frame.pack(side="top", fill="both", expand=True)

        self.logo = tk.PhotoImage(file=self.resource_path(os.path.join(ASSETS_FOLDER, "icon.png")))
        # tamaño de la imagen: 100x100
        self.logo = self.logo.subsample(2, 2)
        self.logo_label = tk.Label(self.top_frame, image=self.logo, bg="white")
        self.logo_label.pack(side="left", padx=10, pady=10)

        self.title_label = tk.Label(
            self.top_frame, text="PARESS2", font=('Times', '20'), bg="white")
        self.title_label.pack(side="left", padx=10, pady=10)

        # check version
        self.version_paress()

        # create a widget in the middle of the window with the url entry and the download button
        self.middle_frame = tk.Frame(self, bg="white")
        self.middle_frame.pack(side="top", fill="both", expand=True)

        self.url_label = tk.Label(
            self.middle_frame, text="Enlace al documento:", font=('Times', '12'), bg="white")
        self.url_label.grid(row=0, column=0, padx=10, pady=10)

        self.url_entry = tk.Entry(self.middle_frame, width=50)
        self.url_entry.grid(row=0, column=1, padx=10, pady=10)

        url_placeholder = "http://pares.mcu.es/ParesBusquedas20/catalogo/show/256820114?nm"
        self.url_placeholder = url_placeholder
        # placeholder for the url entry
        self.url_entry.insert(0, url_placeholder)
        self.url_entry.config(fg="grey")

        # configurar focus in y focus out para el entry de la url
        self.url_entry.bind(
            "<FocusIn>", lambda x: self.on_focus_in(self.url_entry))
        self.url_entry.bind("<FocusOut>", lambda x: self.on_focus_out(
            self.url_entry, url_placeholder))

        # botón para escoger la carpeta de destino
        self.destination_button = tk.Button(
            self.middle_frame, text="Carpeta de destino", command=self.destination)
        self.destination_button.grid(row=1, column=0, padx=10, pady=10)

        # campo para escribir o mostrar la carpeta de destino
        self.destination_entry = tk.Entry(self.middle_frame, width=50)
        self.destination_entry.grid(row=1, column=1, padx=10, pady=10)

        # plus less buttons for the speed
        self.speed_label = tk.Label(
            self.middle_frame, text="Velocidad de descarga:", font=('Times', '12'), bg="white")
        self.speed_label.grid(row=2, column=0, padx=10, pady=10)

        self.speed_entry = tk.Entry(self.middle_frame, width=50)
        self.speed_entry.grid(row=2, column=1, padx=10, pady=10)

        speed_placeholder = "10"
        self.speed_placeholder = speed_placeholder
        # placeholder for the speed entry
        self.speed_entry.insert(0, speed_placeholder)
        self.speed_entry.config(fg="grey")

        # configurar focus in y focus out para el entry de la velocidad
        self.speed_entry.bind(
            "<FocusIn>", lambda x: self.on_focus_in(self.speed_entry))
        self.speed_entry.bind("<FocusOut>", lambda x: self.on_focus_out(
            self.speed_entry, speed_placeholder))

        # botón para descargar
        self.download_button = tk.Button(
            self.middle_frame, text="Descargar", command=self.download)
        self.download_button.grid(row=3, column=1, rowspan=3, padx=10, pady=10)

        # bottom_frame
        self.bottom_frame = tk.Frame(self, bg="white")
        self.bottom_frame.pack(side="top", fill="both", expand=True)

    def on_focus_in(self, entry):
        if entry.cget("fg") == "grey":
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def on_focus_out(self, entry, placeholder):
        if not entry.get():
            entry.insert(0, placeholder)
            entry.config(fg="grey")

    def destination(self):
        folder_selected = filedialog.askdirectory()
        self.destination_entry.delete(0, tk.END)

        # validate if the folder selected is a folder
        if os.path.isfile(folder_selected):
            folder_selected = os.path.dirname(folder_selected)

        # check if the folder selected exists
        if os.path.exists(folder_selected):
            self.destination_entry.insert(0, folder_selected)
        else:
            messagebox.showerror("Error", "La carpeta seleccionada no existe")

    def download(self):

        try:
            self.reporte_frame.destroy()
        except AttributeError:
            pass

        url = self.url_entry.get()

        if not url.startswith("http://pares.mcu.es/ParesBusquedas20/catalogo/show/"):
            # check if the url is valid but begins with https
            if url.startswith("https://pares.mcu.es/ParesBusquedas20/catalogo/show/"):
                pass
            else:
                messagebox.showerror("Error", "La url introducida no es válida")
                return

        # print folder_selected
        dir = self.destination_entry.get()
        # print dir
        vel = self.speed_entry.get()

        # print(url)
        # print(self.url_placeholder)

        if url != self.url_placeholder and dir != "":
            
            Paress(url, destino=dir, velocidad=int(vel)).descargar_imagenes()

            messagebox.showinfo("Descarga completada", "La descarga se ha completado correctamente")
            self.reporte_descarga(dir)
        else:
            if url == self.url_placeholder:
                messagebox.showerror(
                    "Error", "No se ha introducido ninguna url")
            if dir == "":
                messagebox.showerror(
                    "Error", "No se ha seleccionado ninguna carpeta de destino")

    def reporte_descarga(self, dir_destino):
        """Mostrar un reporte con las descargas realizadas"""
        self.bottom_frame.destroy()

        self.reporte_frame = tk.Frame(self, bg="white")
        self.reporte_frame.pack(side="top", fill="both", expand=True)

        self.reporte_label = tk.Label(
            self.reporte_frame, text="Descargas realizadas", font=('Times', '12'), bg="white")
        self.reporte_label.pack(side="top", padx=10, pady=10)

        self.reporte_text = tk.Text(self.reporte_frame, width=50, height=10)
        self.reporte_text.pack(side="top", padx=10, pady=10)

        # get last modified subdirectory in the destination folder
        subdirs = [os.path.join(dir_destino, o) for o in os.listdir(
            dir_destino) if os.path.isdir(os.path.join(dir_destino, o))]
        latest_subdir = max(subdirs, key=os.path.getmtime)

        self.reporte_text.insert(
            tk.END, f"Descargas realizadas en la carpeta {latest_subdir}:")
        self.reporte_text.insert(tk.END, f"{os.listdir(latest_subdir)}")

        # agregar botón para abrir la carpeta de destino
        self.open_folder_button = tk.Button(
            self.reporte_frame, text="Abrir carpeta", command=lambda: os.startfile(latest_subdir))
        self.open_folder_button.pack(side="top", padx=10, pady=10)


    def version_paress(self):
        # get operating system
        try:
            uid = os.getuid()
        except AttributeError:
            uid = ctypes.windll.shell32.IsUserAnAdmin()

        libreria = "paress2"

        try:
            local_version = parse(__import__(libreria).__version__)

            r = requests.get(f"https://pypi.org/pypi/{libreria}/json")
            pypi_version = parse(r.json()["info"]["version"])

            if local_version < pypi_version:
                messagebox.showinfo(
                    "Actualización disponible", f"Se ha encontrado una nueva versión de la librería {libreria} ({pypi_version}).\n\nSe procederá a actualizarla.")

                self.actualizacion_frame = tk.Frame(self, bg="white")
                self.actualizacion_frame.pack(
                    side="top", fill="both", expand=True)

                self.actualizacion_label = tk.Label(
                    self.actualizacion_frame, text="Actualizando librería...", font=('Times', '12'), bg="white")
                self.actualizacion_label.pack(side="top", padx=10, pady=10)

                self.actualizacion_progress_bar = ttk.Progressbar(
                    self.actualizacion_frame, orient="horizontal", length=500, mode="indeterminate")
                self.actualizacion_progress_bar.pack(
                    side="bottom", padx=10, pady=10)

                self.actualizacion_progress_bar.start()

                if uid == 0:
                    # descargar e instalar la versión más reciente de la librería
                    subprocess.call(
                        f"pip install {libreria} --upgrade", shell=True)
                else:
                    messagebox.showerror(
                        "Error", "Por favor, ejecute la aplicación como administrador para actualizar las librerías")

                self.actualizacion_progress_bar.stop()
                self.actualizacion_progress_bar.destroy()
                self.actualizacion_label.destroy()
                self.actualizacion_frame.destroy()

                messagebox.showinfo(
                    "Reiniciar aplicación", "La aplicación se reiniciará para aplicar los cambios")

                # reiniciar la aplicación
                self.restart_app()

        except AttributeError as e:
            logging.error(
                f"Error al obtener la versión de la librería {libreria}: {e}")

        except ModuleNotFoundError as e:
            logging.error(f"ModuleNotFoundError: {e}")
            raise

    def restart_app(self):
        if App.app_restarting:
            return

        script = os.path.abspath(__file__)
        args = [sys.executable, script] + sys.argv[1:]
        App.app_restarting = True
        subprocess.Popen(args)
        os.execv(sys.executable, args)

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """

        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def mostrar_errores(self, exctype, value, traceback):

        ventana = tk.Tk()
        ventana.title("Error")

        ventana.geometry("500x300")
        ventana.resizable(False, False)

        ventana.iconbitmap(self.resource_path(os.path.join(ASSETS_FOLDER, "icon.ico")))

        texto = tk.Text(ventana, height=10, width=50)
        texto.pack(expand=True, fill="both", padx=10, pady=10)

        mensaje = f"{exctype.__name__}: {value}\n\n"
        mensaje += "".join(traceback.format_tb(traceback))
        texto.insert(tk.END, mensaje)

        logging.error(mensaje)

        ventana.mainloop()


if __name__ == "__main__":
    """ app = App()
    sys.excepthook = app.mostrar_errores
    app.mainloop() """
    #print current working directory
    
