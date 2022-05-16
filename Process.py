from Page import Page


class Process:
    def __init__(self, process_id):
        self.process_id = process_id
        self.page_table = []
        self.page_faults = 0
        self.page_in = 0
        self.page_out = 0

        for i in range(16):
            self.page_table.append(Page(i))

    def __str__(self):
        return "Process ID: " + str(self.process_id) + "\n" + \
               "Page Table: " + str(self.page_table) + "\n" + \
               "Page Faults: " + str(self.page_faults) + "\n"

    def get_process_id(self):
        return self.process_id

    def get_page_table(self):
        return self.page_table

    def get_page_faults(self):
        return self.page_faults

    def get_page_in(self):
        return self.page_in

    def get_page_out(self):
        return self.page_out

    def set_page_in(self, page_in):
        self.page_in = page_in

    def set_page_out(self, page_out):
        self.page_out = page_out

    def set_page_faults(self, page_faults):
        self.page_faults = page_faults

    def set_page_table(self, page_table):
        self.page_table = page_table

    def set_process_id(self, process_id):
        self.process_id = process_id

    @staticmethod
    def address_to_page(address):
        return address // 4096

    def write(self, address):
        page_number = self.address_to_page(address)
        self.page_table[page_number].set_modified_bit(True)

    def get_page(self, address):
        page_number = self.address_to_page(address)
        return self.page_table[page_number]

    def increment_page_faults(self):
        self.page_faults += 1

    def increment_page_in(self):
        self.page_in += 1

    def increment_page_out(self):
        self.page_out += 1
