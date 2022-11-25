import pymysql
#definimos un objetos Base de datos
class Database():
    #creamos el constructor con la bbdd elegida a traves de pymysql
    def __init__(self):
        self.connection = pymysql.connect(
        host='localhost',
        user='user',
        password='123test456',
        db='sakila'
    ) 
    #chequeo que la bbdd este en funcionamiento, sino no se conecta
    #y lanza un error (no llega al print)
        self.cursor = self.connection.cursor()
        print("La conexion fue exitosa")
    
    #METODOS
    def all_users (self):
        sql='SELECT COUNT(*) as cant_paises_con_a FROM country WHERE country LIKE "A%";'
        self.cursor.execute(sql)
        users=self.cursor.fetchall()
        return users
    

