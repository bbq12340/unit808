import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import QFile, QThread, QDir
from ui_mainWindow import Ui_MainWindow
from worker import Worker

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.urlRadioButton.toggled.connect(self.handleChecked_url)
        self.ui.fileRadioButton.toggled.connect(self.handleChecked_file) 
        self.ui.fileOpenButton.clicked.connect(self.handle_fileOpen)
        self.ui.startButton.clicked.connect(self.handleClicked)
    
    def handle_fileOpen(self):
        current_path = QDir.currentPath()
        filter = QDir(current_path, "text files (*.txt)").filter()
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(filter)
        filename = dlg.getOpenFileName()
        f = open(filename[0], 'r')
        self.ui.fileLabel.setText(filename[0].split('/')[-1])
        with f:
            self.link_list = f.read().splitlines()
        return
    
    def handleChecked_file(self):
        self.ui.fileFrame.setEnabled(True)
        self.ui.urlFrame.setEnabled(False)
    
    def handleChecked_url(self):
        self.ui.urlFrame.setEnabled(True)
        self.ui.fileFrame.setEnabled(False)
    
    def handleClicked(self):
        if self.ui.urlRadioButton.isChecked():
            input_data = self.ui.urlEdit.text()
        elif self.ui.fileRadioButton.isChecked():
            input_data = self.link_list
        self.thread = QThread()
        self.worker = Worker(input_data)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.ui.progressBar.setValue)
        self.thread.start()
        self.ui.startButton.setEnabled(False)
        self.ui.inputFrame.setEnabled(False)
        self.thread.finished.connect(self.handleFinished)
    
    def handleFinished(self):
        self.ui.startButton.setEnabled(True)
        self.ui.inputFrame.setEnabled(True)
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("수집이 완료되었습니다.")
        msgBox.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())