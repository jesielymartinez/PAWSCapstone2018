from flask import jsonify

from dao.Products import ProductsDAO



class productsHandler:

    def build_products_dict(self, row):
        result = {}
        result['pid'] = row[0]
        result['pname'] = row[1]
        result['description'] = row[2]
        result['pprice'] = row[3]
        result['shipping_cost'] = row[4]
        result['cid'] = row[5]
        result['uid'] = row[6]
        result['pqty'] = row[7]
        return result


    def build_ProductsSeller_dict(self, row):
        result = {}
        result['pid'] = row[0]
        result['pname'] = row[1]
        result['pqty'] = row[2]
        return result

    def build_ProductsCategory_dict(self, row):
        result = {}
        result['cat_name'] = row[0]
        result['pname'] = row[1]
        result['pqty'] = row[2]
        return result

    def build_category_dict(self, row):
        result = {}
        result['cid']= row[0]
        result['cname']= row[1]
        return result

    def build_productpid_dict(self,row):
        result = {}
        result['pid'] = row[0]
        return result

    def build_purchases_dict(self,row):
        result = {}
        result['caid'] = row[0]
        result['uid'] = row[1]
        result['pid'] = row[2]
        result['p_qty'] = row[3]
        return result


    ######################

    def getAllProduct(self):
        dao = ProductsDAO()
        products_list = dao.getAllProducts()
        results_list = []
        for row in products_list:
            result = self.build_products_dict(row)
            results_list.append(result)
        return jsonify(Products=results_list)



    def getCategory(self):
        dao = ProductsDAO()
        category_list = dao.getCategory()
        results_list = []
        for row in category_list:
            result = self.build_category_dict(row)
            results_list.append(result)
        return jsonify(Categories=results_list)

# Get products by seller
    def getAllProductsBySeller(self, uid):
        dao = ProductsDAO()
        products_list = dao.getAllProductsBySeller(uid)
        results_list = []
        for row in products_list:
            result = self.build_ProductsSeller_dict(row)
            results_list.append(result)

        return jsonify(Products_By_User=results_list)

    #get product by pid
    def getProductByPID(self,pid):
        dao = ProductsDAO()
        product = dao.getProductByPID(pid)
        result_list = []
        for row in product:
            result = self.build_products_dict(row)
            result_list.append(result)
        return jsonify(Product_by_PID=result_list)




# Get products in category
    def getAllProductsWithCategory(self):
        dao = ProductsDAO()
        products_list = dao.getAllProductsWithCategory()
        results_list = []
        for row in products_list:
            result = self.build_ProductsCategory_dict(row)
            results_list.append(result)
        return jsonify(Products=results_list)

    def getProductsByCategory(self, cid):
        dao = ProductsDAO()
        products_list = dao.getProductsByCategory(cid)
        results_list = []
        for row in products_list:
            result = self.build_ProductsCategory_dict()
            results_list.append(result)
        return jsonify(Products=results_list)

    def insertProduct(self, form):
        if form and len(form) == 7:
            pname = form['pname']
            description = form['description']
            pprice = form['pprice']
            shipping_cost = form['shipping_cost']
            cid = form['cid']
            uid = form['uid']
            pqty = form['pqty']
            if pname and description and pprice and shipping_cost and cid and uid and pqty:
                dao = ProductsDAO()
                pid = dao.insertProduct(pname, description, pprice, shipping_cost, cid, uid, pqty)
                result = {}
                result['pid'] = pid
                result['pname'] = pname
                result['description'] = description
                result['pprice'] = pprice
                result['shipping_cost'] = shipping_cost
                result['cid'] = cid
                result['uid'] = uid
                result['pqty'] = pqty
                return jsonify(Products=result)
            else:
                return jsonify(Error="unexpected attributes in post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400

#Insert new category

    def insertCategory(self, form):

        if form and len(form) == 1:

            cat_name = form['cat_name']

            if cat_name:
                dao = ProductsDAO()
                cid = dao.insertCategory(cat_name)
                result = {}
                result['cid'] = cid
                result['cat_name'] = cat_name
                return jsonify(Categories=result)
            else:
                return jsonify(Error="unexpected attributes in post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400

    # Make a purchase
    def makePurchase(self, form):
        if form and len(form) == 3:
            uid = form['uid']
            pid = form['pid']
            p_qty = form['p_qty']
            if uid and pid and p_qty:
                dao = ProductsDAO()
                caid = dao.makePurchase(uid, pid, p_qty)
                result = {}
                result['caid'] = caid
                result['uid'] = uid
                result['pid'] = pid
                result['p_qty'] = p_qty
                return jsonify(Cart_Item=result)
            else:
                return jsonify(Error="unexpected attributes in post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400

    def getAllPurchases(self, form):
        dao = ProductsDAO()
        purchase_list = dao.getAllPurchases()
        results_list = []
        for row in purchase_list:
            result = self.build_purchases_dict(row)
            results_list.append(result)
        return jsonify(Purchases=results_list)

