import re

VALID_OPERATORS = {'>', '<', '==', '!=', '>=', '<=', 'AND', 'OR'}
VALID_ATTRIBUTES = {'age', 'department', 'salary', 'experience'}

def validate_rule_string(rule_string):
    tokens = re.split(r'\s+', rule_string)
    for token in tokens:
        if not (token.isalnum() or token in VALID_OPERATORS or token in {"(", ")", "'", '"'}):
            return False
    return True

def validate_attributes(rule_string):
    attributes = re.findall(r'[a-zA-Z_]+', rule_string)
    for attr in attributes:
        if attr not in VALID_ATTRIBUTES:
            return False
    return True
