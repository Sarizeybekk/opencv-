import cv2
import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QVBoxLayout, QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer

class ObjectTrackingApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Object Tracking with OpenCV")
        self.setGeometry(100, 100, 800, 600)

        self.video_label = QLabel(self)
        self.video_label.setGeometry(20, 20, 640, 480)

        self.select_button = QPushButton("Select Video", self)
        self.select_button.setGeometry(20, 520, 100, 30)
        self.select_button.clicked.connect(self.select_video)

        self.start_button = QPushButton("Start Tracking", self)
        self.start_button.setGeometry(140, 520, 100, 30)
        self.start_button.clicked.connect(self.start_tracking)
        self.start_button.setEnabled(False)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)

        self.cap = None
        self.tracker = cv2.TrackerKCF_create()
        self.bbox = None

    def select_video(self):
        video_path, _ = QFileDialog.getOpenFileName(self, "Select Video", "", "Video Files (*.mp4 *.avi *.mov)")
        if video_path:
            self.cap = cv2.VideoCapture(video_path)
            ret, frame = self.cap.read()
            if ret:
                self.start_button.setEnabled(True)
                self.display_frame(frame)

    def start_tracking(self):
        if self.cap:
            ret, frame = self.cap.read()
            if ret:
                self.bbox = cv2.selectROI("Frame", frame, False, False)
                cv2.destroyWindow("Frame")
                self.tracker.init(frame, self.bbox)
                self.timer.start(30)

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            self.timer.stop()
            self.cap.release()
            return

        success, self.bbox = self.tracker.update(frame)
        if success:
            p1 = (int(self.bbox[0]), int(self.bbox[1]))
            p2 = (int(self.bbox[0] + self.bbox[2]), int(self.bbox[1] + self.bbox[3]))
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)

        self.display_frame(frame)

    def display_frame(self, frame):
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.video_label.setPixmap(QPixmap.fromImage(qt_image))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = ObjectTrackingApp()
    main_window.show()
    sys.exit(app.exec_())


