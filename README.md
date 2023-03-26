# Archivo Colectivo: Un aplicativo para la gestión de archivos digitalizados de hispanoamérica

## Descripción

Este proyecto busca facilitar la colección, organización, visualización, manipulación y sistematización de archivos digitalizados de hispanoamérica. El proyecto se encuentra en una fase preliminar de desarrollo, por lo que no se encuentra disponible para su uso público.

## Objetivos

El proyecto tiene como objetivo central facilitar la gestión de archivos digitalizados de hispanoamérica. Para ello, se busca crear una aplicación de escritorio que sirva como una mezcla de recolector de información, gestor de archivos y visualizador de documentos. La aplicación debe permitir la descarga de archivos provenientes de los archivos hispanoamericanos, via API o por descarga automatizada (de preferencia la primera). Además, debe permitir la organización de los archivos en carpetas, la visualización de los archivos en un visor de documentos, la edición de metadatos y la creación de un índice de los archivos digitalizados.

En cierta medida, es una combinación de ideas ya establecidas como [Tropy](https://tropy.org/), [Zotero](https://www.zotero.org/) y [Calibre](https://calibre-ebook.com/). Sin embargo, la aplicación debe ser diseñada para la gestión de archivos digitalizados de hispanoamérica, por lo que debe ser capaz de manejar archivos de diferentes formatos como PDF e imágenes.

## Prototipado

En este momento se está desarrollando un prototipo de la aplicación a partir de una interface de usuario para Windows creada en Python y que únicamente tiene el propósito de facilitar la interacción con la librería [paress2](https://pypi.org/project/paress2/)

### Probar el prototipo (solo Windows)

La manera más fácil de probar el prototipo es descargar la [última version](https://github.com/jairomelo/GUI-archivos-hispanoamericanos/releases/tag/v0.1.0-beta), descomprimir el archivo *.zip e instalar el programa. ⚠️ Debido a que el prototipo aún no está [firmado](https://en.wikipedia.org/wiki/Code_signing), Windows puede mostrar un mensaje de advertencia al ejecutar el programa. Asimismo, Chrome puede mostrar un mensaje de advertencia al descargar el archivo. En ambos casos, se recomienda desactivar temporalmente la protección de Windows Defender y Chrome, respectivamente.

### Probar el prototipo desde el código fuente

Para ejecutar el prototipo desde el código fuente, se debe tener instalado Python 3.8 o superior. 

Antes de ejecutar el código, se debe instalar las dependencias del proyecto. Para ello, se debe abrir una terminal en el directorio `GUI-archivos-hispanoamericanos` y ejecutar el siguiente comando:

```bash
pip install -r requirements.txt
```

El archivo a ejecutar se encuentra en el directorio `archivo_colectivo` y se llama `__main__.py`. Para ejecutarlo, se debe abrir una terminal en el directorio `archivo_colectivo` y ejecutar el siguiente comando:

```bash
python __main__.py
```

También es factible ejecutar directamente este prototipo con el ejecutable `start.exe` que se encuentra en la raíz del proyecto, aunque puede ser tardado porque evalúa las versiones de Python instaladas en el sistema e intenta crear un entorno virtual con la versión más reciente.

## Contribuciones

En este momento, el proyecto se encuentra en una etapa activa de prototipado. Las contribuciones son bienvenidas, pero se recomienda que antes de realizar cualquier cambio me envíen un mensaje para discutir el cambio.

## Tareas inmediatas

- [ ] Encontrar una opción para la firma del código fuente que permita la distribución de la aplicación, pero que no requiera de un pago mensual.
- [ ] Compilar el código en un ejecutable para OS X y Linux (Ubuntu y Debian).
- [ ] Crear una base de datos para almacenar los metadatos de los archivos digitalizados.
- [ ] Decidir si continuar con la interfaz de usuario actual o crear una nueva. Esto incluye probar otras librerías como [PySide2](https://pypi.org/project/PySide2/) o [PyQt5](https://pypi.org/project/PyQt5/) y otros lenguajes como Electron o React.
