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
    INSERT INTO Parques (Capacidad_fastpass, Capacidad_normal, Nombre, Ubicacion) VALUES (5, 10, 'Holliwood Studios', 'Florida');
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
    

