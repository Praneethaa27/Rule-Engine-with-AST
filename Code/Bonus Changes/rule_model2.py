from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rule_string = db.Column(db.String(200), nullable=False)
    rule_ast = db.Column(db.String(500), nullable=False)

def store_rule(rule_string, rule_ast):
    new_rule = Rule(rule_string=rule_string, rule_ast=rule_ast)
    db.session.add(new_rule)
    db.session.commit()

def modify_rule(rule_id, new_rule_string):
    rule = Rule.query.get(rule_id)
    if rule:
        rule.rule_string = new_rule_string
        rule.rule_ast = generate_rule_ast(new_rule_string)  # Update AST
        db.session.commit()
        return True
    return False

def generate_rule_ast(rule_string):
    # Implement your AST generation logic here
    return rule_string  # Placeholder for AST representation
