# Color Detection with OpenCV

This project is a real-time color detection application using Python, OpenCV, and Pillow. It captures video from your webcam and detects specific colors (Yellow, Blue, Green) in the frame, drawing bounding boxes around detected areas.

## Features

- **Real-time Detection:** Processes video feed from the default webcam.
- **Multiple Color Support:** Detects Yellow, Blue, and Green objects simultaneously.
- **Visual Feedback:** Draws a bounding box and labels the detected object with its color name.
- **HSV Color Space:** Uses HSV (Hue, Saturation, Value) color space for more robust color detection compared to RGB.

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- NumPy (`numpy`)
- Pillow (`Pillow`)

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/AntKss07/color-detection-model.git
    cd color-detection-model
    ```

2.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the main script to start the application:

```bash
python main.py
```

- A window will open showing the webcam feed.
- Hold up objects that are Yellow, Blue, or Green.
- The application will draw a rectangle around the detected color and label it.
- Press **'q'** to quit the application.

## Code Structure

- `main.py`: The main entry point. Initializes the camera, processes frames, and handles the main loop.
- `util.py`: Contains utility functions, specifically `get_limits`, which calculates the lower and upper HSV limits for a given BGR color.
