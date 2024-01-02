import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

modelnsfw = load_model('nsfw-mini.h5')

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    squareframe=cv2.resize(frame, (224,224))
    test_image = cv2.cvtColor(squareframe, cv2.COLOR_BGR2RGB)
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    test_image=test_image/255.0
    nsfwresult = (modelnsfw.predict(test_image, batch_size=1))[0][0]
    thereply='{percent:.0%}'.format(percent=(nsfwresult))+" NSFW"
    frame=cv2.resize(frame, (1024, 780))
    cv2.putText(frame, thereply, (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
