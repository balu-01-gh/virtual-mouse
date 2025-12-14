# Virtual Mouse with Hand Gestures

A Python-based virtual mouse control system using computer vision and hand gesture recognition. Control your computer mouse cursor, clicks, and scrolling using hand movements detected via webcam.

## Features

- **Cursor Movement**: Move cursor by opening your palm and moving your hand
- **Left Click**: Pinch thumb and index finger together
- **Right Click**: Pinch thumb and middle finger together
- **Scrolling**: Use second hand with index and middle fingers close, move up/down to scroll
- **Multi-hand Support**: Separate controls for mouse actions and scrolling
- **Real-time Detection**: Smooth, responsive gesture recognition using MediaPipe
- **Customizable Sensitivity**: Adjustable thresholds for different gesture sensitivities

## Requirements

- Python 3.7+
- Webcam
- Windows/Linux/Mac OS

## Installation

1. Clone the repository:
```bash
git clone https://github.com/balu-01-gh/virtual-mouse.git
cd virtual-mouse
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the virtual mouse:
```bash
python main.py
```

2. A webcam window will open showing your hand tracking.

3. **Gestures:**
   - **Move Cursor**: Open your palm fully (all fingers extended) and move your hand
   - **Left Click**: Bring thumb and index finger close together
   - **Right Click**: Bring thumb and middle finger close together
   - **Scroll**: Use your second hand - bring index and middle fingers close and move them up/down

4. Press 'q' to quit the application.

## Configuration

You can adjust sensitivity settings in `main.py`:

```python
# Sensitivity adjustments
click_threshold = 20      # Distance for click detection
move_threshold = 50       # Minimum distance for cursor movement
scroll_threshold = 30     # Distance for scroll gesture detection
smoothing_factor = 0.5    # Cursor smoothing (0-1, higher = smoother)
```

## Dependencies

- OpenCV: Computer vision and webcam handling
- MediaPipe: Hand tracking and gesture recognition
- PyAutoGUI: Mouse control automation
- NumPy: Numerical computations

## How It Works

1. **Hand Detection**: Uses MediaPipe's hand tracking to detect hand landmarks in real-time
2. **Gesture Recognition**: Analyzes finger positions to identify specific gestures
3. **Palm Detection**: Checks if all fingers are extended for cursor movement
4. **Multi-hand Logic**: Supports separate hands for mouse control and scrolling
5. **Smoothing**: Applies smoothing to cursor movement for better control

## Troubleshooting

- **Cursor not moving**: Ensure good lighting and clear hand visibility
- **Gestures not detected**: Adjust threshold values in the code
- **Performance issues**: Close other applications using the webcam
- **Import errors**: Make sure all dependencies are installed correctly

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve the virtual mouse functionality.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- MediaPipe for hand tracking capabilities
- OpenCV for computer vision
- PyAutoGUI for mouse automation
