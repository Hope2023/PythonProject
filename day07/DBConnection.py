from pymysql import Connection


conn = Connection(
    host= 'rm-uf656jp81w6eb013k4o.mysql.rds.aliyuncs.com',
    port= 3306,  # 端口号,默认3306
    user= 'wiki',  # 例如: root
    password= 'Siemens#2024',
    database= 'wiki',
    charset= 'utf8mb4'
)

print(conn.get_server_info())



