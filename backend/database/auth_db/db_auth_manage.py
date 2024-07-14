import pymysql

from backend.database.db_connect_data import RailwayAccessDB, AccessDB


class SuchefAuthDB:
    def __init__(self):
        self.access_db = AccessDB()
        # self.access_db = RailwayAccessDB()
        self.connection = None
        self.users_auth_data = []

    def db_connect(self):
        try:
            self.connection = pymysql.connect(
                host=self.access_db.host,
                port=self.access_db.port,
                user=self.access_db.user,
                password=self.access_db.password,
                database=self.access_db.database,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("[SuchefAuthDB : db_connect] :\n"
                  "connection successfully..")
        except Exception as _ex:
            print(f"[SuchefAuthDB : db_connect] :\n"
                  f"{_ex}")

    def create_user_auth_table(self):
        self.db_connect()
        with self.connection.cursor() as cursor:
            create_table_query = "CREATE TABLE `user_auth`(id int AUTO_INCREMENT," \
                                 " user_id int," \
                                 " username varchar(32)," \
                                 " phone_number varchar(32), PRIMARY KEY (id));"

            cursor.execute(create_table_query)
            print("[SuchefAuthDB : create_user_auth_table] :\n"
                  "Table created successfully")

    def db_insert_user_auth_data(self, telegram_id, telegram_user, user_phone_number):
        self.db_connect()
        try:
            with self.connection.cursor() as cursor:
                query = "INSERT INTO `user_auth` (user_id, username, phone_number) VALUES (%s, %s, %s);"
                cursor.execute(query, (telegram_id, telegram_user, user_phone_number))
        except Exception as _ex:
            print(f"[SuchefAuthDB: db_insert_user_auth_data] :\n"
                  f"{_ex}")
        finally:
            self.connection.commit()
            self.connection.close()

    def db_get_user_auth_data(self):
        self.db_connect()
        try:
            with self.connection.cursor() as cursor:
                query = "SELECT * FROM `user_auth`"
                cursor.execute(query)
                data = cursor.fetchall()

                for user in data:
                    self.users_auth_data.append(list(user.values()))
        except Exception as _ex:
            print(f"[SuchefAuthDB : db_get_user_auth_data] :\n"
                  f"{_ex}")
        finally:
            cursor.close()
            self.connection.close()

    def clear_db(self):
        self.db_connect()
        try:
            with self.connection.cursor() as cursor:
                query = "TRUNCATE TABLE `user_auth`"
                cursor.execute(query)
        except Exception as _ex:
            print(_ex)
        finally:
            self.connection.commit()
            self.connection.close()

    def db_check_user_id_exists(self, telegram_id):
        try:
            self.db_get_user_auth_data()
            data = self.users_auth_data

            for i in range(len(data)):
                if telegram_id == data[i][1]:
                    return True
            return False
        except Exception as _ex:
            print(_ex)

    def db_phone_number_from_id(self, telegram_id):
        self.db_connect()
        try:
            with self.connection.cursor() as cursor:
                query = f"SELECT phone_number FROM `user_auth` WHERE user_id = {telegram_id}"
                cursor.execute(query)
                result = cursor.fetchall()
                phone_number = list(result[0].values())[0]
            return phone_number
        except Exception as _ex:
            print(_ex)

    def db_replace_phone_number_from_id(self, telegram_id, user_phone_number):
        self.db_connect()
        try:
            with self.connection.cursor() as cursor:
                query = "UPDATE `user_auth` SET phone_number = %s WHERE user_id = %s"
                value = (user_phone_number, telegram_id)
                cursor.execute(query, value)
        except Exception as _ex:
            print(_ex)
        finally:
            self.connection.commit()
            cursor.close()
            self.connection.close()