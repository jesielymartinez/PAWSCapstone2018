from flask import jsonify

from dao.users import UsersDAO


class usersHandler:

    # Create a dictionary of users
    def build_users_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['utype'] = row[1]
        result['user_name'] = row[2]
        result['user_lname'] = row[3]
        result['address1'] = row[4]
        result['city'] = row[5]
        result['state'] = row[6]
        result['zipcode'] = row[7]
        result['country'] = row[8]
        result['phone'] = row[9]
        result['user_email'] = row[10]
        result['user_nickname'] = row[11]
        result['user_password'] = row[12]
        return result



    def build_users_dict2(selfself, row):
        result = {}
        result['uid'] = row[0]
        result['utype'] = row[1]
        result['user_name'] = row[2]
        result['user_lname'] = row[3]
        return result



    def build_usersUtype_dict(self, row):
        result = {}
        result['utype'] = row[0]
        return result

    def build_userAddress_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['address1'] = row[1]
        result['city'] = row[2]
        result['state'] = row[3]
        result['zipcode'] = row[4]
        result['country'] = row[5]
        return result

    def build_userPhone_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['phone'] = row[1]
        return result

    def build_userEmail_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['user_email'] = row[1]
        return result

    def build_userNickname_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['user_nickname'] = row[1]
        return result

    def build_userPassword_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['user_password'] = row[1]
        return result

    def build_sellerswithproducts_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['user_name'] = row[1]
        result['user_lname'] = row[2]
        return result

    ####################################

    def getSellerWithProducts(self):
        dao = UsersDAO()
        users_list = dao.getSellersWithPostedProducts()
        results_list = []
        for row in users_list:
            result = self.build_sellerswithproducts_dict(row)
            results_list.append(result)
        return jsonify(Sellers=results_list)

    #################### POST METHODS #############################################
    def insertUser(self,form):

        if form and len(form) == 12:

            utype = form['utype']
            user_name = form['user_name']
            user_lname = form['user_lname']
            address1 = form['address1']
            city = form['city']
            state = form['state']
            zipcode = form['zipcode']
            country = form['country']
            phone = form['phone']
            user_email = form['user_email']
            user_nickname = form['user_nickname']
            user_password = form['user_password']


            if utype and user_name and user_lname and address1 and city and state and zipcode and country and phone and user_email and user_nickname and user_password:
                dao = UsersDAO()
                uid = dao.insertUser(utype, user_name, user_lname, address1, city, state, zipcode, country, phone, user_email, user_nickname, user_password)
                result = {}
                result['uid'] = uid
                result['utype'] = utype
                result['user_name'] = user_name
                result['user_lname'] = user_lname
                result['address1'] = address1
                result['city'] = city
                result['state'] = state
                result['zipcode'] = zipcode
                result['country'] = country
                result['phone'] = phone
                result['user_email'] = user_email
                result['user_nickname'] = user_nickname
                result['user_password'] = user_password
                return jsonify(New_User=result), 201

            else:
                return jsonify(Error="Malformed post request"), 400
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

######## Hacer una compra









    ## Update user
    def updateUsers(self, uid, form):
        dao = UsersDAO()
        if not dao.getUserById(uid):
            return jsonify(Error="User not found."), 404

        else:
            if len(form) != 2 or len(form) != 6:
                return jsonify(Error="Malformed update request"), 400
            else:
                if len(form) == 2:
                    uid = form['uid']
                    phone = form['phone']
                    user_email = form['user_email']
                    user_nickname = form['user_nickname']
                    user_password = form['user_password']

                    if uid and phone:
                        dao.updateUserPhoneNum(uid, phone)
                        result = self.build_userPhone_dict(uid, phone)
                        return jsonify(Users=result)
                    elif uid and user_email:
                        dao.updateUserEmail(uid, user_email)
                        result = self.build_userEmail_dict(uid, user_email)
                        return jsonify(Users=result)
                    elif uid and user_nickname:
                        dao.updateUserNickname(uid, user_nickname)
                        result = self.build_userNickname_dict(uid, user_nickname)
                        return jsonify(Users=result)
                    elif uid and user_password:
                        dao.updateUserPassword(uid, user_password)
                        result = self.build_userPassword_dict(uid, user_password)
                        return jsonify(Users=result)
                    else:
                        return jsonify(Error="Unexpected attrinutes in update request")

                elif len(form) == 6:
                    uid = form["uid"]
                    address1 = form['address1']
                    city = form['city']
                    state = form['state']
                    zipcode = form['zipcode']
                    country = form['country']
                    if uid and address1 and city and state and zipcode and country:
                        dao.updateAddress(uid, address1, city, state, zipcode, country)
                        result = self.build_userAddress_dict(uid, address1, city, state, zipcode, country)
                        return jsonify(Users=result)
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

        ################################
        ############### Delete User

    def deleteUser(self, uid):
        dao = UsersDAO()
        if not dao.getUserById(uid):
            return jsonify(Error="User not found."), 404
        else:
            dao.deleteUser(uid)
        return jsonify(DeleteStatus="OK"), 200

    #################### GET METHODS #############################################
    def getAllUsers(self):
        dao = UsersDAO()
        users_list = dao.getAllUsers()
        results_list = []
        for row in users_list:
            result = self.build_users_dict(row)
            results_list.append(result)
        return jsonify(Users=results_list)

    ## Get User by ID
    def getUserById(self, uid):
        dao = UsersDAO()
        row = dao.getUserById(uid)
        if not row:
            return jsonify(Error="User not found."), 404
        else:
            user = self.build_users_dict(row)
            return jsonify(User=user)

    ## Get user by user type

    def getUserByUtype(self, utype):
        dao = UsersDAO()
        users = dao.getUsersByUtype(utype)
        if not users:
            return jsonify(Error="User not found"), 404
        else:
            result_list = []
            for row in users:
                result = self.build_users_dict(row)
                result_list.append(result)
        return jsonify(User_Type=result_list)
