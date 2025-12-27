import cv2

class Image:
    def __init__(self, path):
        self.path = path
        self.img = cv2.imread(path)
        assert self.img is not None, "No image found. Need to provide os.path if not in current directory"

    def get_image(self):
        return self.img

def display_image(img: Image):
    cv2.imshow("Image", img)
    cv2.waitKey(0)

def display_image_pixels(img: Image):
    print("Hello World")