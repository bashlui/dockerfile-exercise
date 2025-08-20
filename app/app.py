from flask import Flask, jsonify, request, abort

app = Flask(__name__)

news = [{"id": 0, "title": "", "content": ""}]
next_id = 1


@app.route("/", methods=["GET"])
def index():
    pass

# Expected: list with only one element
@app.route("/news", methods=["GET"])
def list_news():
    return jsonify({"count": len(news), "items": news})

# Expected: it will echo the same data submitted in the body
@app.route("/news", methods=["POST"])
def create_news():
    data = request.json
    # Add the new to the array
    news.append({"id": next_id, **data})
    return jsonify(data), 201


# Expected: update an element in the list
@app.route("/news/<int:item_id>", methods=["PUT"])
def update_news(item_id: int):
    item = news[item_id]
    data = request.json
    for key in ("title", "content"):
        if key in data:
            item[key] = data[key]
    return jsonify(item)

# Expected: delete an element bia id.
@app.route("/news/<int:item_id>", methods=["DELETE"])
def delete_news(item_id: int):
    del news[item_id]
    return jsonify({"status": "deleted", "id": item_id})

if __name__ == "__main__":
    app.run(threaded=True, host="0.0.0.0", port=3000)