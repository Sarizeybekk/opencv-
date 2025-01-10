# 📹 Object Tracking Application

This project is a Python-based application for object tracking in video files. It leverages OpenCV for tracking algorithms and PyQt5 for the graphical user interface (GUI).

## ✨ Features
- 🎥 **Select a video file** to load.
- 📌 **Choose a region of interest (ROI)** to track within the video.
- ▶️ **Start** and ⏹️ **stop** the object tracking process.
- 🚀 Supports **KCF (Kernelized Correlation Filters)** tracking algorithm.
- 🖼️ Displays video frames in real-time with the tracked object highlighted.
- ⏲️ Handles **end-of-video** scenarios gracefully.

## 🛠️ Requirements
To run this project, you need the following dependencies:

- 🐍 Python 3.8 or higher
- 🧠 OpenCV
- 🖱️ PyQt5
- 🧮 NumPy

You can install the dependencies using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## 🚀 Installation
1. Clone the repository:
   ```bash
   git clone  
   cd object-tracking-app
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   # Windows
   env\Scripts\activate
   # macOS/Linux
   source env/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Usage
1. Run the application:
   ```bash
   python main.py
   ```

2. Click **"Select Video"** to load a video file.
3. Click **"Start Tracking"** to select an object in the video for tracking.
4. Use your mouse to draw a bounding box around the object, then press `ENTER` or `SPACE` to confirm.
5. The application will track the selected object in real-time.
6. Click **"Stop Tracking"** to halt the tracking process.

## 📁 Project Structure
- `main.py`: 🧠 Main application code.
- `requirements.txt`: 📜 List of dependencies.
- `README.md`: 📘 Documentation for the project.

## 🖼️ Screenshots
![image](https://github.com/user-attachments/assets/62ce836f-bf47-46a1-b79e-df1a48ecfdc2)

## 📝 Notes
- The application uses the **KCF tracker** by default, but you can modify the code to use other OpenCV-supported trackers such as **MOSSE** or **CSRT**.
- Ensure that the video file format is supported by OpenCV (e.g., `.mp4`, `.avi`, `.mov`).

## 📜 License
This project is licensed under the **MIT License**. See the `LICENSE` file for details.



## 🙏 Acknowledgments
- 🖥️ OpenCV for providing powerful computer vision tools.
- 🎨 PyQt5 for the GUI framework.

---






# opencv-
