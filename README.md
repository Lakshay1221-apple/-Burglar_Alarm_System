# Theft Detection OpenCV

A lightweight computer vision project built with Python and OpenCV to detect motion from a live webcam feed and capture evidence frames when movement is detected. The repository also includes a small set of OpenCV practice scripts used for image reading, drawing, and basic image processing.

## Overview

The main application uses frame differencing to identify motion in a camera stream. When significant motion is detected, the system highlights the moving region, displays an alert on screen, and saves a snapshot to a local `detections/` directory.

This project is useful as a starting point for:

- Home or office motion monitoring prototypes
- Learning real-time video processing with OpenCV
- Experimenting with contour-based motion detection

## Features

- Real-time webcam capture with OpenCV
- Grayscale conversion and Gaussian blur for noise reduction
- Motion detection using buffered frame comparison
- Contour filtering to reduce small false positives
- Bounding boxes around detected movement
- Automatic snapshot saving on first detection event
- Separate demo scripts for foundational OpenCV concepts

## Project Structure

```text
Theft_Detection_Open_Cv/
├── bugler_presence.py
├── test.py
├── requirements.txt
├── Basics_OpenCv/
│   ├── annotation.py
│   ├── image_processing.py
│   └── read_image.py
└── README.md
```

## Main Script

### `bugler_presence.py`

This is the primary application in the repository. It:

1. Opens the default webcam
2. Captures frames continuously
3. Converts frames to grayscale and blurs them
4. Compares the oldest and newest frames in a rolling buffer
5. Thresholds the difference image
6. Finds contours representing motion
7. Draws detection boxes and saves an image when motion is first detected

Detected frames are saved inside a `detections/` folder, which is created automatically when the script runs.

## Supporting Scripts

### `test.py`

A simple webcam test utility to confirm that the camera opens correctly and frames are being received.

### `Basics_OpenCv/`

Practice scripts for basic OpenCV operations:

- `read_image.py`: reads and displays a local image
- `image_processing.py`: resizes, grayscales, blurs, and edge-detects an image
- `annotation.py`: draws a line on a blank canvas

These scripts are helpful for learning, but they are not required for the motion detection workflow.

## Requirements

- Python 3.10 or newer recommended
- A working webcam
- Linux-compatible OpenCV camera backend support

Python dependencies:

- `opencv-python==4.12.0.88`
- `numpy==2.3.2`
- `imutils==0.5.4`
- `pygame==2.6.1`

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Theft_Detection_Open_Cv
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Run the motion detection app

```bash
python3 bugler_presence.py
```

Press `q` to close the application window.

### Run the webcam test script

```bash
python3 test.py
```

## How Detection Works

The motion detection pipeline is based on a simple and effective frame differencing approach:

1. A sequence of blurred grayscale frames is stored in memory
2. The oldest and newest frames in the buffer are compared
3. Pixel differences above a threshold are treated as motion candidates
4. Dilation strengthens detected regions
5. Contours smaller than a minimum area are ignored
6. Larger contours are considered valid motion events

This approach is fast and easy to understand, making it a good fit for beginner to intermediate OpenCV projects.

## Configuration

The main detection behavior can be adjusted directly in `bugler_presence.py`:

- `CAMERA_INDEX`: selects the webcam device
- `FRAME_GAP`: number of buffered frames used for comparison
- `MIN_CONTOUR_AREA`: minimum contour area required to count as motion
- `THRESHOLD`: pixel difference threshold for binarization

Tuning these values can help improve performance depending on lighting, camera quality, and scene movement.

## Output

When motion is detected:

- The live feed shows a `BURGLAR DETECTED!` warning
- Bounding boxes are drawn around moving regions
- A timestamped `.jpg` image is saved to `detections/`

## Limitations

- Detection is motion-based, not person-specific
- Sudden lighting changes may trigger false positives
- Camera backend settings are currently optimized for a Linux environment using `cv2.CAP_V4L2`
- Some demo scripts reference absolute local image paths and may not run without adjustment

## Future Improvements

- Add configurable alerts such as sound or email notifications
- Replace motion-only logic with human detection using a deep learning model
- Move hardcoded settings into a config file or CLI arguments
- Add logging and event history
- Add automated tests for non-camera utility logic

## License

Add a license file if you plan to distribute or open-source this project publicly.
