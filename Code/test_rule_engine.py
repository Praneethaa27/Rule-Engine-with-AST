import unittest
from services.rule_service import create_rule, combine_rules, evaluate_rule

class TestRuleEngine(unittest.TestCase):

    def test_create_rule(self):
        rule_string = "age > 30 AND department = 'Sales'"
        ast = create_rule(rule_string)
        self.assertEqual(ast.type, "operator")
        self.assertEqual(ast.value, "AND")

    def test_combine_rules(self):
        rules = ["age > 30 AND department = 'Sales'", "salary > 50000"]
        combined_ast = combine_rules(rules)
        self.assertEqual(combined_ast.value, "AND")

    def test_evaluate_rule(self):
        rule_string = "age > 30 AND department = 'Sales'"
        ast = create_rule(rule_string)
        user_data = {'age': 35, 'department': 'Sales'}
        result = evaluate_rule(ast, user_data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
