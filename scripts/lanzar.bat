@echo off

setlocal enableDelayedExpansion

set "python-versions=3.8 3.9 3.10 3.11"

for %%v in (%python-versions%) do (
  echo.
  echo Trying Python version %%v...
  echo.
  py -%%v -m venv acenv
  if not errorlevel 1 (
    call acenv\Scripts\activate.bat
    if not errorlevel 1 (
      pip install -r ../requirements.txt
      if not errorlevel 1 (
        echo.
        echo Ejecutando archivo colectivo...
        echo.
        python ../archivo_colectivo/__main__.py
        endlocal
        exit /b
      )
    )
  )
)

echo.
echo No se pudo crear el entorno virtual con ninguna versión de Python válida.
echo Por favor, instale Python 3.8 o superior e inténtelo de nuevo.
echo.
endlocal
exit /b
