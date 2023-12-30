import torch
import cv2
import pandas as pd
import os


def main(imageURL):
    modalResult = loadModal(imageURL)
    modalResult.show()
    df = modalResult.pandas().xyxy[0]
  #  print(df)
    objectCrop(imageURL,df)


def loadModal(imageURL):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', _verbose=False)
    image = cv2.imread(imageURL)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return model(image)

def objectCrop(imagePath, df, outputDir='crop'):
    os.makedirs(outputDir, exist_ok=True)
    preCroppedImg = cv2.imread(imagePath)

    row = pd.DataFrame(df).nlargest(1, 'confidence').iloc[0]

    #print(row)

    xmin, ymin, xmax, ymax = map(int, [row['xmin'], row['ymin'], row['xmax'], row['ymax']])
    className = row['name']
    #print(xmin, ymin, xmax, ymax)
    croppedObject = preCroppedImg[ymin:ymax, xmin:xmax]

    outputPath = os.path.join(outputDir, f'{className}.png')
    cv2.imwrite(outputPath, croppedObject)

    cv2.imshow(f"{className}", croppedObject)

if __name__ == '__main__':
    #image = 'media/maxresdefault.jpg'
    image = 'media/my-lawn.jpg'
    main(image)


