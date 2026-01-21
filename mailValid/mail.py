import re
from email_validator import validate_email, EmailNotValidError

def validate_email_address(email):
    """
    Validate an email address using email_validator.
    
    Args:
        email (str): The email address to validate
        
    Returns:
        dict: Contains 'valid' (bool) and 'message' (str)
    """
    try:
        # Validate and normalize the email
        valid_email = validate_email(email)
        return {
            'valid': True,
            'message': f'Valid email: {valid_email.email}',
            'normalized_email': valid_email.email
        }
    except EmailNotValidError as e:
        return {
            'valid': False,
            'message': f'Invalid email: {str(e)}'
        }


# Example usage:
if __name__ == '__main__':
    test_emails = [
        'user@example.com',
        'invalid.email@',
        'test@domain.co.uk',
        'no-at-sign.com'
    ]
    
    for email in test_emails:
        result = validate_email_address(email)
        print(f"{email}: {result}")