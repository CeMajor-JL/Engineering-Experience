import string


def check_password_strength(password: str) -> dict:
    rules = {
        "length": len(password) >= 8,
        "uppercase": any(c.isupper() for c in password),
        "lowercase": any(c.islower() for c in password),
        "digit": any(c.isdigit() for c in password),
        "symbol": any(c in string.punctuation for c in password),
    }

    score = sum(rules.values())

    return {
        "score": score,
        "max_score": len(rules),
        "rules": rules,
        "strong": score >= 4
    }


if __name__ == "__main__":
    pwd = input("Enter password: ")
    result = check_password_strength(pwd)

    print("\nPassword analysis:")
    for rule, passed in result["rules"].items():
        print(f"- {rule}: {'OK' if passed else 'FAIL'}")

    print(f"\nStrength: {result['score']}/{result['max_score']}")
    print("Status:", "Strong" if result["strong"] else "Weak")