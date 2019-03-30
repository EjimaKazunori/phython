def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent)
 
    # first checkbox
    self.upper = QCheckBox('大文字', self)
    self.upper.move(100, 30)
 
    # secand checkbox
    self.lower = QCheckBox('小文字', self)
    self.lower.move(180, 30)
 
    # grouping
    self.group = QButtonGroup()
    self.group.addButton(self.upper,1)
    self.group.addButton(self.lower,2)
 
    self.setGeometry(300, 50, 400, 350)
    self.setWindowTitle('QCheckBox')
