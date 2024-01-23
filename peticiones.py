import requests
from bs4 import BeautifulSoup

# Paso 1: Hacer la petición a la URL
url = 'http://wsa/sato/detalleguia.aspx?guia=014134483245'
response = requests.get(url)

# Verificar si la petición fue exitosa (código de estado 200)
if response.status_code == 200:
    # Paso 2: Parsear el contenido HTML de la respuesta
    soup = BeautifulSoup(response.text, 'html.parser')
    
# Paso 3: Buscar y extraer elementos por su ID
    # Supongamos que el ID que estás buscando es 'mi_elemento_id'
    elemento_con_id = soup.find(id='dtlGuias_ctl00_lblEstadoN')
    print(elemento_con_id)
    # Verificar si se encontró el elemento
    if elemento_con_id:
        # Acceder al atributo 'value' del elemento por su ID
        contenido = elemento_con_id.text
        print(f'Valor del elemento con ID "mi_elemento_id": {contenido}')
    else:
        print('no se encontro resultado de la guia')

else:
    print(f'Error al hacer la petición. Código de estado: {response.status_code}')