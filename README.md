# background_remover

A simple desktop app to remove the background from images using `rembg`, with a graphical interface for file selection or drag-and-drop. The processed image is saved in the **same folder** as the original file, named `output.png`, `output2.png`, etc.

## Requirements

* Python 3.8 or higher

## Installation

Install the required libraries:

```bash
pip install rembg pillow tkinterdnd2 onnxruntime
```

If you're on Linux and get errors related to Tkinter, install it with:

* **Debian/Ubuntu:**

  ```bash
  sudo apt install python3-tk
  ```

* **Arch Linux:**

  ```bash
  sudo pacman -S tk
  ```

## How to Run

Run the application:

```bash
python app.py
```

A window will open. You can:

* Click **"Browse Image"** to select a file
* Or **drag and drop** an image into the highlighted area

The image with the background removed will be saved in the same folder as the original image.

## Supported Formats

* PNG
* JPG / JPEG
* WEBP
* BMP

---

Let me know if you want this exported as a `README.md` file.
