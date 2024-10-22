def mailer(mail_body):
    def inner(name):
        print("Dear Mr/Ms.", name)
        print("\t*** Greating fron ICICI***")
        mail_body()
        print("thanks and regards")
        print("ICICIC team")
    return inner
@mailer
def loan_approval_body():
    print("As discussed yur personal loan is approved")
    print("Kindly visit the for confirmaion")
@mailer
def loan_recovery_boady():
    print("As discussed you idiot fellow have not paid the loan\
amount pay it as soon as possible else we shoot you ")
    print("kindly ignore the message if you have already paid")
loan_approval_body("raju")
loan_recovery_boady("Dinga")