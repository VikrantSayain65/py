import cv2
import matplotlib.pyplot as plt

image = cv2.imread('yuji_itadori.jpg')
h, w = image.shape[:2]
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

r1 = ((20, 20), (150, 150))
r2 = ((w - 220, h - 220), (w - 20, h - 20))
cv2.rectangle(image, r1[0], r1[1], (0, 255, 0), 3)
cv2.rectangle(image, r2[0], r2[1], (255, 0, 255), 3)

c1 = ((r1[0][0] + r1[1][0]) // 2, (r1[0][1] + r1[1][1]) // 2)
c2 = ((r2[0][0] + r2[1][0]) // 2, (r2[0][1] + r2[1][1]) // 2)
cv2.circle(image, c1, 15, (0, 255, 0), -1)
cv2.circle(image, c2, 15, (255, 0, 255), -1)

cv2.line(image, c1, c2, (0, 0, 255), 2)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'Region 1', (r1[0][0], r1[0][1] - 10), font, 0.7, (255, 255, 255), 2)
cv2.putText(image, 'Region 2', (r2[0][0], r2[0][1] - 10), font, 0.7, (255, 255, 255), 2)
cv2.putText(image, 'Center 1', (c1[0] - 40, c1[1] + 40), font, 0.7, (255, 255, 0), 1)
cv2.putText(image, 'Center 2', (c2[0] - 40, c2[1] + 40), font, 0.7, (255, 255, 0), 1)

arrow_s = (20, h - 50)
arrow_e = (w - 20, h - 50)
cv2.arrowedLine(image, arrow_s, arrow_e, (255, 255, 0), 3, tipLength=0.05)
cv2.arrowedLine(image, arrow_e, arrow_s, (255, 255, 0), 3, tipLength=0.05)

cv2.putText(image, f'Width: {w}px', (w // 2 - 70, h - 65), font, 0.7, (255, 255, 255), 2)

plt.imshow(image)
plt.title("Annotated Image")
plt.axis('off')
plt.show()
