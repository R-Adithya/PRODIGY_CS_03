import re

def password_strength(password):
    # Initialize strength and feedback
    strength = 0
    feedback = []

    # Check the length of the password
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters long.")
    else:
        feedback.append("Password length is acceptable.")
        strength += 1

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        feedback.append("Password contains uppercase letters.")
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        feedback.append("Password contains lowercase letters.")
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for digits
    if re.search(r'[0-9]', password):
        feedback.append("Password contains numbers.")
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Check for special characters
    if re.search(r'[\W_]', password):
        feedback.append("Password contains special characters.")
        strength += 1
    else:
        feedback.append("Password should contain at least one special character (e.g., @, #, $, etc.).")

    # Provide overall feedback based on the strength score
    if strength <= 2:
        feedback.append("Overall, your password is weak.")
    elif strength == 3:
        feedback.append("Overall, your password is moderate.")
    else:
        feedback.append("Overall, your password is strong.")

    return strength, feedback

# Main function to get input from user
password = input("Enter your password: ")
strength, feedback = password_strength(password)

print(f"Password Strength: {strength}/5")
print("Feedback:")
for comment in feedback:
    print(f"- {comment}")
