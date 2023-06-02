from PyQt5.QtCore import QObject, pyqtSignal

class MyObject(QObject):
    my_signal = pyqtSignal(str)
    
    def do_something(self):
        # 在这里执行某些操作
        result = "Done"
        self.my_signal.emit(result)

def handle_signal(value):
    print("Received value:", value)

obj1 = MyObject()
obj2 = QObject()

obj1.my_signal.connect(handle_signal)
obj1.do_something()