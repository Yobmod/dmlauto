import numpy as np
import cv2
from typing import Tuple, Any, NewType, TypeVar

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    frame_out: Tuple[bool, np.ndarray] = cap.read()
    # (ret, frame) = frame_out  ## loses typings :/
    ret = frame_out[0]
    frame = frame_out[1]

    if ret is True:
        # Our operations on the frame come here
        gray: np.ndarray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        vflipped: np.ndarray = cv2.flip(frame, 0)  # 0=vert, 1=horiz, -1=both       # Display the resulting frame
        hflipped: np.ndarray = cv2.flip(frame, 1)

        # cv2.imshow('frame', frame)
        # cv2.imshow('frame1', gray)
        # cv2.imshow('frame2', vflipped)
        cv2.imshow('frame2', hflipped)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
