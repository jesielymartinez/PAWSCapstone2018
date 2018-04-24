from config.db_config import db_config
# werkzeug.security import generate_password_hash, check_password_hash
import psycopg2

class ProductsDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (db_config['dbname'],
                                                            db_config['user'],
                                                            db_config['psswd'])
        self.conn = psycopg2._connect(connection_url)

    ## Get the list of products

    def getAllProducts(self):
        cursor = self.conn.cursor()
        query = "select * from Products;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getProductPID(self):
        cursor = self.conn.cursor()
        query = "select pid from Products;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result



    ## Get the products by seller
    def getAllProductsBySeller(self, uid):
        cursor = self.conn.cursor()
        query = "select distinct pid, pname, pqty from Products natural inner join Users where uid= %s;"
        cursor.execute(query,(uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Get product by pid

    def getProductByPID(self, pid):
        cursor = self.conn.cursor()
        query = "select * from Products where pid = %s;"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result




    ## Get the detaisl of a single product

    # Get all products with category
    def getAllProductsWithCategory(self):
        cursor = self.conn.cursor()
        query = "select distinct cat_name, pname, pqty from Category natural inner join Products group by cat_name, pname, pqty order by cat_name;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getProductsByCategory(self,cid):
        cursor = self.conn.cursor()
        query = "select pname, pqty from Category natural inner join Products where cid = %s group by pname, pqty order by pname;"
        cursor.execute(query,(cid,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getCategory(self):
        cursor = self.conn.cursor()
        query = "select * from Category;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result





    def getProductDetails(self, pid):
        cursor = self.conn.cursor()
        query = "Select * from Products where pid = %s;"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    ######################
    # Buy a product
    ## Verifica como puedes modificar

    def buyProduct(self,uid,pid,p_qty):
        cursor=self.conn.cursor()
        query= "insert into cart (uid,pid,p_qty) values (%s,%s,%s);"
        cursor.execute(query,(uid, pid, p_qty,))
        result=[]
        for row in cursor:
            result.append(row)
        return result

    ################### Insert a product

    def insertProduct(self, pname, description, pprice, shipping_cost, cid, uid, pqty ):
        cursor = self.conn.cursor()
        query= "insert into Products(pname, description, pprice, shipping_cost, cid, uid, pqty) values (%s,%s, %s, %s, %s, %s, %s) returning pid;"
        cursor.execute(query, (pname, description, pprice, shipping_cost,cid, uid, pqty,))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid

    ######################## Insert Category


    def insertCategory(self, cat_name):
        cursor = self.conn.cursor()
        query= "insert into Category(cat_name) values (%s) returning cid;"
        cursor.execute(query, (cat_name,))
        cid = cursor.fetchone()[0]
        self.conn.commit()
        return cid

    ################ Make a purchase
    # insert into cart (uid,pid,p_qty) values (3,1,3);

    def makePurchase(self, uid, pid, p_qty):
        cursor = self.conn.cursor()
        query = "insert into cart( uid, pid, p_qty) values (%s, %s, %s) returning caid;"
        cursor.execute(query, (uid, pid, p_qty,))
        caid = cursor.fetchone()[0]
        self.conn.commit()
        return caid

    def getAllPurchases(self):
        cursor = self.conn.cursor()
        query = "select * from Cart;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result












