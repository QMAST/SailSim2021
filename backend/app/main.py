from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/sailLogicCommand', methods=['POST'])
def add_command():
    #Quick little check, leaving this in for now
    #print(Base.metadata.tables.keys())
    #print(Base.metadata.tables)
    posted_command = SailLogicCommandSchema(only=('commandID', 'commandValue'))\
        .load(request.get_json())
    model = SailLogicCommand(**posted_command, created_by="HTTP post request")
    session = Session()
    session.add(model)
    session.commit()
    new_model = SailLogicCommandSchema().dump(model)
    session.close()
    return jsonify(new_model), 201

if __name__ == '__main__':
    app.run()