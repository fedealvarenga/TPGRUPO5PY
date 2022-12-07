import pymysql
import sys

sistema_operativo=sys.platform
#definimos un objetos Base de datos
class Database():
    #creamos el constructor con la bbdd elegida a traves de pymysql
    def __init__(self):
        self.connection = pymysql.connect(
        host='localhost',
        user='root', #user // root
        password="123test456" , # 123test456 // 1234
        db='Proyecto'
    ) 
    #chequeo que la bbdd este en funcionamiento, sino no se conecta
    #y lanza un error (no llega al print)
        self.cursor = self.connection.cursor()
        print("La conexion fue exitosa")
    
    #METODOS
    def get_user_bymail (self, email):
        if (sistema_operativo=='win32') or (sistema_operativo=='win64'):
            query = f"SELECT * FROM usuarios WHERE Email = ('{email}')"
        elif (sistema_operativo=='linux2') or (sistema_operativo=='linux3') or (sistema_operativo=='linux') or (sistema_operativo=='darwin'):
            query = f"SELECT * FROM Usuarios WHERE Email = ('{email}')"
        #query = f"SELECT * FROM Usuarios WHERE Email = ('{email}')"
        self.cursor.execute(query)
        user = self.cursor.fetchall()
        return user

    def get_user_byid (self, id_user):
        if (sistema_operativo=='win32') or (sistema_operativo=='win64'):
            query = f"SELECT * FROM usuarios WHERE id_Usuario = {id_user}"
        elif (sistema_operativo=='linux2') or (sistema_operativo=='linux3') or (sistema_operativo=='linux') or (sistema_operativo=='darwin'):
            query = f"SELECT * FROM Usuarios WHERE id_Usuario = {id_user}"
        #query = f"SELECT * FROM Usuarios WHERE id_Usuario = {id_user}"
        self.cursor.execute(query)
        user = self.cursor.fetchall()
        return user

    """  INSERT INTO Parques (Capacidad_fastpass, Capacidad_normal, Nombre, Ubicacion) VALUES (5, 10, 'Magic Kingdom', 'Florida');    
    INSERT INTO Parques (Capacidad_fastpass, Capacidad_normal, Nombre, Ubicacion) VALUES (5, 10, 'Animal Kingdom', 'Florida');
    INSERT INTO Parques (Capacidad_fastpass, Capacidad_normal, Nombre, Ubicacion) VALUES (5, 10, 'Hollywood Studios', 'Florida');
    INSERT INTO Parques (Capacidad_fastpass, Capacidad_normal, Nombre, Ubicacion) VALUES (5, 10, 'EPCOT', 'Florida'); """
    def add_user (self, apellido, email, nombre, password):
        if (sistema_operativo=='win32') or (sistema_operativo=='win64'):
            query= f"INSERT INTO usuarios (Apellido, Email, Nombre, Password, Usuario) VALUES ('{apellido}', '{email}', '{nombre}', '{password}', 1);"
        elif (sistema_operativo=='linux2') or (sistema_operativo=='linux3') or (sistema_operativo=='linux') or (sistema_operativo=='darwin'):
            query= f"INSERT INTO Usuarios (Apellido, Email, Nombre, Password, Usuario) VALUES ('{apellido}', '{email}', '{nombre}', '{password}', 1);"
        #query= f"INSERT INTO Usuarios (Apellido, Email, Nombre, Password, Usuario) VALUES ('{apellido}', '{email}', '{nombre}', '{password}', 1);" 
        try: 
            self.cursor.execute(query) 
            self.connection.commit()
        except Exception as e: 
            print("INSERT ERROR") 
            raise 

        return

    #hacemos el checkeo en views
    def modify_user (self, new_apellido, new_nombre, new_password, email):
        if (sistema_operativo=='win32') or (sistema_operativo=='win64'):
            query= f"UPDATE usuarios SET Apellido = '{new_apellido}', Nombre = '{new_nombre}', Password = '{new_password}' WHERE Email = '{email}';"
        elif (sistema_operativo=='linux2') or (sistema_operativo=='linux3') or (sistema_operativo=='linux') or (sistema_operativo=='darwin'):
            query= f"UPDATE Usuarios SET Apellido = '{new_apellido}', Nombre = '{new_nombre}', Password = '{new_password}' WHERE Email = '{email}';"
        #query= f"UPDATE Usuarios SET Apellido = '{new_apellido}', Nombre = '{new_nombre}', Password = '{new_password}' WHERE Email = '{email}';"
        try: 
            self.cursor.execute(query) 
            self.connection.commit()
        except Exception as e: 
            print("UPDATE ERROR") 
            raise 

        return


    #date = yyyy-mm-dd
    def get_normal_tickets (self, date, parque):
        if (sistema_operativo=='win32') or (sistema_operativo=='win64'):
            query= f"""SELECT COUNT(*) FROM entradas WHERE Fecha = '{date}' 
                AND FK_Parque = (SELECT id_Parque FROM parques WHERE Nombre = '{parque}')
                AND FK_Tipo_Entrada = (SELECT id_Tipo_Entrada FROM tipo_entrada WHERE Tipo = 'normal');"""

        elif (sistema_operativo=='linux2') or (sistema_operativo=='linux3') or (sistema_operativo=='linux') or (sistema_operativo=='darwin'):
            query= f"""SELECT COUNT(*) FROM Entradas WHERE Fecha = '{date}' 
                AND FK_Parque = (SELECT id_Parque FROM Parques WHERE Nombre = '{parque}')
                AND FK_Tipo_Entrada = (SELECT id_Tipo_Entrada FROM Tipo_Entrada WHERE Tipo = 'normal');"""

        # query= f"""SELECT COUNT(*) FROM Entradas WHERE Fecha = '{date}' 
        #         AND FK_Parque = (SELECT id_Parque FROM Parques WHERE Nombre = '{parque}')
        #         AND FK_Tipo_Entrada = (SELECT id_Tipo_Entrada FROM Tipo_Entrada WHERE Tipo = 'normal');"""
        try: 
            self.cursor.execute(query) 
            count_normal = self.cursor.fetchall()
            return count_normal
        except Exception as e: 
            print("ERROR") 
            raise 


    def get_fast_tickets (self, date, parque):
        if (sistema_operativo=='win32') or (sistema_operativo=='win64'):
            query= f"""SELECT COUNT(*) FROM entradas WHERE Fecha = '{date}' 
                AND FK_Parque = (SELECT id_Parque FROM parques WHERE Nombre = '{parque}')
                AND FK_Tipo_Entrada = (SELECT id_Tipo_Entrada FROM tipo_entrada WHERE Tipo = 'fast');"""

        elif (sistema_operativo=='linux2') or (sistema_operativo=='linux3') or (sistema_operativo=='linux') or (sistema_operativo=='darwin'):
            query= f"""SELECT COUNT(*) FROM Entradas WHERE Fecha = '{date}' 
                AND FK_Parque = (SELECT id_Parque FROM Parques WHERE Nombre = '{parque}')
                AND FK_Tipo_Entrada = (SELECT id_Tipo_Entrada FROM Tipo_Entrada WHERE Tipo = 'fast');"""

        # query= f"""SELECT COUNT(*) FROM Entradas WHERE Fecha = '{date}' 
        #         AND FK_Parque = (SELECT id_Parque FROM Parques WHERE Nombre = '{parque}')
        #         AND FK_Tipo_Entrada = (SELECT id_Tipo_Entrada FROM Tipo_Entrada WHERE Tipo = 'fast');"""
        try: 
            self.cursor.execute(query) 
            count_fast = self.cursor.fetchall()
            return count_fast
        except Exception as e: 
            print("ERROR") 
            raise 

    def get_capacity (self, parque):
        if (sistema_operativo=='win32') or (sistema_operativo=='win64'):
            query= f"SELECT Capacidad_normal, Capacidad_fastpass FROM parques WHERE Nombre = '{parque}';"
        elif (sistema_operativo=='linux2') or (sistema_operativo=='linux3') or (sistema_operativo=='linux') or (sistema_operativo=='darwin'):
            query= f"SELECT Capacidad_normal, Capacidad_fastpass FROM Parques WHERE Nombre = '{parque}';"
        #query= f"SELECT Capacidad_normal, Capacidad_fastpass FROM Parques WHERE Nombre = '{parque}';"
        try: 
            self.cursor.execute(query) 
            capacity = self.cursor.fetchall()
            return capacity
        except Exception as e: 
            print("ERROR") 
            raise 
    
    def insert_ticket (self, tipo_entrada, fk_user, fk_factura, parque, fecha): 

        #Es para transformar el nombre del parque en la fk de la base de datos
        if parque == "Magic":
            fk_parque=1
        elif parque == "Animal":
            fk_parque=2
        elif parque == "Hollywood":
            fk_parque=3
        elif parque == "EPCOT":
            fk_parque=4
        #Es para transformar el tipo de entrada en la fk de la base de datos
        if tipo_entrada == 1:
            fk_tipo_entrada = 1
            if (sistema_operativo=='win32') or (sistema_operativo=='win64'):
                query = f"INSERT INTO entradas (FK_Tipo_Entrada, FK_Parque, FK_Factura, FK_Usuario, Fecha, Precio) VALUES ({fk_tipo_entrada}, {fk_parque}, {fk_factura}, {fk_user},'{fecha}',500);" 
            elif (sistema_operativo=='linux2') or (sistema_operativo=='linux3') or (sistema_operativo=='linux') or (sistema_operativo=='darwin'):
                query = f"INSERT INTO Entradas (FK_Tipo_Entrada, FK_Parque, FK_Factura, FK_Usuario, Fecha, Precio) VALUES ({fk_tipo_entrada}, {fk_parque}, {fk_factura}, {fk_user},'{fecha}',500);" 
        else:
            fk_tipo_entrada = 2
            if (sistema_operativo=='win32') or (sistema_operativo=='win64'):
                query = f"INSERT INTO entradas (FK_Tipo_Entrada, FK_Parque, FK_Factura, FK_Usuario, Fecha, Precio) VALUES ({fk_tipo_entrada}, {fk_parque}, {fk_factura}, {fk_user},'{fecha}',1000);"  
            elif (sistema_operativo=='linux2') or (sistema_operativo=='linux3') or (sistema_operativo=='linux') or (sistema_operativo=='darwin'):
                query = f"INSERT INTO Entradas (FK_Tipo_Entrada, FK_Parque, FK_Factura, FK_Usuario, Fecha, Precio) VALUES ({fk_tipo_entrada}, {fk_parque}, {fk_factura}, {fk_user},'{fecha}',1000);"  


        try: 
            self.cursor.execute(query) 
            self.connection.commit()
        except Exception as e: 
            print("INSERT ERROR") 
            raise 
        return
    
    
    def add_factura (self, fk_user, dtime, total):
        if (sistema_operativo=='win32') or (sistema_operativo=='win64'):
            query = f"INSERT INTO factura (FK_Usuario, Facturacol, Total) VALUES ({fk_user},'{dtime}',{total});"
        elif (sistema_operativo=='linux2') or (sistema_operativo=='linux3') or (sistema_operativo=='linux') or (sistema_operativo=='darwin'):
            query = f"INSERT INTO Factura (FK_Usuario, Facturacol, Total) VALUES ({fk_user},'{dtime}',{total});"
        #query = f"INSERT INTO Factura (FK_Usuario, Facturacol, Total) VALUES ({fk_user},'{dtime}',{total});"
        try: 
            self.cursor.execute(query) 
            self.connection.commit()
        except Exception as e: 
            print("INSERT ERROR") 
            raise 
        return

    def get_factura (self, id_user, dtime):
        if (sistema_operativo=='win32') or (sistema_operativo=='win64'):
            query= f"""SELECT * FROM factura WHERE FK_Usuario = {id_user}
                AND Facturacol = '{dtime}'"""
        elif (sistema_operativo=='linux2') or (sistema_operativo=='linux3') or (sistema_operativo=='linux') or (sistema_operativo=='darwin'):
            query= f"""SELECT * FROM Factura WHERE FK_Usuario = {id_user}
                AND Facturacol = '{dtime}'"""
        # query= f"""SELECT * FROM Factura WHERE FK_Usuario = {id_user}
        #         AND Facturacol = '{dtime}'"""
        try: 
            self.cursor.execute(query) 
            factura = self.cursor.fetchall()
            return factura
        except Exception as e: 
            print("ERROR") 
            raise 

    def get_all_facturas (self, id_user):
        if (sistema_operativo=='win32') or (sistema_operativo=='win64'):
            query= f"SELECT * FROM factura WHERE FK_Usuario = {id_user}"
        elif (sistema_operativo=='linux2') or (sistema_operativo=='linux3') or (sistema_operativo=='linux') or (sistema_operativo=='darwin'):
            query= f"SELECT * FROM Factura WHERE FK_Usuario = {id_user}"
        try: 
            self.cursor.execute(query) 
            facturas = self.cursor.fetchall()
            return facturas
        except Exception as e: 
            print("ERROR") 
            raise 

    def get_data_fast (self, id_factura):
        if (sistema_operativo=='win32') or (sistema_operativo=='win64'):
            query = f"""
        SELECT COUNT(*) FROM entradas WHERE FK_Factura = {id_factura}
        AND FK_Tipo_Entrada = (SELECT id_Tipo_Entrada FROM tipo_entrada WHERE Tipo = "fast");
        """
        elif (sistema_operativo=='linux2') or (sistema_operativo=='linux3') or (sistema_operativo=='linux') or (sistema_operativo=='darwin'):
            query = f"""
        SELECT COUNT(*) FROM Entradas WHERE FK_Factura = {id_factura}
        AND FK_Tipo_Entrada = (SELECT id_Tipo_Entrada FROM Tipo_Entrada WHERE Tipo = "fast");
        """
        # query = f"""
        # SELECT COUNT(*) FROM Entradas WHERE FK_Factura = {id_factura}
        # AND FK_Tipo_Entrada = (SELECT id_Tipo_Entrada FROM Tipo_Entrada WHERE Tipo = "fast");
        # """
        try: 
            self.cursor.execute(query) 
            data = self.cursor.fetchall()
            return data[0][0]
        except Exception as e: 
            print("ERROR") 
            raise 


    def get_data_normal (self, id_factura):
        if (sistema_operativo=='win32') or (sistema_operativo=='win64'):
            query = f"""
        SELECT COUNT(*) FROM entradas WHERE FK_Factura = {id_factura}
        AND FK_Tipo_Entrada = (SELECT id_Tipo_Entrada FROM tipo_Entrada WHERE Tipo = "normal");
        """
        elif (sistema_operativo=='linux2') or (sistema_operativo=='linux3') or (sistema_operativo=='linux') or (sistema_operativo=='darwin'):
            query = f"""
        SELECT COUNT(*) FROM Entradas WHERE FK_Factura = {id_factura}
        AND FK_Tipo_Entrada = (SELECT id_Tipo_Entrada FROM Tipo_Entrada WHERE Tipo = "normal");
        """
        # query = f"""
        # SELECT COUNT(*) FROM Entradas WHERE FK_Factura = {id_factura}
        # AND FK_Tipo_Entrada = (SELECT id_Tipo_Entrada FROM Tipo_Entrada WHERE Tipo = "normal");
        # """
        try: 
            self.cursor.execute(query) 
            data = self.cursor.fetchall()
            return data[0][0]
        except Exception as e: 
            print("ERROR") 
            raise 

    def get_data_fecha (self, id_factura):
        if (sistema_operativo=='win32') or (sistema_operativo=='win64'):
            query = f"SELECT Fecha FROM entradas WHERE FK_Factura = {id_factura} LIMIT 1;"
        elif (sistema_operativo=='linux2') or (sistema_operativo=='linux3') or (sistema_operativo=='linux') or (sistema_operativo=='darwin'):
            query = f"SELECT Fecha FROM Entradas WHERE FK_Factura = {id_factura} LIMIT 1;"
        # query = f"SELECT Fecha FROM Entradas WHERE FK_Factura = {id_factura} LIMIT 1;"
        try: 
            self.cursor.execute(query) 
            data = self.cursor.fetchall()
            return data[0][0]
        except Exception as e: 
            print("ERROR") 
            raise 

    def get_data_park (self, id_factura):
        if (sistema_operativo=='win32') or (sistema_operativo=='win64'):
            query = f"SELECT Nombre FROM parques WHERE id_Parque = (SELECT FK_Parque FROM entradas WHERE FK_Factura = {id_factura} LIMIT 1);"
        elif (sistema_operativo=='linux2') or (sistema_operativo=='linux3') or (sistema_operativo=='linux') or (sistema_operativo=='darwin'):
            query = f"SELECT Nombre FROM Parques WHERE id_Parque = (SELECT FK_Parque FROM Entradas WHERE FK_Factura = {id_factura} LIMIT 1);"
        # query = f"SELECT Nombre FROM Parques WHERE id_Parque = (SELECT FK_Parque FROM Entradas WHERE FK_Factura = {id_factura} LIMIT 1);"

        try: 
            self.cursor.execute(query) 
            data = self.cursor.fetchall()
            return data[0][0]
        except Exception as e: 
            print("ERROR") 
            raise

    def get_data_fecha_factura (self, id_factura):
        if (sistema_operativo=='win32') or (sistema_operativo=='win64'):
            query = f"SELECT Facturacol FROM factura WHERE id_Factura = {id_factura} LIMIT 1;"
        elif (sistema_operativo=='linux2') or (sistema_operativo=='linux3') or (sistema_operativo=='linux') or (sistema_operativo=='darwin'):
            query = f"SELECT Facturacol FROM Factura WHERE id_Factura = {id_factura} LIMIT 1;"
        # query = f"SELECT Facturacol FROM Factura WHERE id_Factura = {id_factura} LIMIT 1;"
        try: 
            self.cursor.execute(query) 
            data = self.cursor.fetchall()
            return data[0][0]
        except Exception as e: 
            print("ERROR") 
            raise  


