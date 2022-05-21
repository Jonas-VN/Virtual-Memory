class Page:
    def __init__(self, page_number):
        self.page_number = page_number
        self.present_bit = False
        self.modified_bit = False
        self.last_access_time = None
        self.frame_number = None

    def get_page_number(self):
        return self.page_number

    def get_present_bit(self):
        return self.present_bit

    def get_modified_bit(self):
        return self.modified_bit

    def get_last_access_time(self):
        return self.last_access_time

    def get_frame_number(self):
        return self.frame_number

    def set_page_number(self, page_number):
        self.page_number = page_number

    def set_present_bit(self, present_bit):
        self.present_bit = present_bit

    def set_modified_bit(self, modified_bit):
        self.modified_bit = modified_bit

    def set_last_access_time(self, last_access_time):
        self.last_access_time = last_access_time

    def set_frame_number(self, frame_number):
        self.frame_number = frame_number

    def set_page(self, frame_number):
        self.set_frame_number(frame_number)
        self.set_present_bit(True)

    def clear_page(self):
        self.set_present_bit(False)
        self.set_modified_bit(False)
        self.set_last_access_time(None)
        self.set_frame_number(None)
