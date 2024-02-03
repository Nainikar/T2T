from flask import Flask, request, jsonify

app = Flask(__name__)

def optimize_route(locations):
    # Replace this with your actual route optimization algorithm
    # For now, let's just reverse the order of locations as a simple example
    optimized_route = list(reversed(locations))
    return optimized_route

@app.route('/optimize-route', methods=['POST'])
def optimize_route_api():
    try:
        data = request.get_json()

        # Ensure 'locations' key is present in the request
        if 'locations' not in data:
            return jsonify({'error': 'Missing "locations" key in the request'}), 400

        locations = data['locations']

        # Check if locations is a list
        if not isinstance(locations, list):
            return jsonify({'error': '"locations" must be a list of locations'}), 400

        # Ensure at least two locations are provided for optimization
        if len(locations) < 2:
            return jsonify({'error': 'At least two locations are required for optimization'}), 400

        optimized_route = optimize_route(locations)

        return jsonify({'optimized_route': optimized_route})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
