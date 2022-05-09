from config import app,db
from flask import jsonify,request,abort
from models import DbPerson

@app.route("/employees")
def getDbPeople():
    listp=DbPerson.query.all()
    result = [x.serialize() for x in listp]
    return jsonify(result)


@app.route("/employees",methods=['POST'])
def processDepartments():
    try:
        input=request.get_json()
        eno=input['eno']
        name=input['name']
        city=input['city']
        designation=input['designation']
        age=input['age']
        db.session.add(DbPerson(eno,name,city,designation,age))
        db.session.commit()
        return {"status": "success"}, 201
    except:
        abort({'status':"Internal server error"},500)

