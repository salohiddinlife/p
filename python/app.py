from flask import Flask, jsonify

app = Flask(__name__)

# Sample data
data = [
    {'id': 1, 'name': 'todo', 'url': 'https://salohiddinlife.github.io/todo/'},
    {'id': 2, 'name': 'vue-grocery', 'url': 'https://github.com/salohiddinlife/diplomka'},
    {'id': 3, 'name': 'cinephile', 'url': 'https://github.com/salohiddinlife/cinephile'}
]

# Route to get all products
@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(data)

# Route to get a specific product by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in data if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
