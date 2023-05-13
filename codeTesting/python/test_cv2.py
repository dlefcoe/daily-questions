import cv2

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    cv2.imshow('image', img)
    cv2.waitKey(1)

    # Press Q on keyboard to quit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break


# Release the video capture object and close the window
cap.release()
cv2.destroyAllWindows()
