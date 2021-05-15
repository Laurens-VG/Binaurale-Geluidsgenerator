import cv2

def calculate_angle(xcenter_frame, xcenter_rectangle):
    angle = (xcenter_rectangle-xcenter_frame)/xcenter_frame
    angle *= 89
    return int(angle)


def calculate_elevation(ycenter_frame, ycenter_rectangle):
    elevation = (ycenter_rectangle-ycenter_frame)/ycenter_frame
    elevation *= -89
    return int(elevation)


def calculate_distance(area_rectangle, area_reference):
    # needs changes!!!
    global distance
    if area_rectangle <= area_reference:
        distance = area_rectangle/area_reference
    else:
        distance = abs(area_rectangle-area_reference)/area_rectangle
        distance *= 2
    distance = distance ** (-1)
    return distance


# def headtracking_camera():
#
#     # whole path for command line run!!!
#     cascPath = "C:\\" + "Users\\" + "reine\PycharmProjects\BinauralSoundGenerator\code\haarcascade_frontalface_default.xml"
#     faceCascade = cv2.CascadeClassifier(cascPath)
#     video_capture = cv2.VideoCapture(0)
#
#     # Check if the webcam is opened correctly
#     if not video_capture.isOpened():
#         raise IOError("Cannot open webcam")
#
#     # Capture frame
#     ret, frame = video_capture.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#
#     # Detect faces in the image
#     faces = faceCascade.detectMultiScale(
#         gray,
#         scaleFactor=1.1,
#         minNeighbors=5,
#         minSize=(30, 30),
#         flags=cv2.CASCADE_SCALE_IMAGE
#     )
#
#     # Get center of frame
#     height = frame.shape[0]
#     width = frame.shape[1]
#     xcenter_frame = int(width/2)
#     ycenter_frame = int(height/2)
#     if len(faces) == 0:
#         angle = 0
#         distance = 1
#         elevation = 0
#     # Draw a rectangle around the faces
#     for (x, y, w, h) in faces:
#         # Get center of rectangle
#         xcenter_rectangle = int(x + w/2)
#         ycenter_rectangle = int(y + h/2)
#         area_rectangle = h*w
#         area_reference = 14400
#
#         angle = calculate_angle(xcenter_frame, xcenter_rectangle)
#         elevation = calculate_elevation(ycenter_frame, ycenter_rectangle)
#         distance = calculate_distance(area_rectangle, area_reference)
#
#         parameters = "angle: " + str(angle)
#         parameters += " elevation: " + str(elevation)
#         parameters += " distance: " + str(distance)
#
#         cv2.putText(frame, parameters, (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
#         cv2.circle(frame, (xcenter_rectangle, ycenter_rectangle), 1, (0, 255, 0), 2)
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#         # Compare with these
#         cv2.circle(frame, (xcenter_frame, ycenter_frame), 1, (0, 0, 255), 2)
#         cv2.rectangle(frame, (xcenter_frame-60, ycenter_frame-60), (xcenter_frame+60, ycenter_frame+60), (0, 0, 255), 2)
#
#     # Display the resulting frame
#     cv2.imshow('Image', frame)
#     video_capture.release()


"""
IMAGE FACE DETECTION
"""
def headtracking_image():
    # Get user supplied values
    # imagePath = "friends.jpg"
    cascPath = "C:\\" + "Users\\" + "steph\PycharmProjects\BinauralSoundGenerator\code\haarcascade_frontalface_default.xml"

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    # frame = cv2.imread(imagePath)
    # Capture frame
    image_capture = cv2.VideoCapture(0)
    ret, frame = image_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    if len(faces) == 0:
        angle = 0
        distance = 1
        elevation = 0

    height = frame.shape[0]
    width = frame.shape[1]
    xcenter_frame = int(width / 2)
    ycenter_frame = int(height / 2)

    for (x, y, w, h) in faces:
        # Get center of rectangle
        xcenter_rectangle = int(x + w / 2)
        ycenter_rectangle = int(y + h / 2)
        area_rectangle = h * w
        area_reference = 14400

        angle = calculate_angle(xcenter_frame, xcenter_rectangle)
        elevation = calculate_elevation(ycenter_frame, ycenter_rectangle)
        distance = calculate_distance(area_rectangle, area_reference)

        parameters = "angle: " + str(angle)
        parameters += " elevation: " + str(elevation)
        parameters += " distance: " + str(distance)

        cv2.putText(frame, parameters, (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
        cv2.circle(frame, (xcenter_rectangle, ycenter_rectangle), 1, (0, 255, 0), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Compare with these
        cv2.circle(frame, (xcenter_frame, ycenter_frame), 1, (0, 0, 255), 2)
        cv2.rectangle(frame, (xcenter_frame - 60, ycenter_frame - 60), (xcenter_frame + 60, ycenter_frame + 60),(0, 0, 255), 2)
    cv2.imshow("Faces parameters", frame)
    cv2.waitKey(1)
    image_capture.release()

    return distance, angle, elevation


if __name__ == "__main__":
    headtracking_image()

