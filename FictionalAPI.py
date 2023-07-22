from flask import Flask, jsonify, request

# creating an API for hypotatical cases/situations of industrial accidents during the first 6 months of 2023 (fictional datas):

app = Flask(__name__)

accidents = [
    {
        'id': 1,
        'title': 'Car accidents',
        'amount': '10'
    },
    {
        'id': 2,
        'title': 'Falls from heights',
        'amount': '5'
    },
    {
        'id': 3,
        'title': 'Struck by an object',
        'amount': '19'
    },
    {
        'id': 4,
        'title': 'Struck against an object',
        'amount': '10'
    },
]

# query(All)
@app.route('/accidents',methods=['GET'])
def get_accidents():
    return jsonify(accidents)

# query(Id)
@app.route('/accidents/<int:id>',methods=['GET'])
def get_accidents_by_id(id):
    for accident in accidents:
        if accident.get('id') == id:
            return jsonify(accident)
# edit
@app.route('/accidents/<int:id>',methods=['PUT'])
def edit_accidents_by_id(id):
    edited_accident = request.get_json()
    for indexnumberIn,accident in enumerate(accidents):
        if accident.get('id') == id:
            accidents[indexnumberIn].update(edited_accident)
            return jsonify(accidents[indexnumberIn])
# create
@app.route('/accidents',methods=['POST'])
def create_new_item():
    new_item = request.get_json()
    accidents.append(new_item)
    
    return jsonify(accidents)
# delete
@app.route('/accidents/<int:id>',methods=['DELETE'])
def delete_item(id):
    for indexnumberIn, accident in enumerate(accidents):
        if accident.get('id') == id:
            del accidents[indexnumberIn]

    return jsonify(accidents)

app.run(port=5000,host='localhost',debug=True)
