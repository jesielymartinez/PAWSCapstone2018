from config.db_config import db_config
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2


class UsersDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (db_config['dbname'],
                                                            db_config['user'],
                                                            db_config['psswd'])
        self.conn = psycopg2._connect(connection_url)

    ## Get the list of the users
    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    ## Get the seller list
    def getAllSellers(self):
        cursor = self.conn.cursor()
        query = "select * from users where utype = 'seller';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    ## Get user by id
    def getUserById(self, uid):
        cursor = self.conn.cursor()
        query = "select * from users where uid = %s;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result

    ## Get the regular users list
    def getUsersByUtype(self, utype):
        cursor = self.conn.cursor()
        query = "select * from users where utype = %s;"
        cursor.execute(query, (utype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    ##Get all the sellers that posted products to sell

    def getSellersWithPostedProducts(self):
        cursor = self.conn.cursor()
        query = "select distinct uid, user_name, user_lname from Users natural inner join Products where utype = 'seller';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    ## Get the seller that posted a product

    ###############################################################################

    ## Delete a user by uid

    def deleteUser(self, uid):
        cursor = self.conn.cursor()
        query = "delete from users where uid = %s;"
        cursor.execute(query, (uid,))
        return uid

    ########################################################################################

    ## Get Max uid



    ## Insert a new user
    #### HASHING THE PASSWORD #############


    def insertUser(self, utype, user_name, user_lname, address1, city, state, zipcode, country, phone, user_email, user_nickname, user_password):
        cursor = self.conn.cursor()
        query = "insert into users(utype, user_name, user_lname, address1, city, state, zipcode, country, phone, user_email, user_nickname, user_password) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) returning uid;"
        cursor.execute(query, (utype, user_name, user_lname, address1, city, state, zipcode, country, phone, user_email, user_nickname, user_password,))
        uid = cursor.fetchone()[0]
        self.conn.commit()
        return uid




    ###############################################################################################

    ##                  Updates users

    #########################################################################################

    ## Update user change utype

    def updateUserType(self, uid, utype):
        cursor = self.conn.cursor()
        query = "update users set utype = %s where uid = %s ;"
        cursor.execute(query, (uid, utype,))
        self.conn.commit()
        return uid

    ##Update user address
    def updateUserAddress(self, uid, address1, city, state, zipcode, country):
        cursor = self.conn.cursor()
        query = "update users set utype = %s where uid = %s ;"
        cursor.execute(query, (uid, address1, city, state, zipcode, country,))
        self.conn.commit()
        return uid

    ## Update user phone number

    def updateUserPhoneNum(self, uid, phone):
        cursor = self.conn.cursor()
        query = "update users set phone = %s where uid = %s ;"
        cursor.execute(query, (uid, phone,))
        self.conn.commit()
        return uid

    # Update user email

    def updateUserEmail(self, uid, user_email):
        cursor = self.conn.cursor()
        query = "update users set user_email = %s where uid = %s ;"
        cursor.execute(query, (uid, user_email,))
        self.conn.commit()
        return uid

    # Update user nickname

    def updateUserNickname(self, uid, user_nickname):
        cursor = self.conn.cursor()
        query = "update users set user_nickname = %s where uid = %s ;"
        cursor.execute(query, (uid, user_nickname,))
        self.conn.commit()
        return uid

    # Update user password

    def updateUserPassword(self, uid, user_password):
        cursor = self.conn.cursor()
        query = "update users set user_password = %s where uid = %s ;"
        cursor.execute(query, (uid, set_password(user_password),))
        self.conn.commit()
        return uid
