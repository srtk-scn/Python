# def form(name,phon,email,phon2,email2):
#     print("name in the form is", name)
#     print("primary phone number is", phon)
#     print("primary email id is", email)
#     print("alternative phone is", phon2)
#     print("alternative email id is", email2)
# rusult= form("sarthak",463253256,"ram@gmail.com",email2="sachan@gmail.com",phon2=4862445625)
# print(rusult)

def form(name,phon,email,phon2=None,email2=None):
    print("name in the form is", name)
    print("primary phone number is", phon)
    print("primary email id is", email)
    if phon2 != None:
        print("alternative phone is", phon2)
    if email2 != None:
        print("alternative email id is", email2)
    print("-"*50)
form("sarthak",463253256,"ram@gmail.com")
form("sarthak",463253256,"ram@gmail.com",455652455)
form("sarthak",463253256,"ram@gmail.com",4556524152,"sachan@gmail.com")
form("sarthak",463253256,"ram@gmail.com",email2="adff@duffar.com")
form("sarthak",463253256,"ram@gmail.com",email2="adfdg@duffer.com",phon2=485652)
