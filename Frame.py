from Page import Page


class Frame:
    def __init__(self, frame_number):
        self.frame_number = frame_number
        self.process_id = -1
        self.page = Page(-1)

    def __str__(self):
        return "Frame: " + str(self.frame_number) + " Process: " + str(self.process_id) + " Page: " + str(self.get_page())

    def get_frame_number(self):
        return self.frame_number

    def get_process_id(self):
        return self.process_id

    def get_page(self):
        return self.page

    def set_frame_number(self, frame_number):
        self.frame_number = frame_number

    def set_process_id(self, process_id):
        self.process_id = process_id

    def set_page(self, page):
        self.page = page

    def get_page_number(self):
        if self.page is not None:
            return self.page.get_page_number()
        else:
            return -1
