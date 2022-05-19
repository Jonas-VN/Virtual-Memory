class Instruction:
    def __init__(self, process_id, operation, address):
        self.process_id = process_id
        self.operation = operation
        self.address = address

    def __repr__(self):
        return "Process ID: " + str(self.process_id) + " | Operation: " + str(self.operation) + " | Virtual Address: " + str(self.address)

    def get_process_id(self):
        return self.process_id

    def get_operation(self):
        return self.operation

    def get_address(self):
        return self.address
