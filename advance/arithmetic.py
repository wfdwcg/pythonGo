from PIL import Image
from numpy import  *
from scipy.ndimage import filters

im = array(Image.open('./sample.jpg').convert('L'))
##高斯滤波器
##https://blog.csdn.net/hanging_gardens/article/details/78662949
im2 = filters.gaussian_filter(im, 5)