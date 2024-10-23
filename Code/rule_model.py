from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rule_string = db.Column(db.String, nullable=False)
    rule_ast = db.Column(db.JSON, nullable=False)  # Store AST as JSON

def store_rule(rule_string, rule_ast):
    new_rule = Rule(rule_string=rule_string, rule_ast=rule_ast.to_dict())
    db.session.add(new_rule)
    db.session.commit()

def get_all_rules():
    return Rule.query.all()
