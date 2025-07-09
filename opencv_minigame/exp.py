import cv2
import random
import time
import numpy as np

score = 0
timer_start = None
life = ["o", "o", "o"]
timer = 5


def start(cap):
    try:
        suc, img = cap.read()
    except Exception:
        print("exception")
    img = cv2.flip(img, 1)
    if "o" not in life:
        cv2.putText(img, f"You're lose ", (img.shape[1] // 4, img.shape[0] // 2), cv2.FONT_HERSHEY_DUPLEX, 4,
                    (0, 0, 0), thickness=3)

    cv2.putText(img, f"Score: {score}", (10, 40), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), thickness=2)
    cv2.putText(img, f"life: {life}", (10, 70), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), thickness=2)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    faces = cv2.CascadeClassifier("faces.xml")
    results = faces.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=6)

    for (x, y, w, h) in results:
        rec = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), thickness=1)
        img = cv2.bitwise_and(img, rec)

    return img, results


class Game_1:

    def __init__(self, cap):
        self.cap = cap

    class Circle:
        circle = None

        def __init__(self, img):
            self.img = img
            self.x = random.randint(0, img.shape[1])
            self.y = random.randint(0, img.shape[0])
            self.rad = 50
            self.draw(self.img)

        def get(self):
            return self.x, self.y

        def draw(self, img):
            cv2.circle(img, (self.x, self.y), self.rad, (0, 0, 224), thickness=5)
            return self.circle

    def is_match(self, object_1, results):
        try:
            px, py = object_1.get()
        except Exception:
            quit("Error")
        for (x, y, w, h) in results:
            return x <= px <= x + w and y <= py <= y + h

    def start_game(self):
        global score
        global life
        global timer
        circle = None
        while True:
            img, results = start(self.cap)

            if "o" in life:
                if circle == None:
                    timer_start = time.time()
                    circle = self.Circle(img)
                if circle is not None and self.is_match(circle, results):
                    score += 1
                    timer *= 0.9
                    circle = None
                if time.time() - timer_start > timer:
                    for i in range(len(life)):
                        if life[i] == "o":
                            life[i] = "X"
                            break
                    circle = None
                try:
                    circle.draw(img)
                except Exception:
                    continue

            cv2.imshow("Result", img)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

class Game_2:

    def __init__(self, cap):
        self.cap = cap

    def start_game(self):
        global score
        global life
        global timer

        while True:
            img, results = start(self.cap)

