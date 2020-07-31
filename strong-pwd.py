import string

def contains(pw, criteria):
    return len(set.intersection( set(pw) , set(criteria))) > 0

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    count = 0 
    criterias = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]

    for criteria in criterias:
        if not contains(password, criteria):
            count += 1
    
    if len(password) < 6:
        missing = 6 - len(password)
        return max(count, missing)

    return count
