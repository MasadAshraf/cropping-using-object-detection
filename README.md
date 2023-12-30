# Object Detection and Image Cropping using YOLOv5

## Author
Muhammad Masad Ashraf

## Assignment Information
**Assignment Name:** Object Detection using YOLO and Cropping Image  
**Course:** PIAIC (Pakistan Institute of Artificial Intelligence and Computing)

## Description
This code utilizes the YOLOv5 model for object detection and cropping images based on the detected objects. The script takes an image URL as input, loads the YOLOv5 model, performs object detection, and then crops the image based on the detected objects.

## Usage
To use the script, run it with the desired image URL as follows:
```bash
python main.py
```

## Requirements

Ensure you have the following prerequisites installed before running the script:

- **Python 3**
- **PyTorch**
- **OpenCV**
- **Pandas**
- **YOLOv5** (automatically loaded from ultralytics/yolov5 repository)

### Installation

You can install the required packages using the following commands:

```bash
pip install torch torchvision
pip install opencv-python
pip install pandas
```

### Instructions

- **Install the required packages using the provided installation commands.**
- **Run the script with your desired image URL.**

```bash
if __name__ == '__main__':
    image = 'media/my-lawn.jpg'
    main(image)
```
This will load the YOLOv5 model, perform object detection on the given image, and save cropped images of the detected objects.