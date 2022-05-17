from Page import Page


class Process:
    def __init__(self, process_id):
        self.process_id = process_id
        self.page_table = [Page(i) for i in range(16)]
        self.page_in = 0
        self.page_out = 0

    def get_process_id(self):
        return self.process_id

    def get_page_table(self):
        return self.page_table

    def get_page_in(self):
        return self.page_in

    def get_page_out(self):
        return self.page_out

    @staticmethod
    def address_to_page(address):
        return address // 4096

    def write(self, address):
        page_number = self.address_to_page(address)
        self.page_table[page_number].set_modified_bit(True)

    def get_page(self, address):
        page_number = self.address_to_page(address)
        return self.page_table[page_number]

    def increment_page_in(self):
        self.page_in += 1

    def increment_page_out(self):
        self.page_out += 1

    def clear_page_table(self):
        for page in self.page_table:
            page.clear_page()
