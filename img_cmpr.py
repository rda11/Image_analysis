import cv2
import webbrowser
import time
from pyzbar.pyzbar import decode
import pathlib

def orb_sim(img1, img2):
    orb = cv2.ORB_create()
    kp_a, desc_a = orb.detectAndCompute(img1, None)
    kp_b, desc_b = orb.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(desc_a, desc_b)
    # Look for similar regions with distance < 50. Goes from 0 to 100 so pick a number between.
    similar_regions = [i for i in matches if i.distance < 20]
    if len(matches) == 0:
        return 0
    return len(similar_regions) / len(matches)

html_content_xx = f"<html> \
                <head> \
                <h1> CYLINDER LINER SELECTION <h1/>  \
                <p> <br> CYLINDER 1: </p> \
                <p> <br> Engraving block image: </p> \
                <p> <img src='C:\\Users\\rajab\\PycharmProjects\\pythonProject\\roicap_imgy.jpg'> </p> \
                <p> <br> Engraving block value is X </p> \
                <p> <br> CYLINDER 2: </p> \
                <p> <br> Engraving block image: </p> \
                <p> <img src='C:\\Users\\rajab\\PycharmProjects\\pythonProject\\roicap_imgy.jpg'> </p> \
                <p> <br> Engraving block value is X </p> \
                <p> <br> QR image: </p> \
                <p> <img src='C:\\Users\\rajab\\PycharmProjects\\pythonProject\\j6qrcopy.jpg'> </p> \
                <p> <br> QR value is 7201126$X3405722$ 4914$23.02.2022$NA$R22B-029Y$NA$J$CYLINDERLINER$KUSALAVA </p> \
                 </head> \
                 </html>"
html_content_xy = f"<html> \
                 <head> \
                <h1> CYLINDER LINER SELECTION <h1/>  \
                <p> <br> CYLINDER 1: </p> \
                <p> <br> Engraving block image: </p> \
                <p> <img src='C:\\Users\\rajab\\PycharmProjects\\pythonProject\\roicap_imgy.jpg'> </p> \
                <p> <br> Engraving block value is X </p> \
                <p> <br> CYLINDER 2: </p> \
                <p> <br> Engraving block image: </p> \
                <p> <img src='C:\\Users\\rajab\\PycharmProjects\\pythonProject\\roicap_imgy.jpg'> </p> \
                <p> <br> Engraving block value is Y </p> \
                <p> <br> QR image: </p> \
                <p> <img src='C:\\Users\\rajab\\PycharmProjects\\pythonProject\\j6qrcopy.jpg'> </p> \
                <p> <br> QR value is 7201126$X3405722$ 4914$23.02.2022$NA$R22B-029Y$NA$J$CYLINDERLINER$KUSALAVA </p> \
                 </head> \
                 </html>"
html_content_yy_B =f"<html> \
                <head> \
                <h1> CYLINDER LINER SELECTION <h1/>  \
                <p> <br> CYLINDER 1: </p> \
                <p> <br> Engraving block image: </p> \
                <p> <img src='C:\\Users\\rajab\\PycharmProjects\\pythonProject\\double_roi_imgy.jpg'> </p> \
                <p> <br> Engraving block value is Y </p> \
                <p> <br> CYLINDER 2: </p> \
                <p> <br> Engraving block image: </p> \
                <p> <img src='C:\\Users\\rajab\\PycharmProjects\\pythonProject\\double_roi2_imgy.jpg'> </p> \
                <p> <br> Engraving block value is Y </p> \
                <p> <br> BLOCK Color code Blue  </p> \
                <p> <br> QR image: </p> \
                <p> <img src='C:\\Users\\rajab\\PycharmProjects\\pythonProject\\j6qrcopy.jpg'> </p> \
                <p> <br> QR value is 7201126$X3405722$ 4914$23.02.2022$NA$R22B-029Y$NA$J$CYLINDERLINER$KUSALAVA </p> \
                 </head> \
                 </html>"
html_content_yy_Y =f"<html> \
                <head> \
                <h1> CYLINDER LINER SELECTION <h1/>  \
                <p> <br> CYLINDER 1: </p> \
                <p> <br> Engraving block image: </p> \
                <p> <img src='C:\\Users\\rajab\\PycharmProjects\\pythonProject\\double_roi_imgy.jpg'> </p> \
                <p> <br> Engraving block value is Y </p> \
                <p> <br> CYLINDER 2: </p> \
                <p> <br> Engraving block image: </p> \
                <p> <img src='C:\\Users\\rajab\\PycharmProjects\\pythonProject\\double_roi2_imgy.jpg'> </p> \
                <p> <br> Engraving block value is Y </p> \
                <p> <br> BLOCK Color code Yellow  </p> \
                <p> <br> QR image: </p> \
                <p> <img src='C:\\Users\\rajab\\PycharmProjects\\pythonProject\\j6qrcopy.jpg'> </p> \
                <p> <br> QR value is 7201126$X3405722$ 4914$23.02.2022$NA$R22B-029Y$NA$J$CYLINDERLINER$KUSALAVA </p> \
                 </head> \
                 </html>"
