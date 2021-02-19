"""."""
import numpy as np
import cv2

from typing import Tuple, Union  # , Any, NewType, TypeVar


def set_res(cap: cv2.VideoCapture, resolution: Union[int, str]) -> str:
    """."""
    if resolution in [480, "480", "480p"]:
        cap.set(3, 640)
        cap.set(4, 480)
    elif resolution in [1080, "1080", "1080p"]:
        cap.set(3, 1920)
        cap.set(4, 1080)
    elif resolution in [720, "720", "720p"]:
        cap.set(3, 1920)
        cap.set(4, 1080)
    else:
        resolution = 720
        set_res(cap, resolution)
    return str(resolution)

cap = cv2.VideoCapture(0)

set_res(cap, 480)

while(cap.isOpened()):
    frame_out: Tuple[bool, np.ndarray] = cap.read()
    # (ret, frame) = frame_out  ## loses typings :/
    ret = frame_out[0]
    frame = frame_out[1]

    if ret is True:
        # Our operations on the frame come here
        gray: np.ndarray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        vflipped: np.ndarray = cv2.flip(frame, 0)  # 0=vert, 1=horiz, -1=both       # Display the resulting frame
        hflipped: np.ndarray = cv2.flip(frame, 1)  # 0=vert, 1=horiz, -1=both       # Display the resulting frame


        cv2.imshow('frame', frame)
        # cv2.imshow('frame1', gray)
        # cv2.imshow('frame2', vflipped)
        # cv2.imshow('frame2', hflipped)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
