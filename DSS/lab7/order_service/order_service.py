from flask import Flask, request, jsonify

app = Flask(__name__)

orders = []

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    orders.append(data)
    return jsonify({'message': 'Order created successfully'})

@app.route('/orders/<user_id>', methods=['GET'])
def get_orders_for_user(user_id):
    user_orders = [order for order in orders if order.get('user_id') == user_id]
    return jsonify(user_orders)

if __name__ == '__main__':
    app.run(port=8082)
