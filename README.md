# RealTime-ColorDetection-using-Computer-Vision-Vityarthi

## Project Overview

This project implements a real-time **Multi-Color Detection and Tracking system** using computer vision techniques. It detects multiple colors through a webcam feed and highlights them with bounding circles and labels.

The system uses HSV color space segmentation and masking to identify colors such as red, green, blue, yellow, and more in real time.

This project demonstrates practical applications of image processing, object tracking, and real-time video analysis using Python and OpenCV.

---

## Problem Statement

Detecting and tracking multiple colored objects in real time can be challenging due to:

* Variations in lighting conditions
* Overlapping color ranges
* Noise and false detections

This project solves these challenges by using HSV-based color segmentation, masking, and contour detection to accurately track multiple colors simultaneously.

---

## Why This Project Matters

* Demonstrates core computer vision concepts in a practical way
* Helps understand **HSV color space and masking techniques**
* Acts as a foundation for advanced applications like:

  * Augmented Reality (AR)
  * Gesture-based systems
  * Object tracking systems
  * Surveillance and automation

---

## Tech Stack

**Language:** Python

**Libraries:**

* OpenCV
* NumPy

---

## How It Works

1. Capture video frames from the webcam
2. Convert frames from BGR to HSV color space
3. Define HSV ranges for multiple colors
4. Create masks for each color
5. Remove noise using blur
6. Detect contours of colored objects
7. Draw bounding circles and labels on detected objects
8. Display the final output in real time

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Ish-Me/RealTime-ColorDetection-using-Computer-Vision-Vityarthi.git
cd RealTime-ColorDetection-using-Computer-Vision-Vityarthi
```

### 2. Install Dependencies

```bash
pip install opencv-python numpy
```

### 3. Run the Project

```bash
python main.py
```

---

## Usage Instructions

* Show colored objects in front of your webcam
* The system will detect and label them in real time
* Press `ESC` to exit the application

---

## Project Structure

```
├── colordetection.py                # Main script  
├── requirements.txt      # Dependencies  
└── README.md             # Project documentation  
```

---

## Colors Supported

* Red
* Green
* Blue
* Yellow
* Orange
* Purple
* Brown
* Pink
* Black

---

## Challenges Faced

* Lighting sensitivity affects color detection
* Overlapping HSV ranges (e.g., orange & yellow)
* Noise in detection requiring threshold tuning

---

## Key Learnings

* Understanding of HSV color space
* Real-time video processing using OpenCV
* Contour detection and object tracking
* Noise reduction techniques in image processing

---

## Future Improvements

* Add HSV trackbars for dynamic tuning
* Implement object tracking trails
* Build an Air Drawing system using colors
* Integrate GUI for better control
* Optimize performance for higher FPS

---

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## License

This project is open-source and available under the MIT License.

---

## Acknowledgements

* OpenCV documentation and community
* Computer vision learning resources

---

## Author

Ishaan Mehrotra B.Tech CSE (AI & ML) Student
