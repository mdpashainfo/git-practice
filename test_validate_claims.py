
import unittest
from validate_claims import validate_claims


class TestClaimValidation(unittest.TestCase):

    def test_claim_validation(self):
        claims = [
            {"claim_id": 101, "claim_amount": 500},
            {"claim_id": 102, "claim_amount": -50},
            {"claim_id": None, "claim_amount": 300},
            {"claim_id": 101, "claim_amount": 500},
            {"claim_id": 103, "claim_amount": 200}
        ]

        valid, rejected = validate_claims(claims)

        self.assertEqual(len(valid), 2)
        self.assertEqual(len(rejected), 3)

        reasons = [reason for _, reason in rejected]

        self.assertIn("Missing claim ID", reasons)
        self.assertIn("Invalid claim amount", reasons)
        self.assertIn("Duplicate claim ID", reasons)


if __name__ == "__main__":
    unittest.main()
