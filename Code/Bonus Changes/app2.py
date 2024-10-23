from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models.rule_model import store_rule, get_all_rules, modify_rule

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rules.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model
class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rule_string = db.Column(db.String(200), nullable=False)
    rule_ast = db.Column(db.String(500), nullable=False)

# Create the database tables within an application context
with app.app_context():
    db.create_all()

@app.route('/create_rule', methods=['POST'])
def api_create_rule():
    data = request.get_json()
    rule_string = data.get("rule_string")
    
    # Error handling for invalid rule string
    if not rule_string or not is_valid_rule(rule_string):
        return jsonify({"error": "Invalid rule string."}), 400
    
    rule_ast = generate_rule_ast(rule_string)  # Assuming you have this function
    store_rule(rule_string, rule_ast)
    return jsonify({"message": "Rule created successfully."}), 201

@app.route('/modify_rule/<int:rule_id>', methods=['PUT'])
def api_modify_rule(rule_id):
    data = request.get_json()
    new_rule_string = data.get("rule_string")

    # Validate the new rule string
    if not new_rule_string or not is_valid_rule(new_rule_string):
        return jsonify({"error": "Invalid rule string."}), 400
    
    modified = modify_rule(rule_id, new_rule_string)
    if modified:
        return jsonify({"message": "Rule modified successfully."}), 200
    else:
        return jsonify({"error": "Rule not found."}), 404

def is_valid_rule(rule_string):
    # Basic validation logic (to be extended as needed)
    # Check for valid operators and structure
    valid_operators = ['AND', 'OR', '=', '<', '>', '<=', '>=']
    for operator in valid_operators:
        if operator in rule_string:
            return True
    return False

if __name__ == '__main__':
    app.run(debug=True)
