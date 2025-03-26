
import imageio.v3 as iio

filenames = ['frame-01.png','frame-02.png','frame-03.png','frame-04.png','frame-05.png','frame-06.png']
images =[]
for filename in filenames:
    images.append(iio.imread("./images/"+filename))

iio.imwrite('totaro.gif', images, duration = 500, loop = 0)