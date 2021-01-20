from PySide6.QtCore import QThread, QObject, Signal
import pandas as pd
import datetime, time

from unitScraper import unitScraper

class Worker(QObject):
    finished = Signal()
    progress = Signal(float)

    def __init__(self, input):
        super().__init__()
        self.input_data = input

    def run(self):
        app = unitScraper()
        now = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
        if type(self.input_data) == str:
            data = app.extract_goods_single(self.input_data)
            df = pd.DataFrame([data], columns=list(data.keys()))
            df.to_csv(f"result/{now}.csv")
        elif type(self.input_data) == list:
            df = pd.DataFrame({}, columns=['imageLink','name','sellPrice','memberPrice','id','country','optionNames','html'])
            for link in self.input_data:
                self.progress.emit((self.input_data.index(link)+1)/len(self.input_data)*100)
                link = "https://unit808.com"+link
                data = app.extract_goods_single(link)
                df = df.append(pd.DataFrame([data], columns=list(data.keys())))
                time.sleep(0.5)
            df.to_csv(f"result/{now}.csv")
        self.finished.emit()