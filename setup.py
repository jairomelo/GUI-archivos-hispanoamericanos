from setuptools import setup

setup(
    name='Archivo Colectivo',
    version = '0.1.0-beta',
    description = 'Archivo Colectivo es una aplicación para ayudar a los investigadores a trabajar con archivos y repositorios digitales.',
    author = 'Jairo Antonio Melo',
    author_email = 'jairoantoniomelo@gmail.com',
    entry_points = {
        'console_scripts': [
            'ac = ac.__main__:main',
        ],
    },
    options={
        'pyinstaller': {
            'name': 'ArchivoColectivo',
            'onefile': True,
            'windowed': True,
            'icon': 'assets\\icon.ico',
            'add-data': 'assets;assets',
            'add-data': 'assets\\icon.ico',
            'add-data': 'assets\\icon.png',
            'version-file': 'version.txt',
        },
    }
    )

