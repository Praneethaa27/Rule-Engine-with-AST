# Rule-Engine-with-AST
**Objective:** Develop a simple 3-tier rule engine application(Simple UI, API and Backend, Data) to determine user eligibility based on attributes like age, department, income, spend etc.The system can use Abstract Syntax Tree (AST) to represent conditional rules and allow for dynamic creation,combination, and modification of these rules.

**Application Design**: Rule Engine with AST

We can break down the project into the following parts:

#### 1. **Architecture Overview**:
   
- **Frontend (UI)**: A simple interface where users can input rules, view existing rules, and test with sample data.
- **API Layer:** The interface that handles requests to create rules, combine rules, and evaluate them based on JSON input.
- **Backend**: Handles rule parsing, combination, and evaluation logic, working with an AST (Abstract Syntax Tree).
- **Database**: Stores rules and metadata for later retrieval and modification.

#### 2. **API Design:**
- **create_rule(rule_string):**
   > Parse a rule string and convert it into an AST structure using custom or standard parsing techniques (like Python's ast module).
   >	Return a Node object representing the AST.
- **combine_rules(rules):**
   >  Merge multiple rules into a single AST.
   >	The AST should be optimized for efficient evaluation.
   >	Return the root node of the combined AST.
- **evaluate_rule(JSON_data):**
   >  Use the generated AST to evaluate the rule against the provided user data (JSON format).
   >	Return True if the data meets the conditions in the rule, otherwise False.

#### 3. **AST Data Structure:**
A rule AST can be represented by a simple Node structure with fields for type, left, right, and value:


   class Node:
   
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type  # 'operator' or 'operand'
        self.value = value  # for operands (like 'age > 30')
        self.left = left  # left child node (for operators like AND/OR)
        self.right = right  # right child node (for operators like AND/OR)

        
5. Detailed Design:
(A) Create Rule (create_rule):
•	Input: A rule string like "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
•	This function parses the rule and converts it into an AST structure.
Steps:
1.	Tokenize the rule string.
2.	Construct an AST where nodes represent operators (AND, OR) and operands (age > 30, salary > 50000).
3.	Return the root of the AST.
Example for create_rule("age > 30 AND department = 'Sales'"):
python
Copy code
rule1 = Node("operator", "AND",
             Node("operand", "age > 30"),
             Node("operand", "department = 'Sales'")
            )
(B) Combine Rules (combine_rules):
•	Input: List of rule strings.
•	This function takes the ASTs for individual rules and combines them using an efficient strategy.
Example: Combining rule1 and rule2 using the AND operator.
python
Copy code
def combine_rules(rules):
    # Assuming 'rules' is a list of rule strings
    combined_root = None
    for rule_string in rules:
        rule_ast = create_rule(rule_string)
        if combined_root:
            combined_root = Node("operator", "AND", combined_root, rule_ast)
        else:
            combined_root = rule_ast
    return combined_root
(C) Evaluate Rule (evaluate_rule):
•	Input: The combined rule’s AST and a dictionary of user attributes.
•	This function recursively evaluates the AST based on the user data.
python
Copy code
def evaluate_rule(ast, user_data):
    if ast.type == "operand":
        return eval_condition(ast.value, user_data)
    elif ast.type == "operator":
        left_result = evaluate_rule(ast.left, user_data)
        right_result = evaluate_rule(ast.right, user_data)
        if ast.value == "AND":
            return left_result and right_result
        elif ast.value == "OR":
            return left_result or right_result
    return False

def eval_condition(condition, user_data):
    # For example, 'age > 30' becomes `user_data['age'] > 30`
    return eval(condition.format(**user_data))
5. Test Cases:
•	Test 1: Create individual rules:
o	Input: create_rule("age > 30 AND department = 'Sales'")
o	Expected Output: AST representation of the rule.
•	Test 2: Combine rules:
o	Input: Combine "age > 30 AND department = 'Sales'" and "salary > 50000"
o	Expected Output: AST representing "(age > 30 AND department = 'Sales') AND (salary > 50000)"
•	Test 3: Evaluate combined rule:
o	Input: Rule AST, and user data {'age': 35, 'department': 'Sales', 'salary': 60000}
o	Expected Output: True
6. Data Storage:
•	Choice of Database: Use a SQL database like PostgreSQL or a NoSQL solution like MongoDB.
o	SQL for strict schema and relations.
o	NoSQL for dynamic rules and schema-less flexibility.
Schema Example (SQL):
•	Rules Table:
o	id: Unique identifier
o	rule_string: Original rule string
o	ast: Serialized AST structure
o	created_at: Timestamp
o	updated_at: Timestamp
sql
Copy code
CREATE TABLE rules (
  id SERIAL PRIMARY KEY,
  rule_string TEXT NOT NULL,
  ast JSONB,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);
Schema Example (MongoDB):
•	MongoDB document for rules:
json
Copy code
{
  "_id": ObjectId("..."),
  "rule_string": "age > 30 AND department = 'Sales'",
  "ast": {
    "type": "operator",
    "value": "AND",
    "left": {"type": "operand", "value": "age > 30"},
    "right": {"type": "operand", "value": "department = 'Sales'"}
  },
  "created_at": "2024-10-23T12:34:56Z",
  "updated_at": "2024-10-23T12:34:56Z"
}
7. Sample Rules for Testing:
•	Rule 1: "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
•	Rule 2: "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"
These can be used to verify AST creation, combination, and evaluation logic.

