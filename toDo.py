import sqlite3

class ToDo:
    # Constructor de la clase, el cual se encargará de establecer la conexión con la base de datos y llamará al método encargado de crear la tabla task.
    def __init__(self):
        self.conexion = sqlite3.connect('task.db')
        self.c = self.conexion.cursor()
        self.create_table_task()

    # Método encargado de crear la tabla task en la base de datos.
    def create_table_task(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS task (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       deadline TEXT NOT NULL
        );''')

    # Método encargado de añadir tareas nuevas a la base de datos.
    def add_task(self):
        name = input('\nIntroduzca el nombre de la tarea: ')
        deadline = input('Introduzca la fecha límite (YYYY-MM-DD): ')
        self.c.execute('INSERT INTO task (name, deadline) VALUES (?,?)', (name, deadline))
        self.conexion.commit()
        print("\nTarea añadida con éxito\n")

    # Método encargado de mostrar una tarea específica o todas las tareas según indiquemos.
    def show_task(self):
        id = input('\nIntroduce el id de la tarea(* para mostrar todas): ')
        if id != '*':
            self.c.execute('SELECT * FROM task WHERE id = ?', (id,))
            fila = self.c.fetchone()
            if fila:
                print(f"\n{fila}\n")
            else:
                print("\nNo se encontró la tarea con el id proporcionado\n")
        else:
            print("\nTodas las tareas:")
            for fila in self.c.execute('SELECT * FROM task'):
                print(fila)
            print()

    # Método encargado de verificar si una tarea existe por ID.
    def task_exists(self, id):
        self.c.execute('SELECT * FROM task WHERE id = ?', (id,))
        return self.c.fetchone() is not None

    # Método encargado de eliminar una tarea de la base de datos.
    def delete_task(self):
        id = input('\nIntroduzca el id de la tarea que desea eliminar: ')
        
        if not self.task_exists(id):
            print("\nNo se encontró la tarea con el id proporcionado\n")
            return

        self.c.execute('DELETE FROM task WHERE id = ?', (id,))
        self.conexion.commit()
        print("\nTarea eliminada con éxito\n")

    # Método encargado de actualizar el nombre y la fecha límite de una tarea existente.
    def update_task(self):
        id = input('\nIntroduce el id de la tarea que desea actualizar: ')
        
        if not self.task_exists(id):
            print("\nNo se encontró la tarea con el id proporcionado\n")
            return

        new_name = input('Introduzca el nuevo nombre de la tarea: ')
        new_deadline = input('Introduzca la nueva fecha límite (YYYY-MM-DD): ')
        self.c.execute('UPDATE task SET name = ?, deadline = ? WHERE id = ?', (new_name, new_deadline, id))
        self.conexion.commit()
        print("\nTarea actualizada con éxito\n")

    # Método encargado de mostrar el menú y gestionar la interacción con el usuario.
    def menu(self):
        while True:
            print("\n--- Menú ---")
            print("1. Añadir tarea")
            print("2. Mostrar tarea(s)")
            print("3. Actualizar tarea")
            print("4. Eliminar tarea")
            print("5. Salir")
            choice = input("\nSeleccione una opción: ")

            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.show_task()
            elif choice == '3':
                self.update_task()
            elif choice == '4':
                self.delete_task()
            elif choice == '5':
                print("\nSaliendo del programa...\n")
                break
            else:
                print("\nOpción no válida. Inténtelo de nuevo.\n")

# Crear una instancia de la clase ToDo y mostrar el menú
todo = ToDo()
todo.menu()


