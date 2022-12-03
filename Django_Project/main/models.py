import pymysql
#definimos un objetos Base de datos
class Database():
    #creamos el constructor con la bbdd elegida a traves de pymysql
    def __init__(self):
        self.connection = pymysql.connect(
        host='localhost',
        user='user',
        password='123test456',
        db='Proyecto'
    ) 
    #chequeo que la bbdd este en funcionamiento, sino no se conecta
    #y lanza un error (no llega al print)
        self.cursor = self.connection.cursor()
        print("La conexion fue exitosa")
    
    #METODOS
    def get_user_bymail (self, email):
        query = f"SELECT * FROM Usuarios WHERE Email = ('{email}')"
        self.cursor.execute(query)
        user = self.cursor.fetchall()
        return user

    """  INSERT INTO Parques (Capacidad_fastpass, Capacidad_normal, Nombre, Ubicacion) VALUES (5, 10, 'Magic Kingdom', 'Florida');    
    INSERT INTO Parques (Capacidad_fastpass, Capacidad_normal, Nombre, Ubicacion) VALUES (5, 10, 'Animal Kingdom', 'Florida');
    INSERT INTO Parques (Capacidad_fastpass, Capacidad_normal, Nombre, Ubicacion) VALUES (5, 10, 'Hollywood Studios', 'Florida');
    INSERT INTO Parques (Capacidad_fastpass, Capacidad_normal, Nombre, Ubicacion) VALUES (5, 10, 'EPCOT', 'Florida'); """
    def add_user (self, apellido, email, nombre, password):
        query= f"INSERT INTO Usuarios (Apellido, Email, Nombre, Password, Usuario) VALUES ('{apellido}', '{email}', '{nombre}', '{password}', 1);" 
        try: 
            self.cursor.execute(query) 
            self.connection.commit()
        except Exception as e: 
            print("INSERT ERROR") 
            raise 

        return

    #hacemos el checkeo en views
    def modify_user (self, new_apellido, new_nombre, new_password, email):
        query= f"UPDATE Usuarios SET Apellido = '{new_apellido}', Nombre = '{new_nombre}', Password = '{new_password}' WHERE Email = '{email}';"
        try: 
            self.cursor.execute(query) 
            self.connection.commit()
        except Exception as e: 
            print("UPDATE ERROR") 
            raise 

        return


    #date = yyyy-mm-dd
    def get_normal_tickets (self, date, parque):
        query= f"""SELECT COUNT(*) FROM Entradas WHERE Fecha = '{date}' 
                AND FK_Parque = (SELECT id_Parque FROM Parques WHERE Nombre = '{parque}')
                AND FK_Tipo_Entrada = (SELECT id_Tipo_Entrada FROM Tipo_Entrada WHERE Tipo = 'normal');"""
        try: 
            self.cursor.execute(query) 
            count_normal = self.cursor.fetchall()
            return count_normal
        except Exception as e: 
            print("ERROR") 
            raise 


    def get_fast_tickets (self, date, parque):
        query= f"""SELECT COUNT(*) FROM Entradas WHERE Fecha = '{date}' 
                AND FK_Parque = (SELECT id_Parque FROM Parques WHERE Nombre = '{parque}')
                AND FK_Tipo_Entrada = (SELECT id_Tipo_Entrada FROM Tipo_Entrada WHERE Tipo = 'fast');"""
        try: 
            self.cursor.execute(query) 
            count_fast = self.cursor.fetchall()
            return count_fast
        except Exception as e: 
            print("ERROR") 
            raise 

    def get_capacity (self, parque):
        query= f"SELECT Capacidad_normal, Capacidad_fastpass FROM Parques WHERE Nombre = '{parque}';"
        try: 
            self.cursor.execute(query) 
            capacity = self.cursor.fetchall()
            return capacity
        except Exception as e: 
            print("ERROR") 
            raise 
    
    