html_content_yx =f"<html> \
                 <head> \
                <h1> CYLINDER LINER SELECTION <h1/>  \
                <p> <br> CYLINDER 1: </p> \
                <p> <br> Engraving block image: </p> \
                <p> <img src='C:\\Users\\rajab\\PycharmProjects\\pythonProject\\double_roi_imgy.jpg'> </p> \
                <p> <br> Engraving block value is Y </p> \
                <p> <br> CYLINDER 2: </p> \
                <p> <br> Engraving block image: </p> \
                <p> <img src='C:\\Users\\rajab\\PycharmProjects\\pythonProject\\double_roi2_imgy.jpg'> </p> \
                <p> <br> Engraving block value is X </p> \
                <p> <br> QR image: </p> \
                <p> <img src='C:\\Users\\rajab\\PycharmProjects\\pythonProject\\j6qrcopy.jpg'> </p> \
                <p> <br> QR value is 7201126$X3405722$ 4914$23.02.2022$NA$R22B-029Y$NA$J$CYLINDERLINER$KUSALAVA </p> \
                 </head> \
                 </html>"

#QR processing
my_QR = cv2.imread('j6qrcopy.jpg')
im_gray = cv2.cvtColor(my_QR, cv2.COLOR_BGR2GRAY)
thresh_, mask = cv2.threshold(im_gray, 160, 255, cv2.THRESH_BINARY)
mask = ~mask
#QR Decode
decode = decode(mask)
print(decode[0].data.decode("ascii"))
cv2.imshow('qr',mask)

#video processing
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 840)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
for _ in range(10):
    _, frame = cap.read()
frame = cv2.resize(frame, (840, 480))
#frame = cv2.flip(frame, 1)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
roi_cap = gray[20:110,80:200]
roi_cap2 = gray[20:110,280:400]
cv2.imwrite('double_roi_imgy.jpg',roi_cap)
cv2.imwrite('double_roi2_imgy.jpg',roi_cap2)
#show
cv2.imshow('original image',frame)
cv2.imshow('original image1',roi_cap)
cv2.imshow('original image2',roi_cap2)
cv2.waitKey(0)

#pixel point
pixel_point = frame[165,815]
b, g, r = pixel_point
print(pixel_point)

# PRELOADED
imgxo = cv2.imread('ycheck.jpg')
imgyo = cv2.imread('doublecheck_roi_imgy.jpg')
imgzo = cv2.imread('imgzo.PNG')

imgx1 = cv2.imread('ycheck.jpg')
imgy1 = cv2.imread('doublecheck_roi2_imgy.jpg')
imgz1 = cv2.imread('imgzo.PNG')
# check for similarity
orb_similarityx = orb_sim(roi_cap, imgxo)
orb_similarityy = orb_sim(roi_cap, imgyo)
orb_similarityz = orb_sim(roi_cap, imgzo)

orb_similarityx1 = orb_sim(roi_cap2, imgx1)
orb_similarityy1 = orb_sim(roi_cap2, imgy1)
orb_similarityz1 = orb_sim(roi_cap2, imgz1)
# print values
print("Similarity using ORB FOR 1st X is: ", orb_similarityx)
print("Similarity using ORB FOR 1st Y is: ", orb_similarityy)
print("Similarity using ORB FOR 1st Z is: ", orb_similarityz)

print("Similarity using ORB FOR 2nd X is: ", orb_similarityx1)
print("Similarity using ORB FOR 2nd Y is: ", orb_similarityy1)
print("Similarity using ORB FOR 2nd Z is: ", orb_similarityz1)
# compare the greater value
if (orb_similarityx > orb_similarityy and orb_similarityx > orb_similarityz and orb_similarityx1 > orb_similarityy1 and orb_similarityx1 > orb_similarityz1):
         with open("webpage.html", 'w') as html_file:
            html_file.write(html_content_xx)

         time.sleep(2)
         webbrowser.open_new_tab("webpage.html")

if (orb_similarityx > orb_similarityy and orb_similarityx > orb_similarityz and orb_similarityy1 > orb_similarityx1 and orb_similarityy1 > orb_similarityz1):
         with open("webpage.html", 'w') as html_file:
            html_file.write(html_content_xy)

         time.sleep(2)
         webbrowser.open_new_tab("webpage.html")

if (orb_similarityy > orb_similarityx and orb_similarityy > orb_similarityz and orb_similarityy1 > orb_similarityx1 and orb_similarityy1 > orb_similarityz1 and b>g and b>r):
         with open("webpage.html", 'w') as html_file:
            html_file.write(html_content_yy_B)

         time.sleep(2)
         webbrowser.open_new_tab("webpage.html")

if (orb_similarityy > orb_similarityx and orb_similarityy > orb_similarityz and orb_similarityy1 > orb_similarityx1 and orb_similarityy1 > orb_similarityz1 and b<g and b<r):
         with open("webpage.html", 'w') as html_file:
            html_file.write(html_content_yy_Y)

         time.sleep(2)
         webbrowser.open_new_tab("webpage.html")

if (orb_similarityy > orb_similarityx and orb_similarityy > orb_similarityz and orb_similarityx1 > orb_similarityy1 and orb_similarityx1 > orb_similarityz1):
         with open("webpage.html", 'w') as html_file:
            html_file.write(html_content_yx)

         time.sleep(2)
         webbrowser.open_new_tab("webpage.html")
