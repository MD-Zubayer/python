import cv2


# Image load
image = cv2.imread('images.png')

# display image
cv2.imshow('my image', image)

key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite('seved_image.png', image)
    print('✅ Image Saved as saved_flower.jpg')
elif key == 27:
        print("❌ Exited without saving")

cv2.destroyAllWindows()