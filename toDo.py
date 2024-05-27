import sqlite3

class ToDo:

    # Constructor de la clase, el cual se encargará de esablecer la conexión con la base de datos y llamará al método encargada de crear la tabla task.
    def __init__(self):
        self.conexion = sqlite3.connect('task.db')
        self.c = self.conexion.cursor()
        self.create_table_task()

    # Método encargado de crear la tabla task en la base de datos.
    def create_table_task(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS task (
                       id INTEGER PRIMARY KEY,
                       name TEXT NOT NULL,
                       deadline TEXT NOT NULL
        );''')

    # Método encargado de añadir tareas nuevas a la base de datos.
    def add_task(self):
        name = input('Introduzca el nombre de la tarea: ')
        deadline = input('Introduzca la fecha límite: ')
        self.c.execute('INSERT INTO task (name, deadline) VALUES (?,?)', (name, deadline))
        self.conexion.commit()

    # Método encargado de mostrar una tarea específica o todas las tareas según indiquemos.
    def show_task(self):
        id = input('Introduce el id de la tarea(* para mostrar todas): ')
        if id != '*':
            self.c.execute('SELECT * FROM task WHERE id = ?', (id,))
            fila = self.c.fetchone()
            print(fila)
            return fila
        else:
            for fila in self.c.execute('SELECT * FROM task'):
                print(fila)


    def delete_task(self):
        id = input('Introduzca el id de la tarea que desea eliminar: ')
        self.c.execute('DELETE FROM task WHERE id = ?', (id,))
        self.conexion.commit()
todo = ToDo()
# todo.add_task()
todo.show_task()
todo.delete_task()
todo.show_task()