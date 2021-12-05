class PhoneContact:
    def __init__(self, name, contact_number, note):
        self.name = str(name)
        self.contact_number = str(contact_number)
        self.note = str(note)

    def string_information(self, name, contact_number, note):
        information = f'Name:{name}; Phone:{contact_number}; Note:{note}'
