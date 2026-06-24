def is_strong(password):
    msg = 'Password must contain at least'
    
    if len(password) < 8:
        return False, msg + "8 characters"
    
    has_upper =  any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_one_dig = any(c.isdigit() for c in password)
    spec_char = set("!@#$%&*-_.+=")
    has_spec_char = any(c in spec_char for c in password)
    
    if not has_upper:
        return False, msg + "one uppercase letter"
    if not has_lower:
        return False, msg + "one lowercase letter"
    if not has_one_dig:
        return False, msg + "one digit"
    if not has_spec_char:
        return False, msg + "one special character (!@#$%^&*-_+=)"
        
    return True, "Password is Strong!"

password = str(input("Enter the Password: "))

valid, message = is_strong(password)
print(message)
