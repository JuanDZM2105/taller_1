# Quicker Ticket Assistant (QTA)
## Description
QTA is a help desk management system designed for companies working with medical devices. The application's goal is to establish order in the flow of calls received by companies. Additionally, it aims to automate the way companies handle their tickets.

## Usage Instructions
To run the project, make sure you have the following installed:

* **Python**
* **Django**
* **matplotlib**

Follow these steps:

### 1. Clone the project from GitHub:
```bash
git clone https://github.com/jmmunozg1/QTAProject.git
```
### 2. Navigate to the project directory:
```bash
cd QTAProject
```
### 3. Start the server:
```bash
python manage.py runserver
```
### 4. Open your browser and go to http://localhost:8000 to access the application.


## How to Contribute
If you would like to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch for your contribution.
3. Make the changes and be sure to follow the project's style guidelines.
4. Submit a pull request.

## Contact
For any inquiries or suggestions, please contact us at camazog1@eafit.edu.co, jdzapatam@eafit.edu.co,  jmmunozg1@eafit.edu.co or open an issue on GitHub.



## Quality Attributes Analysis

### 1. Usabilidad

#### Aspectos positivos:
- La interfaz está dividida por vistas claras (home, about, mainscreen, ticket, stadistics), lo que facilita la navegación del usuario y al entrar a la pagina es agradable a la vista e intuitiva

#### Aspectos a mejorar:
- No hay validación de formularios del lado del cliente (JS) ni del servidor (Django Forms o ModelForms), lo que puede llevar a errores.

- La interfaz podría beneficiarse de un diseño más amigable (UI/UX), especialmente para usuarios no técnicos.

- Algunos nombres de campos (por ejemplo Support_name, id_unico) pueden confundir al usuario.

- En cuanto al diseño, la interfaz no está adaptada para distintos tamaños de pantalla, lo que limita su uso principalmente a dispositivos de escritorio y dificulta su accesibilidad desde celulares o tablets.

-  no se ha implementado un sistema para registrar nuevos usuarios desde la aplicación web. Esto obliga a crear cuentas manualmente desde la terminal, lo cual representa una barrera significativa para usuarios sin conocimientos técnicos

### 2. Compatibilidad

#### Aspectos positivos:
- Proyecto basado en Django, un framework ampliamente compatible con múltiples sistemas operativos y bases de datos.

- Se utilizan bibliotecas estándar (pandas, matplotlib, etc.) que permiten migrar el sistema fácilmente entre entornos.

#### Aspectos a mejorar:
- La generación de gráficos se hace en el backend y se guarda como imágenes estáticas. Esto puede no funcionar correctamente si se despliega en servicios sin sistema de archivos persistente.

- No se usa ningún frontend responsivo o adaptativo, lo cual limita su uso en dispositivos móviles.

- no se proporciona un archivo con los requerimentos para poder correr la aplicación.


### 3. Rendimiento
#### Aspectos positivos:
- Consultas simples a la base de datos (filter, all) permiten obtener rápidamente la información.

- Uso de pandas permite análisis eficiente de datos en memoria.

#### Aspectos a mejorar:
- La vista mainscreen escribe todo el archivo ticketData.csv cada vez que se carga. Esto es costoso y no escalable.

- La generación de múltiples gráficos en cada request (stadistics) puede saturar el servidor con muchos usuarios concurrentes.


### 4. Seguridad

#### Aspectos positivos:
- Uso de @login_required en vistas importantes garantiza acceso controlado.

- Se utiliza logout() correctamente para cerrar sesión de forma segura.

#### Aspectos a mejorar:

- No hay validación de datos antes de guardarlos (ej. en ticket, more_info) → riesgo de inyección o corrupción de datos.

- call_time se convierte desde un string manualmente, lo que puede generar errores o permitir manipulación maliciosa.

