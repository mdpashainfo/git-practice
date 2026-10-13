
def validate_claims(claims):
    valid_claims = []
    rejected_claims = []
    seen_claim_ids = set()

    for claim in claims:
        claim_id = claim.get("claim_id")
        amount = claim.get("claim_amount")

        if claim_id is None or not str(claim_id).strip():
            rejected_claims.append((claim, "Missing claim ID"))

        elif isinstance(amount, bool) or not isinstance(amount, (int, float)) or amount <= 0:
            rejected_claims.append((claim, "Invalid claim amount"))

        elif claim_id in seen_claim_ids:
            rejected_claims.append((claim, "Duplicate claim ID"))

        else:
            valid_claims.append(claim)
            seen_claim_ids.add(claim_id)

    return valid_claims, rejected_claims


if __name__ == "__main__":
    claims = [
        {"claim_id": 101, "claim_amount": 500},
        {"claim_id": 102, "claim_amount": -50},
        {"claim_id": None, "claim_amount": 300},
        {"claim_id": 101, "claim_amount": 500},
        {"claim_id": 103, "claim_amount": 200}
    ]

    valid, rejected = validate_claims(claims)

    print("Valid claims:", valid)
    print("Rejected claims:", rejected)
    print("Valid count:", len(valid))
    print("Rejected count:", len(rejected))
