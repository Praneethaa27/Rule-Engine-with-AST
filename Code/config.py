from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models.rule_model import store_rule, get_all_rules

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rules.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create your database models here, if not in separate files
class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rule_string = db.Column(db.String(200), nullable=False)
    rule_ast = db.Column(db.String(500), nullable=False)

# Create the database tables within an application context
with app.app_context():
    db.create_all()  # Create the database tables

@app.route('/combine_rules', methods=['POST'])
def api_combine_rules():
    # Your logic for combining rules
    return jsonify({"message": "Rules combined successfully"}), 200

@app.route('/evaluate_rule', methods=['POST'])
def api_evaluate_rule():
    # Your logic for evaluating a rule
    return jsonify({"message": "Rule evaluated successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
