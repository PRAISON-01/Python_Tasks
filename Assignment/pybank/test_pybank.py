from unittest import TestCase 

import pybank

class TestValidatEmail (TestCase):
    def test_that_valid_email_exist(self):
        pybank.validate_email("praise@gmail.com")

    def test_that_email_length_is_minimum_of_8_characters(self):
        is_valid = pybank.validate_email("praise@gmail.com")
        self.assertTrue(is_valid)

    def test_that_email_length_is_less_than_8_characters(self):
        is_valid = pybank.validate_email("pr@.com")
        self.assertFalse(is_valid)

    def test_that_email_contains_special_character(self):
        is_valid = pybank.validate_email("praise@gmail.com")
        self.assertTrue(is_valid)

    def test_that_email_does_not_start_with_special_character(self):
        in_valid = pybank.validate_email("@praisegmail.com") 
        self.assertTrue(in_valid, "Invalid Email")

    def test_that_email_does_not_end_with_special_character(self):
        in_valid = pybank.validate_email("@praisegmail.com@") 
        self.assertTrue(in_valid, "Invalid Email")

class TestCalculateBalance (TestCase):
    def test_that_calculate_balance_returns_correct_balance(self):
        actual = pybank.calculate_balance([2500,2000])
        expected = 4500
        self.assertEqual(actual, expected)

        actual = pybank.calculate_balance([2500,5000])
        expected = 7500
        self.assertEqual(actual, expected)

        actual = pybank.calculate_balance([5000, -1000, 2000, -500])
        expected = 5500
        self.assertEqual(actual, expected)

    def test_that_empty_transaction_returns_zero(self):
        actual = pybank.calculate_balance([0])
        expected = 0
        self.assertEqual(actual, expected)

class TestStrongPassword (TestCase):
    def test_that_password_is_minimum_of_8_characters_return_true(self):
        is_valid = pybank.is_strong_password("password")
        self.assertTrue(is_valid)

    def test_that_password_is_less_than_8_characters_return_false(self):
        is_valid = pybank.is_strong_password("passwor")
        self.assertFalse(is_valid)

class TestApplyInterest (TestCase):
    def test_that_apply_interest_returns_correct_balance(self):
        actual = pybank.apply_interest(5000, 0.05, 10)
        expected = 8144.47
        self.assertEqual(actual, expected)

    def test_that_rate_raises_value_error_if_rate_is_less_than_zero(self):
        with self.assertRaises(ValueError):
            pybank.apply_interest(5000, -0.05, 10)

    def test_that_rate_raises_value_error_if_year_is_less_than_1(self):
        with self.assertRaises(ValueError):
            pybank.apply_interest(5000, 0.05, 0)
        
class TestGetTransactionSummary(TestCase):
    def test_that_transaction_summary_is_correct(self):
         transactions = [["credit", 2000], ["debit", 500], ["credit", 1000]]
        actual = pybank.get_transaction_summary(transactions)
        expected = [["total_credits", 3000], ["total_debits", 500], ["net_balance", 2500], ["transaction_count", 3]]
        self.assertEqual(actual, expected)
