class Message:
    static_val = 'static!'

    def __init__(self, text_message='lets go and dring some coffee', author="Danylo", delivery_date=29, receiver="Yana",
                 phone="Samsung", time="19:30"):
        self.text_message = text_message
        self.author = author
        self.delivery_date = delivery_date
        self.receiver = receiver
        self.phone = phone
        self.time = time

    def __del__(self):
        print('destructor')

    def MessageInfo(self):
        print('Повідомлення: ' + self.text_message + '\nАвтор: ' + str(self.author) + '\nДата відправки: ' + str(
            self.delivery_date) +
              '\nОтримувач: ' + str(self.receiver) + '\nТелефон: ' + self.phone + '\nЧас: ' + str(self.time) + '\n')

    @staticmethod
    def Get_static_val(self):
        return self.static_val



