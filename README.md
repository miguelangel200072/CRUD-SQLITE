# CRUD-SQLITE
Programa para la gestión de tareas con Python y SQLITE
## Descripción

**ToDo List Manager** es una aplicación de gestión de tareas simple y eficaz, desarrollada en Python utilizando SQLite como sistema de base de datos. El propósito de esta aplicación es permitir a los usuarios gestionar sus tareas diarias de manera organizada, almacenando información sobre cada tarea en una base de datos local.

### Funcionalidades Clave

- **Añadir Tareas**: Permite a los usuarios crear nuevas tareas especificando un nombre y una fecha límite.
- **Mostrar Tareas**: Ofrece la posibilidad de ver una tarea específica mediante su ID o listar todas las tareas almacenadas en la base de datos.
- **Actualizar Tareas**: Facilita la modificación del nombre y/o la fecha límite de una tarea existente.
- **Eliminar Tareas**: Permite borrar tareas de la base de datos mediante su ID.

El proyecto está diseñado para ser un ejemplo claro y funcional de cómo manejar tareas básicas en una base de datos, y se puede extender para incluir características adicionales como recordatorios, categorización de tareas, y más.

## Configuración y ejecución

Para comenzar a utilizar la aplicación **ToDo List Manager**, sigue estos pasos:

### Instalación

1. Clona el repositorio a tu máquina local:
    ```bash
    git clone https://github.com/miguelangel200072/CRUD-SQLITE.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd CRUD-SQLITE
    ```

### Requisitos

Asegúrate de tener Python 3.x instalado en tu sistema. La aplicación utiliza SQLite, que viene preinstalado con Python, por lo que no necesitas instalar ningún paquete adicional.

### Ejecución

1. **Ejecuta el archivo principal**: Para iniciar la aplicación, ejecuta el siguiente comando en tu terminal:
    ```bash
    python3 todo.py
    ```
2. **Interactúa con el menú**: La aplicación te presentará un menú interactivo con las siguientes opciones:
    - **1. Añadir tarea**: Permite crear una nueva tarea proporcionando un nombre y una fecha límite.
    - **2. Mostrar tarea(s)**: Muestra una tarea específica por ID o todas las tareas si introduces `*`.
    - **3. Actualizar tarea**: Actualiza el nombre y/o la fecha límite de una tarea existente.
    - **4. Eliminar tarea**: Elimina una tarea específica proporcionando su ID.
    - **5. Salir**: Termina la aplicación.

### Ejemplo de Uso

1. **Añadir una tarea**:
    - Selecciona la opción 1.
    - Introduce el nombre de la tarea y la fecha límite (formato `DD-MM-YYYY`).

2. **Mostrar tareas**:
    - Selecciona la opción 2.
    - Introduce un ID para ver una tarea específica o `*` para ver todas las tareas.

3. **Actualizar una tarea**:
    - Selecciona la opción 3.
    - Introduce el ID de la tarea que deseas actualizar, seguido del nuevo nombre y la nueva fecha límite.

4. **Eliminar una tarea**:
    - Selecciona la opción 4.
    - Introduce el ID de la tarea que deseas eliminar.

### Notas Adicionales

- Los datos se almacenan en un archivo de base de datos llamado `task.db`, que se crea automáticamente en el directorio del proyecto.
- Asegúrate de introducir la fecha límite en el formato `DD-MM-YYYY` para evitar errores.

Para más detalles sobre la estructura del proyecto y el código, consulta el archivo `todo.py` en el repositorio.
