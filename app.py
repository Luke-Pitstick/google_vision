import cv2 
import time
import io
import os
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/lukepitstick/personal/googlekey/alien-motif-350718-2e1ee73db95e.json'


def takePicture():
    cam = cv2.VideoCapture(0)

    for i in range(3, 0, -1):
        time.sleep(1)
        print(f"Picture will be taken in {i} seconds")

    s, img = cam.read()

    cv2.imwrite('img/works.png', img)

def detectText(path):

    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)
    texts = response.text_annotations
    
    return texts




### prints the objects in the picture ###

 
def detectObjects(path):
    client = vision.ImageAnnotatorClient()

    # Loads the image into memory
    with io.open('img/works.png', 'rb') as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    
    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    return labels
 


vid = cv2.VideoCapture(0)

while(True):
    
    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)
    
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        takePicture()
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

text = detectText('img/works.png')

print('Texts:\n')

try:
    print(text[0].description)
except:
    print('Invalid Picure')
