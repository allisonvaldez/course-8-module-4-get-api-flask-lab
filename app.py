# Import all utilities
from flask import Flask, jsonify, request, make_response
from data import products

app = Flask(__name__)

"""
Implement homepage route that returns a welcome message, don't forget to include the status message upon successful load.
"""
@app.route("/", methods=["GET"])
def home():
    # Return a welcome message
    return make_response(jsonify({"message": "Welcome to the homepage"}), 200)

"""
Implement GET /products route that returns all products or filters by category
"""

@app.route("/products", methods= ["GET"])
def get_products():

    # Return all products or filter by ?category=
    category = request.args.get("category")

    # Control flow
    if category:
        filtered = [p for p in products if p["category"].lower() == category.lower()]
        return make_response(jsonify(products), 200)
    
    # If a filtered product is not found return empty list
    return make_response(jsonify(filtered), 200)

"""
Implement GET /products/<id> route that returns a specific product by ID or 404. For a unique identifier.
"""
@app.route("/products/<int:id>", methods= ["GET"])
def get_product_by_id(id):

    # Search for products and return the first one that matches
    product = next((p for p in products if p["id"] == id), None)

    # Return product by ID or 404
    if product:
        # Control flow if product found
        return make_response(jsonify(product), 200)
    return make_response(jsonify({"error": f"No product found with id {id}"}), 404)

    
if __name__ == "__main__":
    app.run(debug=True)
