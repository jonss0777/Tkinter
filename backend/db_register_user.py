from backend.database import connectToDatabase


# Documents
    # for now I will connect directly to the db but in the future I plan create a 
    # RESTAPI to handle CRUD operations
def db_register_user(user):
    register_user(user)

def register_user(user):
    if valid(user):
        print("valid user")
    else:
        print("invalid user")

def valid(user):
    for c in user:
        if not (c.isalpha() or c.isdigit() or c=='_'):
            return False
    return True


register_user("GreatUser")
register_user("031GreatUser")
register_user("Some#")
register_user("__SOmethisn1312")





