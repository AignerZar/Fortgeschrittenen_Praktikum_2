import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Initial settings
image_path = '/Users/zarahaigner/Documents/Physik_Master_1/FP_2/Cherenkov_Effect/Data_Exercise_1/tek00010.png'  # path to the screenshot, modify for each screenshot
ns_per_div = 4.0        # can be seen in the oscilloscope screenshot     
divisions = 10          # can be seen in the oscilloscope screenshot
sigma_pixel = 1.0          

# converting image into an array
img = mpimg.imread(image_path)
fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(img)
ax.set_title("Click on the peaks of channel 1 and channel 2 one after the other, be as precise as possible")
plt.axis("off")

# person needs to click onto the two peaks, positions of them gets stored
points = plt.ginput(2, timeout=0)  
plt.close()


x1, y1 = points[0]  #first peak
x2, y2 = points[1]  #second peak

"""
Time difference------------------------------------------------------------
"""
width_in_pixels = img.shape[1]
ns_per_pixel = (ns_per_div * divisions) / width_in_pixels   # computing the ns per pixel
delta_t_ns = abs(x2 - x1) * ns_per_pixel    #computing the difference 

sigma_delta_t = np.sqrt(2) * sigma_pixel * ns_per_pixel     # computing the error, sigma_x1 = sigma_x2 = 1 Pixel, using gaussian error propagation

print(f"Pixel-Positions: x1 = {x1:.1f} +- {sigma_pixel:.1f}, x2 = {x2:.1f} +- {sigma_pixel:.1f}")
print(f"Time resolution: {ns_per_pixel:.4f} ns/Pixel")
print(f" Zeitdifference delta t = {delta_t_ns:.3f} +- {sigma_delta_t:.3f} ns")


