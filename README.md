
# 🎛️ Pinch Volume Controller using Computer Vision

Control your system volume in real-time using just your fingers!  
This project uses computer vision and hand tracking to detect a **pinch gesture** and map it to your system’s **audio volume** with a smooth virtual slider interface.

---

## 🚀 Features

✅ Real-time hand tracking using webcam  
✅ Pinch gesture detection for volume control  
✅ Smooth volume mapping & control  
✅ Virtual volume slider UI overlay  
✅ Works with real system volume  
✅ Clean exit & basic error handling  

---

## 🛠️ Technologies Used

- Python  
- OpenCV  
- MediaPipe  
- PyCaw  
- NumPy  

---

## 🎯 How It Works

1. The webcam captures live video.
2. MediaPipe detects and tracks hand landmarks.
3. The distance between thumb and index finger is calculated.
4. This distance is mapped to the system’s audio volume.
5. A virtual volume bar displays the change in real time.

---

## 📦 Installation

```bash
git clone https://github.com/your-username/Pinch-Volume-Controller.git
cd Pinch-Volume-Controller
pip install -r requirements.txt
````

---

## ▶️ Run the Project

```bash
python hand_gesture.py
```

Press **Q** to exit the application safely.

---

## 🖥️ Requirements

* Python 3.8 or higher
* Working webcam
* Supported audio drivers for PyCaw
* Windows or macOS

---

## 📁 Project Structure

```
Pinch-Volume-Controller/
│
├── hand_gesture.py
├── requirements.txt
├── README.md
└── venv/ (optional)
```

---

## 📸 Demo

Add your screenshots or screen recording here.

---

## 🌟 Learning Outcome

Through this project, I gained hands-on experience with:

* Real-time computer vision
* Hand gesture recognition
* MediaPipe hand landmark detection
* System-level audio control
* OpenCV UI overlays
* Debugging live CV applications

---

## 🙌 Author

**Sunidhi Chauhan**
CSE Student | Computer Vision & AI Enthusiast

---

## 📜 License

This project is licensed under the MIT License.

```

