from flask import Flask, jsonify, request

from handler.users import usersHandler;
from handler.Products import productsHandler;

import User_autentication

app = Flask(__name__)


# Initial page to display
@app.route('/')
def greeting():
    return 'Hola, bienvenido a Huella Sin Fronteras!'


# Get all registered users
@app.route('/Marketplace/users', methods=['GET', 'POST'])
def getAllUsers():
    if request.method == 'POST':

        return usersHandler().insertUser(request.form)

    elif request.method == 'PUT':
        return usersHandler().updateUsers(request.args, request.form)

    else:
        if not request.args:
            return usersHandler().getAllUsers()

@app.route('/Marketplace/users/delete', methods=['DELETE'])
def deleteUser(form):
    if form and len(form) == 1:
        uid = form['uid']
        if uid:
            return usersHandler().deleteUser(uid)




# Get Categories

@app.route('/Marketplace/categories', methods=['GET', 'POST'])
def getCategory():
    if request.method == 'POST':

        return productsHandler().insertCategory(request.form)
    else:
        if not request.args:
            return productsHandler().getCategory()


@app.route('/Marketplace/products', methods=['GET', 'POST'])
def getProductsCategories():
    if request.method == 'POST':
        return productsHandler().insertProduct(request.form)
    else:
        if not request.args:
            return productsHandler().getAllProductsWithCategory()


# GEt Sellers with Posted Products
@app.route('/Marketplace/sellersproducts', methods=['GET'])
def getSellersWithProducts():
    return usersHandler().getSellerWithProducts()



# Get user by uid
@app.route('/Marketplace/users/<int:uid>', methods=['GET'])
def getUsersByUid(uid):
    return usersHandler().getUserById(uid)


# Get user by utype

@app.route('/Marketplace/users/type/<utype>', methods=['GET'])
def getUsersByUtype(utype):
    return usersHandler().getUserByUtype(utype)

# Get products from seller by uid
@app.route('/Marketplace/products/<int:uid>', methods=['GET'])
def getProductsBySeller(uid):
    return productsHandler().getAllProductsBySeller(uid)

# Get all products
@app.route('/Marketplace/productslist', methods=['GET'])
def getAllProducts():
    return productsHandler().getAllProduct()

# Get product by pid

@app.route('/Marketplace/product/<int:pid>', methods=['GET'])
def getProductByPID(pid):
    return productsHandler().getProductByPID(pid)


#################################################3

### Make a purchase

@app.route('/Marketplace/purchase', methods=['POST'])
def makePurchase():
    if request.method == 'POST':
        return productsHandler().makePurchase(request.form)

# Get all items in the cart

@app.route('/Marketplace/purchase/allCarts', methods=['GET'])
def getAllCarts():
    return productsHandler().getAllPurchases(request.form)









########## USER Register and Login #########################

# Registration of users

@app.route('/register', methods=['POST'])
def userRegister():
    if request.method == 'POST':
        return usersHandler().insertUser(request.form)


# User Login

@app.route('/login', methods=['GET'])
def getUserLoginByUid(uid):
    return usersHandler().getUserLoginByUid(uid)


class UserNotFoundError(Exception):
    def __init__(self, message):
        assert isinstance(message, object)
        self.message = message


if __name__ == "__main__":
    app.run()
