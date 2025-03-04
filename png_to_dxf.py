# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 12:32:21 2025

@author: HP
"""

import ezdxf
import numpy as np
from PIL import Image, ImageFilter
import cv2


def png_to_dxf(input_png, output_dxf, scale_microns=1.0):
    # Load image and convert to grayscale
    img = Image.open(input_png).convert("L")
    img = img.filter(ImageFilter.FIND_EDGES)  # Detect edges
    img = np.array(img)

    # Convert image to binary (black & white)
    _, binary = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a new DXF document
    doc = ezdxf.new()
    msp = doc.modelspace()

    # Process contours and add to DXF
    for contour in contours:
        points = [(p[0][0] * scale_microns, -p[0][1] * scale_microns) for p in contour]
        if len(points) > 1:
            msp.add_lwpolyline(points, close=True)

    # Save DXF file
    doc.saveas(output_dxf)
    print(f"DXF file saved: {output_dxf}")


# Example usage
input_png = "C:/Users/HP/Desktop/wettability coating UV trearment/program to create dxf/UB.png"  # Replace with your image path
output_dxf = "UB.dxf"
scale_microns = 0.01  # Adjust scale factor for microns
png_to_dxf(input_png, output_dxf, scale_microns)
