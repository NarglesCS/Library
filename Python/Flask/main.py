from flask import Flask, request, jsonify

app = Flask(__name__)

ls_book = [
    {
        "id":0,
        "book":'Anthem',
    }
]



@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/books', methods=['GET','POST'])
def books():
    if request.method == 'GET':
        if len(ls_book) >0:
            return jsonify(ls_book), 200
        else:
            'Nothing found', 404
    elif request.methods == 'POST':
        new_obj= {
            "id":(ls_book[-1]['id']+1),
            "book": request.form['book']
        }
        ls_book.append(new_obj)
        return jsonify(ls_book), 201

@app.route('/books/<id:int>', methods=['GET', 'PUT', 'DELETE'])
def search_books():
    if request.method == 'GET':
        if len(ls_book) >0:
            
            for bk in ls_book:
                if bk['id'] == id:
                    return jsonify(bk), 200
            return 'Nothing found', 404
        else:
            'Nothing found', 404
    elif request.method == 'PUT':
        new_obj{
            'id':id,
            'book': request.form['book']
        }
        for bk in ls_book:
            if bk['id'] == id:
                bk = new_obj

        return jsonify(ls_book), 201
    elif request.method == 'DELETE':
        for bk in ls_book:
            if bk['id'] == id:
                ls_book.pop(ls_book.index(bk))

        return jsonify(ls_book), 201

if __name__ == "__main__":
    app.run()
