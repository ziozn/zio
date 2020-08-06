import configparser


class ReadIni:

    def __init__(self, file_name=None, node=None):
        if file_name is None:
            file_name = 'C:/Users/Administrator/PycharmProjects/AppiumCansee/config/localElement.ini'
        if node is None:
            self.node = 'login_element'
        else:
            self.node = node
        self.cf = self.load_ini(file_name)

    @staticmethod
    def load_ini(file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name, encoding="utf-8-sig")
        print(cf.read(file_name, encoding="utf-8-sig"))
        return cf

    def get_value(self, key):
        data = self.cf.get(self.node, key)
        return data


if __name__ == '__main__':
    read_init = ReadIni()
    print(read_init.get_value('login_domain'))
