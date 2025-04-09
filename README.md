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



## Analisis de atributos de calidad

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


## Refactorización: Aplicación del Principio de Inversión de Dependencias (DIP) en la vista stadistics

### ¿Qué se cambió?
Se refactorizó la función de vista stadistics en el archivo views.py para desacoplar la lógica de generación de estadísticas del controlador (view).
Anteriormente, toda la lógica de negocio (consulta de tickets, generación de estadísticas, creación de gráficas, etc.) estaba directamente implementada dentro de la vista.

Ahora, se ha aplicado el principio de inversión de dependencias dividiendo el código en tres componentes principales:

- Interfaz IStatisticsService (definida en statistics_interface.py) que declara el método generate_statistics.

- Implementación concreta StatisticsService (en statistics_service.py) que implementa la lógica de generación de estadísticas.

- Vista stadistics (en views.py) que ahora delega la lógica al servicio a través de la interfaz.

### ¿Por qué se hizo este cambio?
Se aplicó este principio por las siguientes razones:

- Desacoplamiento	La vista ya no depende directamente de una clase concreta ni contiene lógica de negocio.
- Testabilidad	Se facilita la creación de pruebas unitarias, ya que ahora se puede inyectar una implementación mock de IStatisticsService en lugar de depender de datos reales.
- Reutilización	La lógica de estadísticas puede ser usada en otros contextos (APIs, scripts, tareas programadas) sin duplicar código.
- Mantenibilidad	Permite modificar o extender la lógica sin tocar la vista, respetando el principio de abierto/cerrado.

### ¿Cómo se implementó?
- Creación de la interfaz IStatisticsService con el método abstracto generate_statistics.

- Implementación de StatisticsService, que concentra toda la lógica

- Refactorización de la vista stadistics para recibir como dependencia una instancia de IStatisticsService, que por defecto es StatisticsService.

- Organización del código en módulos separados para facilitar su mantenimiento.



---

## 5.Implementación de Patrones de Diseño en el Proyecto de Django

## Patrones Implementados:

### Normalización de Modelos

#### **Decisión detrás del patrón**:
La **normalización de modelos** se eligió como patrón para mejorar la estructura de los datos en la base de datos, eliminando redundancias y mejorando la integridad de los datos. En el modelo original de `Ticket`, había campos redundantes como `first_follow_up`, `second_follow_up`, y `third_follow_up`, que se podían gestionar de una manera más eficiente mediante la creación de un modelo separado para los seguimientos.

Este patrón fue elegido para garantizar que los datos estuvieran mejor estructurados, con relaciones claras entre los modelos y sin duplicación innecesaria de información. Además, facilita la escalabilidad del sistema, ya que permite agregar más seguimientos sin tener que modificar la estructura del modelo `Ticket`.

#### **Implementación del patrón**:
- **Modelo Original**: El modelo `Ticket` contenía múltiples campos para almacenar los seguimientos (`first_follow_up`, `second_follow_up`, `third_follow_up`).
- **Refactorización**: Se creó un nuevo modelo `FollowUp` para manejar los seguimientos de manera más flexible. Cada instancia de `Ticket` ahora tiene múltiples instancias del modelo `FollowUp` relacionadas con él. Esto elimina la redundancia y hace que el sistema sea más fácil de mantener y ampliar en el futuro.

**Código del modelo `FollowUp`:**

```python
class FollowUp(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='follow_ups')
    follow_up_time = models.DateTimeField(default=now)
    follow_up_text = models.CharField(max_length=500, blank=True, default="")
    follow_up_type = models.CharField(max_length=50, blank=True, default="")
```

**Modificaciones en el modelo `Ticket`:**

```python
class Ticket(models.Model):
    # Otros campos...
    first_follow_up = models.ForeignKey('FollowUp', on_delete=models.CASCADE, related_name='first_follow_up', blank=True, null=True)
    second_follow_up = models.ForeignKey('FollowUp', on_delete=models.CASCADE, related_name='second_follow_up', blank=True, null=True)
    third_follow_up = models.ForeignKey('FollowUp', on_delete=models.CASCADE, related_name='third_follow_up', blank=True, null=True)
```

#### **Mejora en la implementación**:
La creación del modelo `FollowUp` permite que los seguimientos sean gestionados de manera más eficiente y flexible. Si en el futuro se requieren más seguimientos, solo será necesario agregar más instancias del modelo `FollowUp`, sin necesidad de modificar la estructura del modelo `Ticket`.

---

### Vistas CRUD para Controladores

#### **Decisión detrás del patrón**:
El patrón **CRUD para controladores** se eligió porque las vistas de la aplicación siguen un flujo básico de creación, lectura, actualización y eliminación de recursos. Este patrón permite organizar el código de manera más limpia y modular, utilizando las vistas basadas en clases (CBV) que Django proporciona.

Las vistas CRUD son esenciales en aplicaciones donde se manejan entidades que se pueden crear, leer, actualizar y eliminar. En lugar de escribir vistas tradicionales de función (FBV) para cada acción, las vistas basadas en clases proporcionan un marco estructurado y reutilizable, lo que facilita el mantenimiento y la ampliación del sistema.

#### **Implementación del patrón**:
En el archivo `views.py`, se implementaron las vistas CRUD utilizando las vistas basadas en clases (CBV) para manejar las operaciones sobre el modelo `Ticket`. Estas incluyen:

- **ListView** para mostrar todos los tickets.
- **CreateView** para crear un nuevo ticket.
- **UpdateView** para editar un ticket existente.
- **DeleteView** (agregada posteriormente) para eliminar un ticket.

**Código de la vista `TicketListView`:**

```python
class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'mainscreen.html'
    context_object_name = 'tickets'
```

**Código de la vista `TicketCreateView`:**

```python
class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    template_name = 'ticket.html'
    fields = ['call_time', 'priority', 'discussion', 'state', 'place', 'equipment', 'contact_number', 'contact_name']
    success_url = reverse_lazy('mainscreen')
```

**Código de la vista `TicketUpdateView`:**

```python
class TicketUpdateView(LoginRequiredMixin, UpdateView):
    model = Ticket
    template_name = 'more_info.html'
    fields = ['Support_name', 'first_follow_up', 'second_follow_up', 'third_follow_up', 'state']
    success_url = reverse_lazy('mainscreen')
```

**Código de la vista `TicketDeleteView` (agregada posteriormente):**

```python
class TicketDeleteView(LoginRequiredMixin, DeleteView):
    model = Ticket
    template_name = 'ticket_confirm_delete.html'
    success_url = reverse_lazy('mainscreen')
```

#### **Mejora en la implementación**:
El uso de vistas basadas en clases (CBV) permite que la lógica de cada operación CRUD esté organizada de forma modular y reutilizable. Además, la implementación de `TicketDeleteView` completa el patrón CRUD, permitiendo eliminar tickets de manera segura.






