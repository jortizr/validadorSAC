#instalacion del ambiente virtual
python -m venv venv

#activador de la consola 
venv\Scripts\activate.bat

#instalar flet
pip install flet

#crear el archivo de requerimientos
pip freeze > requirements.txt 