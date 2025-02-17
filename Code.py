import cv2
import os

# Load Image
img = cv2.imread("imagepic.jpg")  # Replace with your image path
if img is None:
    raise ValueError("Error: Image not loaded. Check the file path and format.")

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

rows, cols, _ = img.shape
n, m, z = 0, 0, 0

# Encrypt Message
for i in range(len(msg)):
    img[n % rows, m % cols, z] = d[msg[i]]
    n += 1
    m += 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Open the encrypted image (Windows only)

# Decrypt Message
message = ""
n, m, z = 0, 0, 0

pas = input("Enter passcode for Decryption: ")
if password == pas:
    for i in range(len(msg)):
        message += c[img[n % rows, m % cols, z]]
        n += 1
        m += 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT AUTHORIZED!")
