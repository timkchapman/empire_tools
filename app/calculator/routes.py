from app.calculator import bp
from app.calculator.functions import convert_to_rings, convert_from_rings
from flask import render_template, request, jsonify, redirect

@bp.route('/calculator')
def index():
    return render_template('calculator.html')

@bp.route('/calculator/')
def calculator_with_slash():
    return redirect('/calculator')

@bp.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    rings = data.get('rings', 0)
    crowns = data.get('crowns', 0)
    thrones = data.get('thrones', 0)
    output_unit = data.get('output_unit', 'rings').lower()

    total_rings = convert_to_rings(rings, crowns, thrones)
    result = convert_from_rings(total_rings, output_unit)

    return jsonify({'result': result, 'unit': output_unit})