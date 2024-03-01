def add_user(name, lastname, age, address, email, phone):
    users.append((name, lastname, age, address, email, phone))
users = []
while True:
    name = input("Ismingizni kiriting: ")
    lastname = input("Familiyangizni kiriting: ")
    age = input("Yoshingizni kiriting: ")
    address = input("Manzilingizni kiriting: ")
    email = input("Emailingizni kiriting: ")
    phone = input("Telefon raqamingizni kiriting: ")
    if phone[::4] == "+998" or len(phone[14]):
        pass
    else:
        break
    add_user(name, lastname, age, address, email, phone)
    stop = input("Dasturni to'xtatish uchun 'stop' deb yozasizmi: ")
    if stop.lower() == "stop":
        break
for user in users:
    print(users)