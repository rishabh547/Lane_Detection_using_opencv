# Lane_Detection_using_opencv
In this project ,  Car lanes are detected on a sample road video &amp;  image  by using opencv_techniques and concepts,
it is done in 3 parts.
### Concepts used :
##### 1 Grayscaling Images (Easier to apply Blur and edge detection on grayscaled image)
##### 2 Gaussian Blur (to reduce video & image noise)
##### 3 Canny edge Detection (to detect wide range of edges using inbuilt multi-stage algorithm)
##### 4 Region of interest & Masking (To mask out the region that wasn't concerned with the road lanes)
##### 5 Hough line transform method (To draw lines on lanes by detecting them based on arguments provided)
##### 

## First Step: Determining region of interest on a particular image frame
![Figure_1](https://user-images.githubusercontent.com/59617133/120296792-1b3a3c00-c2e6-11eb-9b1d-c415fdcf2d16.png)

## Second Step : Identifying lanes on the cropped image obtained
![Figure_2](https://user-images.githubusercontent.com/59617133/120297089-63f1f500-c2e6-11eb-9005-3938fc6854ee.png)

## Finally : Testing Lane detection on a Video Sample.

https://user-images.githubusercontent.com/59617133/120297873-2772c900-c2e7-11eb-82fe-dbda2b2594b4.mp4

