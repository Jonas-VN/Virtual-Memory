from Page import Page


class Frame:
    def __init__(self, frame_number):
        self.frame_number = frame_number
        self.process_id = None
        self.page = Page(None)

    def get_frame_number(self):
        return self.frame_number

    def get_process_id(self):
        return self.process_id

    def get_page(self):
        return self.page

    def set_process_id(self, process_id):
        self.process_id = process_id

    def set_page(self, page):
        self.page = page
