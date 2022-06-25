class Host:
    def __init__(self, ip):
        self.ip=ip
        self.ports = []
        self.os=""

    # get funcs
    def get_ip(self):
        return str(self.ip)

    def get_port_list(self):
        return self.ports

    def get_os(self):
        return str(self.os)

    # set funcs
    def add_port(self, port):
        self.ports.append(port)

    def set_os(self, os):
        self.os = os

class Port:
    def __init(self, number, protocol, service="", product="", version=""):
        self.number = number
        self.protocol = protocol
        self.service = service
        self.product = product
        self.version = version

    # get funcs
    def get_number(self):
        return self.number
        
    def get_protocol(self):
        return self.protocol
    
    def get_service(self):
        return self.service

    def get_product(self):
        return self.product
    
    def get_version(self):
        return self.version
    
    # set funcs
    def set_service(self, service):
        self.service = service
    
    def set_product(self, product):
        self.product = product
    
    def set_version(self, version):
        self.version = version
    