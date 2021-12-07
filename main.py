class UserContact:
    def __init__(self, name, contact_number, status):
        self.name = str(name)
        self.contact_number = str(contact_number)
        self.status = str(status)

    def string_information(self):
        information_dict = {"Name": self.name, "Contact number": self.contact_number, "Status": self.status}
        return information_dict


class UserBook:
    def __init__(self):
        self.list_contact = []

    def add_contact(self, user):
        self.list_contact.append(user)
        return self.list_contact

    def get_contact_by_name(self, name):
        for i in self.list_contact:
            if i['Name'] == name:
                return i







