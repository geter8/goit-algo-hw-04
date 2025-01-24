from unittest import expectedFailure


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
    except ValueError:
        return "for add contact you shoud add name and number"
    return "Contact added."

def change_data(args,contacts):
    name,phone = args
    if name in contacts:
        contacts[name] = phone
        return "phone is changed"
    else:
       return "name is not find firstly try to add contact"

def get_number(args,contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else :
        return "name is incorrect"

def get_all_info(contacts):
    info = []
    for name, phone in contacts.items():
        info.append(f"name: {name}, phone: {phone}")
    return "\n".join(info)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit","stop"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_data(args,contacts))
        elif command == "get_num":
            print(get_number(args,contacts))
        elif command == "get_all":
            print(get_all_info(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
