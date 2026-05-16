# Import all utilities
from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

"""
Implement homepage route that returns a welcome message, don't forget to include the status message upon successful load.
"""
@app.route("/", methods={"GET"})
def home():
    # Return a welcome message
    return jsonify({"message": "Welcome to the homepage"}), 200

"""
Implement GET /products route that returns all products or filters by category
"""

@app.route("/products", methods=["GET"])
def get_products():
    
    # Return all products or filter by ?category=
    category = request.args.get("category")

    # Control flow
    if category:
        filtered = [item for item in data if item["category"] == category]
        return jsonify(filtered), 200
    return jsonify(data), 200

"""
Implement GET /products/<id> route that returns a specific product by ID or 404. For a unique identifier.
"""
@app.route("/products/<int:id>", methods={"GET"})
def get_product_by_id(id):

    # Return product by ID or 404
    for product in data:
        # Control flow
        if product["id"] == id:
            return jsonify(product), 200
        return jsonify({"message": "Product not found"}), 404
    
if __name__ == "__main__":
    app.run(debug=True)
