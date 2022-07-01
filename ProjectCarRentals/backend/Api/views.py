from flask import jsonify
from flask import request, render_template

from Api import app
from .models import user, user_table,userSchema,user_bookingSchema,user_booking, db

todo_item_schema = userSchema()
todo_list_schema = userSchema(many=True)

booking_schema = user_bookingSchema()
booking_schema = user_bookingSchema(many=True)

@app.route("/")
def index():
    return render_template('signup.html')

@app.route("/signup",methods = ['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username)
        print(password)
        item = user_table(username,password)
        db.session.add(item)
        db.session.commit()
        return {'status': 'ok'}
    return 'Hello World'

@app.route("/login",methods = ['POST', 'GET'])
def login():
    try:
        if request.method == 'POST':
            email = request.form['username']
            password = request.form['password']
            user = user_table.query.filter_by(email=email).first()
            if email == 'adminbuzz@gmail.com' and password=='admin285':
                return{'status':'admin'}
            elif email==user.email and password == user.password:
                print(email)
                print(password)
                return {'status': 'ok'}
    except:
        return{'status':'error'}
    return 'Hello World'

 

@app.route("/carsdata", methods=["POST"])
def add_item():
    if 'carname' in request.form and 'cardescription' in request.form:
        carname = request.form['carname']
        cardescription = request.form['cardescription']
        newcar = user(carname, cardescription)
        db.session.add(newcar)
        db.session.commit()
        return todo_item_schema.jsonify(newcar)

@app.route("/carsdata", methods=["GET"])
def get_todo_list():
    result = user.query.all()
    result = todo_list_schema.dump(result)
    print(result)
    return jsonify(result)


@app.route("/carsdata/<id>", methods=["GET"])
def get_todo_item(id):
    if id:
        result = user.query.filter(user.id==id)
        db.session.commit()
        return"good"

@app.route("/carsdata/<id>", methods=["DELETE"])
def delete_todo_item(id):
    user.query.filter(user.id==id).delete()
    db.session.commit()
    return "ok"

@app.route('/carsdata/<id>', methods=['PUT'])
def update(id):
    update = user.query.get(id)
    carname = request.form['carname']
    cardescription = request.form['cardescription']

    update.carname = carname
    update.cardescription = cardescription

    db.session.commit()
    return todo_item_schema.jsonify(update)

@app.route("/carsdata/<id>", methods=["GET"])
def booking(id):
    if id:
        return"ok"



