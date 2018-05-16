"""
controller_database define all operations whit mongodb database
insert, search, update and delete fields from database
"""

from bson.json_util import dumps


def search_user(collection, json) -> tuple:
    success = False
    try:
        email = json['email']
        password = json['password']
    except Exception as e:
        print(e)
        message = 'You should type username and password'
    else:
        try:
            user_response = collection.find_one({'email': email})
        except Exception as e:
            print(e)
            message = str(e)
        else:
            if user_response is not None:
                if user_response['password'] == password:
                    success = True
                    message = 'Correct credentials'
                else:
                    message = 'Incorrect password'
            else:
                message = 'Incorrect username'
    return success, message


def insert_user(collection, json) -> tuple:
    success = False
    try:
        username = json['username']
        email = json['email']
        password = json['password']
        status = json['status']
        photo = json['photo']
    except Exception as e:
        print(e)
        message = 'All inputs are required'
    else:
        try:
            collection.insert(
               {
                   'username': username,
                   'email': email,
                   'password': password,
                   'status': status,
                   'photo': photo
               }
            )
        except Exception as e:
            print(e)
            message = str(e)
        else:
            success = True
            message = 'User save successfully'
    return success, message


def get_plates(collection) -> tuple:
    success = False
    try:
        plates_response = collection.find()
    except Exception as e:
        print(e)
        message = str(e)
    else:
        success = True
        plates_response = dumps(plates_response)
        if len(plates_response) > 2:
            message = plates_response
            print(message)
        else:
            message = 'There is no plates yet'
    return success, message


def get_drinks(collection) -> tuple:
    success = False
    try:
        drinks_response = collection.find()
    except Exception as e:
        print(e)
        message = str(e)
    else:
        success = True
        drinks_response = dumps(drinks_response)
        if len(drinks_response) > 2:
            message = drinks_response
            print(message)
        else:
            message = 'There is no drinks yet'
    return success, message


def insert_plate(collection, json):
    success = False
    try:
        name = json['name']
        kind = json['kind']
        price = json['price']
        preparation_time = json['preparation_time']
        photo = json['photo']
    except Exception as e:
        print(e)
        message = 'All inputs are required'
    else:
        try:
            collection.insert(
               {
                   'name': name,
                   'kind': kind,
                   'price': price,
                   'preparation_time': preparation_time,
                   'photo': photo
               }
            )
        except Exception as e:
            print(e)
            message = str(e)
        else:
            success = True
            message = 'Plate save successfully'
    return success, message


def insert_drink(collection, json):
    success = False
    try:
        name = json['name']
        price = json['price']
        photo = json['photo']
    except Exception as e:
        print(e)
        message = 'All inputs are required'
    else:
        try:
            collection.insert(
               {
                   'name': name,
                   'price': price,
                   'photo': photo
               }
            )
        except Exception as e:
            print(e)
            message = str(e)
        else:
            success = True
            message = 'Drink save successfully'
    return success, message
