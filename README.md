# DOCUMENTACION PROYECTO :dart::octocat:

Proyecto desarrollado con el fin de modernizar el proceso de cifrado y descifrado de archivos haciendo uso de la librería pgp free llamada gnupg o gpg.

## 1. Nombre :computer:

Cifrado y Decifrado de Archivos con OpenPGP

## 2. Descripción 	:bookmark_tabs:

Este proyecto tiene como objetivo reemplazar la arquitectura actual de cifrado mediante cryptovault, modernizando el cifrado y la transferencia de información mediante el uso de librerias pgp, estandarizando el proceso para el uso en multicloud.

## 3. Instalación :jigsaw:

Usamos el package manager [pip](https://pip.pypa.io/en/stable/) para instalar la libreria pgp.

```bash
pip install python-gnupg
```

Instalar en el entorno virtual las herramientas google.

```bash
pip install --upgrade google-cloud-storage

pip install google-cloud-secret-manager
```

Actualizar las herramientas de python instaladas.

```bash
pip install --upgrade setuptools
```

## 4. Despliegue Cloud Functions:  :writing_hand:

1. Creación del trigger "activador".

    1.1 Creación de Topicos Pub/Sub para crear los trigger de las funciones de cifrado y descifrado.
    ```bash
    gcloud pubsub topics create projects/gcp-st-transit-multi-cloud/topics/gcp-st-tmc-trigger-to-encrypt

    gcloud pubsub topics create projects/gcp-st-transit-multi-cloud/topics/gcp-st-tmc-trigger-to-decrypt
    ```

    1.2 Crear la notificación asociada al topico del Pub/Sub creado en el paso anterior.
    ```bash
    gsutil notification create -f json -t projects/gcp-st-transit-multi-cloud/topics/gcp-st-tmc-trigger-to-encrypt -p export-lab-digital -e OBJECT_FINALIZE -e OBJECT_METADATA_UPDATE gs://export-zone-cds

    gsutil notification create -f json -t projects/gcp-st-transit-multi-cloud/topics/gcp-st-tmc-trigger-to-decrypt -p import-lab-digital -e OBJECT_FINALIZE -e OBJECT_METADATA_UPDATE gs://gcp-aws-import-zone
    ```

2. Crear los secretos subiendo las llaves publica y privada de pgp (Area llaves y criptogramas).
```txt
gcp-st-tmc-gpg-pb
gcp-st-tmc-gpg-pv
```

3. Creación de la service_accounts.

    3.1 Asignar permisos de multiproyecto.
```txt
Agente de servicio de Cloud Functions
Usuario de cuenta de servicio
```

    3.2 Asignar permisos en los servicios.
```txt
Administrador de objetos de Storage
Usuario con acceso a secretos de Secret Manager
Visualizador del administrador de secretos
```

4. Creación de las Cloud Functions: :electron:

    **Nota:** El cifrado tendra un topico de Pub/Sub activador y una cloud functions y el decifrado tendra otro topico de Pub/Sub activador y una cloud functions respectivamente.

    4.1 Para el despliegue en cloud functions se utiliza la versión de python 3.9 de lo contrario no logra instalar las librerias declaradas en el archivo requirements.txt

    4.2 Subir solo los scripts usados mediante importación de librerias en los main de cifrado y descifrado.

    4.3 En el despliegue de la cloud functions debe remplazar los scripts *main_cloud_encrypt.py*  y *main_cloud_decrypt.py* por *main.py* y con punto de entrada *main* respectivamente.

    4.4 Deshabilitar la opción de reintento en caso de error.

    4.5 Usar una memoria de 512 MB (Depende del tamaño de archivos a procesar).

    4.6 Usar instancias de 1 a 100.

    4.7 Usar tiempo de espera de 60 segundos.

    4.8 Usar la service_accounts habilitada para usarse en los proyectos de GCP (ver punto 3).

    4.9 Crear variables de entorno.

    ```bash
    #email de la key pgp a usar
    export NAME_EMAIL= 'agalin1@gmail.com.co'
    
    #path de la ubicación del json service_accounts
    export GOOGLE_APPLICATION_CREDENTIALS='C:\Users\crist\OneDrive\Escritorio\Proyectos\BdB\service_accounts\gcp-st-transit-multi-cloud-a2191790c572.json'--linux

    #Id de los proyectos gcp
    export PROJECT_ID_A='gcp-st-transit-multi-cloud'
    export PROJECT_ID_B='gcp-de-cds'

    #nombre del bucket cloud function cifrar
    export BUCKET_TO_ENCRYPT_IN='export-zone-cds'
    export BUCKET_ENCRYPTED_OUT='gcp-aws-export-zone'
    export BUCKET_TO_ENCRYPT_OLD='export-zone-cds-backup'

    #nombre del bucket cloud function decifrar
    export BUCKET_TO_DECRYPT_IN='gcp-aws-import-zone'
    export BUCKET_DECRYPTED_OUT='import-zone-cds'
    export BUCKET_TO_DECRYPT_OLD='gcp-aws-import-zone-backup'

    #Id del proyecto donde esta el SM
    export ID_PROJECT_SECRET='553319150162'

    #Id del secreto publico
    export SECRET_ID_PB= 'gcp-st-tmc-gpg-pb'
    #Id del secreto privado
    export SECRET_ID_PV='gcp-st-tmc-gpg-pv'
    #password de la key pgp privada
    export SECRET_ID_PSW='gcp-st-tmc-gpg-psw'

    #Usuario
    export CLIENT='import-lab-digital' #'import-adl'
    ```

    4.10. Verificar existencia de las variables de entorno creadas:

    ```bash
    echo $NAME_EMAIL
    ```

    **Nota:** Si no se crean estas variables de entorno el sistema arrojara el siguiente error.

    ```bash
    TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'

    TypeError: str expected, not NoneType
    ```


## 5. Lógica del Desarrollo: :electron:

*./app/main_onprimese_encrypt.py*

Este scrypt es el que se desplegara en onprimese, el cual cumple con la función de listar todos los archivos planos con extensión ***.txt o .csv*** que se encuentren en los diferentes subniveles de carpetas de la carpeta ***./in***. Una vez se listan los archivos se invoca la función de encriptación la cual toma la llave pgp declarada y cifra los archivos y los almacena en la carpeta ***./encrypted*** para su posterior trasferencia al bucket del cloud.

*./app/main_cloud_decrypt.py*

Este scrypt es el que se desplegara en cloud, el cual cumple con la función de acceder al secreto que contiene la llave privada, posteriormente invoca la función de importación de la llave capturada y realiza la intalación de esta en el llavero con su respectivo certificado de confianza. Luego se genera el listado de los archivos encriptados con extensión ***.pgp o .gpg*** que se encuentren en los diferentes subniveles de carpeta en el bucket activador ***BUCKET_TO_DECRYPT_IN***.
Una vez se listan los archivos se invoca la función de desencripción la cual toma la llave pgp declarada junto con el passphrase y descifra los archivos y los almacena en la carpeta ***BUCKET_DECRYPTED_OUT*** alojada en el bucket del cloud. El archivo original es movida a la carpeta ***BUCKET_TO_DECRYPT_OLD*** limpiando la capeta in.

**Nota:** Este scrypt en el despliegue de la cloud functions debe remplazarce por *main.py* y con punto de entrada *main*.

*./app/main_cloud_encrypt.py*

Este scrypt es el que se desplegara en cloud, el cual cumple con la función de acceder al secreto que contiene la llave publica, posteriormente invoca la función de importación de la llave capturada y realiza la intalación de esta en el llavero con su respectivo certificado de confianza. Luego se genera el listado de los archivos en claro que se encuentren en los diferentes subniveles de carpeta en el bucket activador ***BUCKET_TO_ENCRYPT_IN***.
Una vez se listan los archivos se invoca la función de encripción la cual toma la llave pgp declarada y cifra los archivos y los almacena en la carpeta ***BUCKET_ENCRYPTED_OUT*** alojada en el bucket del cloud. El archivo original es movida a la carpeta ***BUCKET_TO_ENCRYPT_OLD*** limpiando la capeta in.


**Nota:** Este scrypt en el despliegue de la cloud functions debe remplazarce por *main.py* y con punto de entrada *main*.


## 6. Roadmap - Ideas :roller_coaster:
* [x] Realizar un desarrollo con programación orientada a objetos.

* [x] Cambiar las variables quemadas en codigo por variables de entorno.

* [x] Realizar un desarrollo para ejecución en Onprimese y  Cloud.
  
* [x] Implementar consumo de llaves alojadas en secret manager de gcp.

* [x] Interacción de servicios multiproyecto.

* [ ] Generar integración para pruebas unitarias.

## 7. Autor :technologist:
Cristian Beltrán -- Data Engineer

## 8. Referencias :books:
> SaltyCrane Blog (2012). [saltycrane.com](https://www.saltycrane.com/blog/2011/10/python-gnupg-gpg-example/#:~:text=python%2Dgnupg%20is%20a%20Python,see%20the%20python%2Dgnupg%20documentation)

> Python Hosted (2017). [pythonhosted.org](https://pythonhosted.org/python-gnupg/#encryption)

> It's Foss (2021). [itsfoss.com](https://itsfoss.com/gpg-encrypt-files-basic/#:~:text=When%20you%20encrypt%20a%20file,not%20given%20out%20to%20anyone.)

> Read the Docs (2022). [gnupg.readthedocs.io](https://gnupg.readthedocs.io/en/latest/)

## 9. Estado del Proyecto - Fases Devops :construction:
* [x] Fase de Planeación (Entendimiento del brief. Roadmap)
* [x] Fase de Construcción (Generación de Diseño y Código del desarrollo)
* [x] Fase de Integración Continua (Testeo, calidad con sonar. Pruebas unitarias)
* [ ] Fase de Implementación o Despliegue continuo (Instalación en los ambientes qa, staging, production con github actions)
* [ ] Fase de Gestionar
* [ ] Fase de Feedback Continuo (Retroalimentación Cliente y Usuario)
