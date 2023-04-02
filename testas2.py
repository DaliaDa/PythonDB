from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="root",
        password="qwery",
    ) as connection:
        create_db_query = "Create database online_movie_rating"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
except Error as e:
    print(e)
