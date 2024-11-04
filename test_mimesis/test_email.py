def validate_email(email):
    print(email)
    return True

def test_validate_email(mimesis):
    assert validate_email(mimesis('email'))