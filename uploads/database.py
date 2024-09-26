# import pyodbc
# print("hi")
# def get_db_connection():
#     conn = pyodbc.connect(
#         'DRIVER={ODBC Driver 17 for SQL Server};'
#         'SERVER=localhost;'
#         'DATABASE=Fruit_Detection;'
#         'Trusted_Connection=yes;'
#     )
#     print("Connected to SQL Server database")
#     return conn
#
#
#
# def fetch_nutrition_info(fruit_name):
#     conn = get_db_connection()
#     cursor = conn.cursor()
#
#     query = """
#     SELECT
#         Proteins_level,
#         Carbo_level,
#         Fats_level,
#         Fiber_level,
#         Vit_level,
#         Nutrition_description
#     FROM Nutrition_Info
#     WHERE Fruit_name = ?
#     """
#
#     cursor.execute(query, (fruit_name,))
#     row = cursor.fetchone()
#
#     if row:
#         # Convert pyodbc.Row to a dictionary
#         nutrition_info = {
#             "Proteins_level": row.Proteins_level,
#             "Carbo_level": row.Carbo_level,
#             "Fats_level": row.Fats_level,
#             "Fiber_level": row.Fiber_level,
#             "Vit_level": row.Vit_level,
#             "Nutrition_description": row.Nutrition_description
#         }
#         print(nutrition_info)  # Now you can print the dictionary
#         return nutrition_info
#     else:
#         print(f"No nutrition information found for {fruit_name}")
#         return None
# get_db_connection()

import pyodbc


def get_db_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=192.168.1.8,1433;"
        "DATABASE=Fruit_Detection;"
        "UID=MS;"
        "PWD=MS;"
    )
    return conn


def fetch_nutrition_info(fruit_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM Nutrition_info WHERE Fruit_name = ?"
    cursor.execute(query, (fruit_name,))
    result = cursor.fetchone()

    # Convert result to dictionary if not None
    if result:
        return {
            'Fruit_name': result[0],
            'Proteins_level': result[1],
            'Carbo_level': result[2],
            'Fats_level': result[3],
            'Fiber_level': result[4],
            'Vit_level': result[5],
            'Nutrition description': result[6]
        }
    return {}


def store_visitor_ip(visitor_ip):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Check if the IP address is already in the database
    query_check = "SELECT COUNT(*) FROM visitors WHERE ip_address = ?"
    cursor.execute(query_check, (visitor_ip,))
    exists = cursor.fetchone()[0]

    if exists == 0:
        # Insert new IP address if it doesn't already exist
        query_insert = "INSERT INTO visitors (ip_address) VALUES (?)"
        cursor.execute(query_insert, (visitor_ip,))
        conn.commit()

    cursor.close()
    conn.close()


# Get the total number of unique visitors
def get_unique_visitor_count():
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT COUNT(*) FROM visitors"
    cursor.execute(query)
    visitor_count = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return visitor_count
