import exp
import cv2

cap = cv2.VideoCapture(0)

cap.set(3, 1920)
cap.set(4, 1080)

game = exp.Game_1(cap)
game.start_game()