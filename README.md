# RCC-FICO-SCORE-PLD API Client  

## Requisitos

 - Python >= 3.9.16
 - pip
 - System Linux/Unix
 - Git

### Dependencias adicionales

Se debe contar con las siguientes dependencias:
- openssl ~ 3.0.7
- python cryptography ~ 41.0.2
- python requests ~ 2.31.0

```sh
# Para RHEL o derivados:
yum install openssl
dnf install openssl

# Para Debian o derivados:
apt install openssl
```
```sh
pip install cryptography
pip install requests
```
  

## Guía de inicio

### Paso 1. Clonar repositorio
Clona este repositorio en tu sistema Linux/Unix
Utiliza el siguiente comando:
```sh
git clone <nombre_del_repositorio>
```

### Paso 2. Generar llaves criptográficas

 - Ejecuta el archivo *crypto_keys_generator.sh* desde la línea de comandos de su sistema Unix/Linux
 - Resguardar en una bóveda segura la contraseña elegida para el keystore durante la ejecución del archivo *crypto_keys_generator.sh*
 - Identifica el directorio generado donde se guardaron las llaves generadas

### Paso 3. Descarga el certificado público de Círculo de Crédito

 1. Ingresa al portal de desarrolladores
 2. Inicia sesión en el portal
 3. Descarga el certificado

  

### Paso 4. Agrega tus credenciales para poder invocar el API

 - Identifica la clase *ApiRccFicoScorePld* en el módulo *rcc_fico_score_pld_test.py*.
 - Edita la clase agregando la ruta de los archivos con las llaves criptográficas así como tus credenciales para consumir el API .

```python
# ...
class  ApiRccFicoScorePld:
	def  __init__(self):
		# API cryptographic keys
		self.public_cert_path = "/your-path/cdc_cert_xxxx.pem"
		self.pkcs12_path = "/your-path/keystore.p12"
		self.pkcs12_password = "your-keystore-password"

		# API credentials
		self.api_username = "your-username"
		self.api_password = "your-password"
		self.api_key = "your-api-key"
# ...
```

### Paso 5. Consumir el API RCC-FICO-SCORE-PLD

En la clase *ApiRccFicoScorePld* descomenta el método correspondiente para llamar el método deseado del API.

```python
# ...
api = ApiRccFicoScorePld()
#api.retrieve_rcc()
#api.retrieve_credits()
#api.retrieve_addresses()
#api.retrieve_jobs()
#api.retrieve_queries()
#api.retrieve_scores()
#api.retrieve_messages()
# ...
```

Ejecuta el archivo rcc_fico_score_pld_test.py
```ssh
python3 rcc_fico_score_pld_test.py
```

[CONDICIONES DE USO, REPRODUCCIÓN Y DISTRIBUCIÓN](https://github.com/APIHub-CdC/licencias-cdc)