def get_ticket_Price(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    if age <=12:
        return 5 
    if age <=59:
        return 15
    if age >60:
        return 10