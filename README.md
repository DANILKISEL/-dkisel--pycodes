# Drawing Application

This project is a simple drawing application built using Python and Pygame. Users can draw on a canvas, change colors using keyboard shortcuts, and save their drawings. The application also supports fullscreen mode and an eraser tool.

## Project Structure

The project consists of the following files:

- `colors.py`: Contains functions to load a color map from a JSON file and return a dictionary mapping keys to colors.
- `drawer.py`: Implements the main drawing application, including setup, event handling, and drawing logic.
- `pygame_key_test.py`: A simple script to test and print key presses using Pygame.
- `colors_map.json`: A JSON file that defines a mapping of keys to RGB color values.
- `colors_map.md`: A markdown file that provides a visual representation of the color mapping.

## Installation

To run this application, ensure you have Python and Pygame installed. You can install Pygame using pip:

```bash
pip install pygame

```
Usage
Run the Application: Execute the drawer.py file to start the drawing application.

```bash
python drawer.py

```
Drawing: Click and drag the mouse to draw on the canvas.

## Keyboard Shortcuts:

Escape: Quit the application.
Z: Clear the canvas.
S: Save the drawing. You'll be prompted to enter a filename.
E: Toggle the eraser tool (black color).
F12: Toggle fullscreen mode.
Function Keys (F1-F11): Change colors based on the colors_map.json configuration.
Number Keys (1-0): Select additional colors.

## Color Mapping
| Key | Color Name      |
|-----|-----------------|
| F1  | Red             |
| F2  | Green           |
| F3  | Blue            |
| F4  | Orange          |
| F5  | Yellow          |
| F6  | Pink            |
| F7  | Purple          |
| F8  | Cyan            |
| F9  | White           |
| F10 | Gray            |
| F11 | Black           |
| 1   | Hot Pink        |
| 2   | Light Blue      |
| 3   | Light Green     |
| 4   | Plum            |
| 5   | Khaki           |
| 6   | Light Sky Blue  |
| 7   | Light Coral     |
| 8   | Cornflower Blue |
| 9   | Bisque          |
| 0   | Light Cyan      |

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements
Pygame for the game development library.