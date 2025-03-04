# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 22:22:15 2024

@author: Lidia Lozano Martín

Programa para leer y plotear archivos DXF para imprimir diseños con el 
sistema del laser pulsado UV

Unidades en mm
"""
# %%   Esta celda es la que funciona

import ezdxf
from ezdxf.addons.drawing import Frontend, RenderContext, svg, layout, config, pymupdf, dxf
import io
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#  # doc = ezdxf.readfile("C:/Users/HP/Desktop/copia_ordenador_planta_4/square_10um_2version.dxf")


def one_line():  # diseño de espiral cuadrada
    doc = ezdxf.new()  # crea el doc
    msp = doc.modelspace()  # crea el espacio
    x0, y0, x1, y1 = 0, 0, 0.6, 0.6 # coordenadas origen, va a tener 1mm de diámetro
    # separación entre líneas, aprox 1um (0.001 mm) que se corresponde con el spot del laser
    step = 0.001
    start = (x0, y0)
    end = (x1, y0)
     # 500 es el número de vueltas, en total 2*500*0.001= 1 mm tamaño
    msp.add_lwpolyline( [start, end] )
    return doc



def squared_spiral():  # diseño de espiral cuadrada
    doc = ezdxf.new()  # crea el doc
    msp = doc.modelspace()  # crea el espacio
    x0, y0, x1, y1 = 0, 0, 1, 1  # coordenadas origen, va a tener 1mm de diámetro
    # separación entre líneas, aprox 1um (0.001 mm) que se corresponde con el spot del laser
    step = 0.001
    start = (x0, y0)
    end = (x0 + step, y0)
    for color in range(1, 3):  # 500 es el número de vueltas, en total 2*500*0.001= 1 mm tamaño
        msp.add_lwpolyline(
            [start, (x0, y1), (x1, y1), (x1, y0),
             end], dxfattribs={"color": color}
        )
        x0 += step
        x1 -= step
        y0 += step
        y1 -= step
        start = end
        end = (x0 + step, y0)
    return doc


def triangle():  # diseño de espiral cuadrada
    doc = ezdxf.new()  # crea el doc
    msp = doc.modelspace()  # crea el espacio
    x0, y0, x1, y1, x2 = 0.4, 0, 0, 0.346, 0.2
    # x0, y0, x1, y1, x2 = 1, 0, 0, 1.73/2, 0.5 #coordenadas origen, va a tener 1mm de diámetro
    # separación entre líneas, aprox 1um (0.001 mm) que se corresponde con el spot del laser
    step = 0.001
    start = (x0, y0)
    end = (x0, y0 + step)
    for color in range(1, 3):  # 500 es el número de vueltas, en total 2*500*0.001= 1 mm tamaño
        msp.add_lwpolyline(
            [start, (x1, y0), (x2, y1)], dxfattribs={"color": color}
        )
        start = x0, y0 + step
        x0 += step
        x1 += step
        y0 += step
        y1 -= step

    return doc


def open_squared_spiral():  # diseño de espiral cuadrada
    doc = ezdxf.new()  # crea el doc
    msp = doc.modelspace()  # crea el espacio
    x0, y0, x1, y1 = 0, 0, 0.4, 0.4  # coordenadas origen, va a tener 1mm de diámetro
    # separación entre líneas, aprox 1um (0.001 mm) que se corresponde con el spot del laser
    step = 0.001
    start = (x0, y0)

    for color in range(1, 2):  # 500 es el número de vueltas, en total 2*500*0.001= 1 mm tamaño
        msp.add_lwpolyline(
            [start, (x0, y1), (x1, y1), (x1, y0)], dxfattribs={"color": color}
        )
        start = (x0+step, y0)
        x0 += step
        x1 -= step
        y0 += step
        y1 -= step

        end = (x0 + step, y0)
    return doc

def paralel_lines_backandfor(): #diseño de líneas paralelas
    doc = ezdxf.new()
    msp = doc.modelspace()
    x0, y0, x1= 0, 0, 1
    step= 0.001

    for color in range(1, 500):
        msp.add_lwpolyline(
            [(x0, y0), (x1, y0)], dxfattribs={"color": color}
        )
        msp.add_lwpolyline(
            [(x1, y0  + step), (x0, y0+ step)], dxfattribs={"color": color}
        )

        y0 += 2*step
    return doc

def paralel_lines_samedirection():
    doc = ezdxf.new()
    msp = doc.modelspace()
    x0, y0, x1= 0, 0, 1

    for color in range(1, 100):
        msp.add_lwpolyline(
            [(x0, y0), (x1, y0)], dxfattribs={"color": color}
        )

        y0 +=0.001

    return doc


def array_squares_op():
    doc = ezdxf.new()
    msp = doc.modelspace()
    
    # step = 0.1 # separacion de 100 um entre puntos y/o lineas
    # base_size = 5 # 500 um / 100 um, mayor densidad de puntos para conseguir el mismo tamaño
    
    # step = 0.05 # separacion de 50 um entre puntos y/o lineas
    # base_size = 10 # 1000 um / 50 um, lo mismo que 1 mm/0.05 mm; tamaño total entre la separación = numero de lineas(loops), Dividido entre 2 porque cada loop es ida y vuelta
    
    # step = 0.025 # separacion de 25 um entre puntos y/o lineas
    # base_size = 20 # 2000 um / 25 um, mayor densidad de puntos para conseguir el mismo tamaño
    
    # step = 0.02 # separacion de 20 um entre puntos y/o lineas
    # base_size = 25 # 2500 um / 20 um, mayor densidad de puntos para conseguir el mismo tamaño
    
    
    # step = 0.01 # separacion de 10 um entre puntos y/o lineas
    # base_size = 50 # 5000 um / 50 um, mayor densidad de puntos para conseguir el mismo tamaño
    
    
    
    # scale_factors = [1, 0.7, 0.5, 0.3, 0.1] #tamaño de los cuadrados en mm
    scale_factors = [1] #tamaño de los cuadrados en mm
    
    x_start = 0
     
    for scale in scale_factors:
        square_width = scale
        
        x0, x1 = x_start, x_start + square_width
        y0 = 0
        loops = int(base_size * scale) # tamaño del cuadrado por el numero de lineas
        print(2*loops)
        for color in range(0, loops):
            msp.add_lwpolyline([(x0, y0), (x1, y0)], dxfattribs={"color": color})
            msp.add_lwpolyline([(x1, y0 + step), (x0, y0 + step)], dxfattribs={"color": color})
            y0 += 2 * step
            
        
        # Update x_start for the next square
        x_start = x1 + 1
       
    
    return doc

def export(doc):  # crea el documento en formato dxf
    export_doc = ezdxf.new()
    msp = doc.modelspace()
    # 1. create the render context
    context = RenderContext(doc)
    # 2. create the backend
    backend = dxf.DXFBackend(export_doc.modelspace())
    # 3. create the frontend
    frontend = Frontend(context, backend)
    # 4. draw the modelspace
    frontend.draw_layout(msp)
    # 5. save or return DXF document
    # export_doc.saveas(
    #     "C:/Users/HP/Desktop/wettability coating UV trearment/program to create dxf/1_square1mmx1mm_sep20um.dxf")
    
    # exporta el archivo en png para visualizar la imagen
    # 2. create the backend
    backend = pymupdf.PyMuPdfBackend()
    # create a new configuration for a white background and and a black foreground color
    cfg = config.Configuration(
        background_policy=config.BackgroundPolicy.WHITE,
        color_policy=config.ColorPolicy.COLOR,
    )
    # 3. create the frontend
    frontend = Frontend(context, backend, config=cfg)
    # 4. draw the modelspace
    frontend.draw_layout(msp)
    # 5. create an A4 page layout, not required for all backends
    page = layout.Page(210, 297, layout.Units.mm,
                        margins=layout.Margins.all(20))  
    # 6. get the PNG rendering as bytes
    png_bytes = backend.get_pixmap_bytes(page, fmt="png", dpi=96)
    # 7. Save png image 
    # with open("C:/Users/HP/Desktop/wettability coating UV trearment/program to create dxf/1_square_sep50um.png", "wb") as fp:
    #     fp.write(png_bytes)
    
    # Convert PNG bytes to an image and display
    image_stream = io.BytesIO(png_bytes)  # Convert bytes to a file-like object
    image = mpimg.imread(image_stream, format='png')  # Read the image
    
    plt.imshow(image)  # Display the image
    # plt.axis("off")  # Hide axes
    # plt.show()  # Show the plot
      
if __name__ == "__main__":
    export(array_squares_op())
    
    # export_dark_bg(example_doc())
    # export_png(array_squares_op())


# def array_squares():
#     doc = ezdxf.new()
#     msp = doc.modelspace()
    
#     #square 1
#     x0, y0, x1 = 0, 0, 1
    
#     step= 0.001
#     end=500  
#     for color in range(1, end):
#         msp.add_lwpolyline(
#             [(x0, y0), (x1, y0)], dxfattribs={"color": color}
#         )
#         msp.add_lwpolyline(
#             [(x1, y0  + step), (x0, y0+ step)], dxfattribs={"color": color}
#         )

#         y0 += 2*step
        
#     #square 2
#     x2, x3 = x1+ 1, x1+ 1+ x1*0.7
#     y0=0
#     end=int(500*0.7)
#     for color in range(1, end):
#         msp.add_lwpolyline(
#             [(x2, y0), (x3, y0)], dxfattribs={"color": color}
#         )
#         msp.add_lwpolyline(
#             [(x3, y0  + step), (x2, y0+ step)], dxfattribs={"color": color}
#         )

#         y0 += 2*step
        
#     #square 3
#     y0=0
#     x4, x5 = x3+ 1, x3+ 1+ x1*0.5
#     end=int(500*0.5)
    
#     for color in range(1, end):
#         msp.add_lwpolyline(
#             [(x4, y0), (x5, y0)], dxfattribs={"color": color}
#         )
#         msp.add_lwpolyline(
#             [(x5, y0  + step), (x4, y0+ step)], dxfattribs={"color": color}
#         )

#         y0 += 2*step
        
        
#     #square 4
#     y0=0
#     x6, x7 = x5+ 1, x5+ 1+ x1*0.3
#     end=int(500*0.3)
#     for color in range(1, end):
#         msp.add_lwpolyline(
#             [(x6, y0), (x7, y0)], dxfattribs={"color": color}
#         )
#         msp.add_lwpolyline(
#             [(x7, y0  + step), (x6, y0+ step)], dxfattribs={"color": color}
#         )

#         y0 += 2*step
        
        
#     #square 5
#     y0=0
#     x8, x9 = x7+ 1, x7+ 1+ x1*0.1
#     end=int(500*0.1)
#     for color in range(1, end):
#         msp.add_lwpolyline(
#             [(x8, y0), (x9, y0)], dxfattribs={"color": color}
#         )
#         msp.add_lwpolyline(
#             [(x9, y0  + step), (x8, y0+ step)], dxfattribs={"color": color}
#         )

#         y0 += 2*step
#     return doc




# def export_png(doc):  # exporta el archivo en png para visualizar la imagen
#     msp = doc.modelspace()
#     # 1. create the render context
#     context = RenderContext(doc)
#     # 2. create the backend
#     #backend = svg.SVGBackend()
#     backend = pymupdf.PyMuPdfBackend()
#     # create a new configuration for a white background and and a black foreground color
#     cfg = config.Configuration(
#         background_policy=config.BackgroundPolicy.WHITE,
#         color_policy=config.ColorPolicy.COLOR,
#     )
#     # 3. create the frontend
#     frontend = Frontend(context, backend, config=cfg)
#     # 4. draw the modelspace
#     frontend.draw_layout(msp)
#     # 5. create an A4 page layout, not required for all backends
#     page = layout.Page(210, 297, layout.Units.mm,
#                         margins=layout.Margins.all(20))
#     # # 6. get the SVG rendering as string - this step is backend dependent
#     #svg_string = backend.get_string(page)
#     # 6. get the PNG rendering as bytes
#     png_bytes = backend.get_pixmap_bytes(page, fmt="png", dpi=96)
#     with open("C:/Users/HP/Desktop/wettability coating UV trearment/program to create dxf/1_square_sep20um.png", "wb") as fp:
#         fp.write(png_bytes)
#     # with open("output.svg", "wt", encoding="utf8") as fp: #lo crea en formato SVG
#     #     fp.write(svg_string)


# def export_dark_bg(doc): #lo exporta con el fondo negro
#     msp = doc.modelspace()
#     # 1. create the render context
#     context = RenderContext(doc)
#     # 2. create the backend
#     backend = pymupdf.PyMuPdfBackend()
#     # 3. create the frontend
#     frontend = Frontend(context, backend)
#     # 4. draw the modelspace
#     frontend.draw_layout(msp)
#     # 5. create an A4 page layout

#     page = layout.Page(10.5, 15, layout.Units.mm, margins=layout.Margins.all(2))
#     # page = layout.Page(0, 0, layout.Units.mm, margins=layout.Margins.all(2))

#     # 6. get the PDF rendering as bytes
#     pdf_bytes = backend.get_pdf_bytes(page)
#     with open("2square.pdf", "wb") as fp:
#         fp.write(pdf_bytes)



# def export_png(doc):
#     msp = doc.modelspace()
#     # 1. create the render context
#     context = RenderContext(doc)
#     # 2. create the backend
#     #backend = svg.SVGBackend()
#     backend = pymupdf.PyMuPdfBackend()
#     # create a new configuration for a white background and and a black foreground color
#     cfg = config.Configuration(
#         background_policy=config.BackgroundPolicy.WHITE,
#         color_policy=config.ColorPolicy.COLOR,
#     )
#     # 3. create the frontend
#     frontend = Frontend(context, backend, config=cfg)
#     # 4. draw the modelspace
#     frontend.draw_layout(msp)
#     # 5. create an A4 page layout, not required for all backends
#     page = layout.Page(210, 297, layout.Units.mm, margins=layout.Margins.all(20))
#     # # 6. get the SVG rendering as string - this step is backend dependent
#     #svg_string = backend.get_string(page)
#     # 6. get the PNG rendering as bytes
#     png_bytes = backend.get_pixmap_bytes(page, fmt="png", dpi=96)
#     with open("C:/Users/HP/Desktop/wettability coating UV trearment/program to create dxf/400umline.png", "wb") as fp:
#         fp.write(png_bytes)
#     # with open("output.svg", "wt", encoding="utf8") as fp:
#     #     fp.write(svg_string)
# def export(doc):
#     export_doc = ezdxf.new()
#     msp = doc.modelspace()
#     # 1. create the render context
#     context = RenderContext(doc)
#     # 2. create the backend
#     backend = dxf.DXFBackend(export_doc.modelspace())
#     # 3. create the frontend
#     frontend = Frontend(context, backend)
#     # 4. draw the modelspace
#     frontend.draw_layout(msp)
#     # 5. save or return DXF document
#     export_doc.saveas("C:/Users/HP/Desktop/wettability coating UV trearment/program to create dxf/400umline.dxf")

# if __name__ == "__main__":
#     export(paralel_lines())
#     # export_dark_bg(example_doc())
#     export_png(paralel_lines())


# %%
# #!/usr/bin/env python3

# __version__ = '1.0.0' # Major.Minor.Patch

# import ezdxf
# import numpy as np  # Import numpy for calculations
# import matplotlib.pyplot as plt
# from matplotlib.patches import Circle, Polygon, Arc

# import sys,os,copy
# from PIL import Image, ImageDraw
# #%%
# doc = ezdxf.readfile("C:/Users/HP/Desktop/copia_ordenador_planta_4/square_10um_2version.dxf")
# #doc = ezdxf.readfile("square_10um_2version.dxf")
# # doc2 = ezdxf.new()
# # file_path = "C:/Users/HP/Desktop/copia_ordenador_planta_4/square_10um_2version.dxf"
# # doc2.saveas(file_path)
# # print(doc2)

# #%%
# def dxf_to_png(file, output_image, image_format='PNG'):
#     file_path = "C:/Users/HP/Desktop/copia_ordenador_planta_4/square_10um_2version.dxf"

#     doc = ezdxf.readfile(file)
#     msp = doc.modelspace()

#     fig = plt.Figure()
#     plt.FigureCanvasAgg(fig)
#     ax = fig.add_subplot(111)

#     for entity in msp.query('LINE,CIRCLE,ARC,LWPOLYLINE'):
#         entity.render(ax)

#     fig.savefig(output_image, format=image_format)

# output_image_file= 'output_1.png'
# dxf_to_png(doc, output_image_file, image_format='PNG')
# #%%
# import os
# print(os.path.exists(doc))
# #%%
# def main():
#     # if len(sys.argv) < 3:
#     #     print("Usage: {} input.dxf output.png".format(sys.argv[0]))
#     #     sys.exit(1)

#     # infilename = sys.argv[1]
#     # outfilename = sys.argv[2]

#     # if os.path.exists(outfilename):
#     #     sys.exit("Output file {} exists".format(outfilename))


#     # Read the DXF file
#     #doc = ezdxf.readfile('E:\square_10um_2version.dxf')
#     msp = doc.modelspace()

#     # Prepare a matplotlib figure
#     fig, ax = plt.subplots()
#     ax.set_aspect('equal')

#     # Iterate through entities in the model space
#     for entity in msp:
#         if entity.dxftype() == 'LINE':
#             draw_line(ax, entity.dxf.start, entity.dxf.end)
#         elif entity.dxftype() == 'CIRCLE':
#             draw_circle(ax, (-entity.dxf.center.x, entity.dxf.center.y), entity.dxf.radius)
#         elif entity.dxftype() == 'LWPOLYLINE':
#             draw_lwpolyline(ax, entity)
#             #points = entity.get_points(format='xy')
#             #draw_lwpolyline(ax, points, entity.closed)

#     # Set aspect ratio and limits for better visualization
#     ax.autoscale_view()

#     # Save the figure to a PNG file
#     #plt.savefig(outfilename, dpi=300)

#     # Optionally, display the plot
#     plt.show()


# # Function to draw a circle
# def draw_circle(ax, center, radius):
#     circle = Circle(center, radius, fill=False, color='black')
#     ax.add_patch(circle)

# # Function to draw a lightweight polyline (LWPolyline)
# def draw_lwpolyline(ax, points, is_closed):
#     if is_closed:
#         polygon = Polygon(points, closed=True, fill=False, edgecolor='black')
#         ax.add_patch(polygon)
#     else:
#         ax.plot([p[0] for p in points], [p[1] for p in points], 'k-')

# # Function to draw a line
# def draw_line(ax, start, end):
#     ax.plot([start.x, end.x], [start.y, end.y], 'k-')


# def add_arc(ax, start, end, bulge):
#     # Calculate the arc's radius and center
#     dx, dy = end[0] - start[0], end[1] - start[1]
#     dist = np.sqrt(dx**2 + dy**2)
#     radius = dist * (1 + bulge**2) / (2 * bulge)

#     # Middle point between start and end
#     mid = [(start[0] + end[0]) / 2, (start[1] + end[1]) / 2]

#     # Distance from midpoint to arc center
#     sagitta = radius - dist / 2 * abs(bulge)
#     angle = np.arctan2(dy, dx)

#     # Determine center of the arc
#     if bulge > 0:
#         center = [mid[0] + sagitta * np.sin(angle), mid[1] - sagitta * np.cos(angle)]
#     else:
#         center = [mid[0] - sagitta * np.sin(angle), mid[1] + sagitta * np.cos(angle)]

#     # Calculate start and end angles
#     start_angle = np.degrees(np.arctan2(start[1] - center[1], start[0] - center[0]))
#     end_angle = np.degrees(np.arctan2(end[1] - center[1], end[0] - center[0]))

#     # Arc drawing
#     if bulge < 0:
#         if start_angle < end_angle:
#             start_angle += 360
#     else:
#         if end_angle < start_angle:
#             end_angle += 360

#     arc = Arc(center, 2*radius, 2*radius, angle=0, theta1=start_angle, theta2=end_angle, color='black')
#     ax.add_patch(arc)


# def draw_lwpolyline(ax, entity):
#     vertices = entity.get_points(format='xyb')
#     for i in range(len(vertices) - 1):
#         start, end = vertices[i], vertices[i + 1]
#         bulge = start[2]
#         if bulge == 0:
#             ax.plot([start[0], end[0]], [start[1], end[1]], 'k-')
#         else:
#             add_arc(ax, start, end, bulge)


# def draw_lwpolyline_o2(ax, entity):
#     def add_arc(ax, start, end, bulge):
#         # Calculate midpoint
#         mid = ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)

#         # Distance between start and end points
#         dist = np.hypot(end[0] - start[0], end[1] - start[1])

#         # Radius of the arc
#         radius = dist / 2 * (1 + bulge**2) / (2 * bulge)

#         # Angle of the line connecting start and end points
#         angle = np.arctan2(end[1] - start[1], end[0] - start[0])

#         # Distance from midpoint to arc center
#         sagitta = radius - dist / 2 * bulge

#         # Calculate center of the arc
#         center_x = mid[0] + sagitta * np.sin(angle)
#         center_y = mid[1] - sagitta * np.cos(angle)

#         # Start and end angles
#         start_angle = np.arctan2(start[1] - center_y, start[0] - center_x)
#         end_angle = np.arctan2(end[1] - center_y, end[0] - center_x)

#         # Correct angles for drawing
#         if bulge < 0:
#             start_angle, end_angle = end_angle, start_angle
#         if end_angle < start_angle:
#             end_angle += 2 * np.pi

#         # Draw the arc
#         arc = Arc((center_x, center_y), 2*radius, 2*radius, theta1=np.degrees(start_angle), theta2=np.degrees(end_angle),
#                                       color='black', fill=False)
#         ax.add_patch(arc)

#     vertices = entity.get_points(format='xyb')  # x, y, bulge

#     # Draw each segment
#     for i in range(len(vertices) - 1):
#         start, end = vertices[i], vertices[i + 1]
#         bulge = start[2]
#         if bulge == 0:
#             ax.plot([start[0], end[0]], [start[1], end[1]], 'k-')
#         else:
#             add_arc(ax, start, end, bulge)

#     # Close the polyline if it's closed, considering possible bulge in last segment
#     if entity.closed:
#         start, end = vertices[-1], vertices[0]
#         bulge = start[2]
#         if bulge == 0:
#             ax.plot([start[0], end[0]], [start[1], end[1]], 'k-')
#         else:
#             add_arc(ax, start, end, bulge)


# def draw_lwpolyline_o(ax, entity):
#     vertices = entity.get_points(format='xyb')  # Get vertices and bulges
#     for i in range(len(vertices) - 1):
#         start, end = vertices[i], vertices[i + 1]
#         bulge = start[2]
#         if bulge == 0:
#             # Draw straight line for segments with no bulge
#             ax.plot([start[0], end[0]], [start[1], end[1]], 'k-')
#         else:
#             # Calculate arc for segments with bulge
#             # Arc center, radius, start angle, and end angle calculation
#             dx, dy = end[0] - start[0], end[1] - start[1]
#             distance = np.hypot(dx, dy)
#             radius = distance * (1 + bulge**2) / (4 * bulge)
#             angle = np.arctan2(dy, dx)
#             center = (start[0] + dx / 2 - radius * np.sin(angle),
#                       start[1] + dy / 2 + radius * np.cos(angle))
#             start_angle = np.degrees(np.arctan2(start[1] - center[1], start[0] - center[0]))
#             end_angle = np.degrees(np.arctan2(end[1] - center[1], end[0] - center[0]))

#             # Ensure the arc moves in the correct direction
#             if bulge < 0:
#                 start_angle, end_angle = end_angle, start_angle
#             # Correct the angles for drawing
#             if end_angle <= start_angle:
#                 end_angle += 360

#             # Draw the arc
#             arc = Arc(center, 2*radius, 2*radius, angle=0, theta1=start_angle, theta2=end_angle, color='black')
#             ax.add_patch(arc)

#     # Close the polyline if it is closed
#     if entity.closed:
#         start, end = vertices[-1], vertices[0]
#         bulge = vertices[-1][2]
#         if bulge == 0:
#             ax.plot([start[0], end[0]], [start[1], end[1]], 'k-')
#         else:
#             # Handle the last segment as an arc if needed, similar to above
#             pass  # Implement arc drawing for the closing segment if needed


# if __name__ == '__main__':
#     main()

# #%%
# import matplotlib.pyplot as plt
# import ezdxf
# from ezdxf.addons.drawing import RenderContext, Frontend
# from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
# import re


# class DXF2IMG(object):

#     default_img_format = '.png'
#     default_img_res = 300
#     def convert_dxf2img(self, names, img_format=default_img_format, img_res=default_img_res):
#         for name in names:
#             doc = ezdxf.readfile(name)
#             msp = doc.modelspace()
#             # Recommended: audit & repair DXF document before rendering
#             auditor = doc.audit()
#             # The auditor.errors attribute stores severe errors,
#             # which *may* raise exceptions when rendering.
#             if len(auditor.errors) != 0:
#                 raise Exception("The DXF document is damaged and can't be converted!")
#             else:
#                 fig = plt.figure()
#                 ax = fig.add_axes([0, 0, 1, 1])
#                 ctx = RenderContext(doc)
#                 ctx.set_current_layout(msp)
#                 ctx.current_layout.set_colors(bg='#FFFFFF')
#                 out = MatplotlibBackend(ax)
#                 Frontend(ctx, out).draw_layout(msp, finalize=True)

#                 img_name = re.findall("(\S+)\.",name)  # select the image name that is the same as the dxf file name
#                 first_param = ''.join(img_name) + img_format  #concatenate list and string
#                 fig.savefig(first_param, dpi=img_res)


# if __name__ == '__main__':
#     first = DXF2IMG()
#     first.convert_dxf2img(['C:/Users/HP/Desktop/copia_ordenador_planta_4/square_10um_2version.dxf'],img_format='.png')


# %%

#doc = ezdxf.readfile("C:/Users/HP/Desktop/copia_ordenador_planta_4/square_10um_2version.dxf")
# def example_doc():
#     doc = ezdxf.new()
#     msp = doc.modelspace()
#     x0, y0, x1, y1 = 0, 0, 0.5, 0.5
#     step= 0.1
#     start = (x0, y0)
#     end = (x0 + step, y0)
#     for color in range(1, 5):
#         msp.add_lwpolyline(
#             [start, (x0, y1), (x1, y1), (x1, y0), end], dxfattribs={"color": color}
#         )
#         x0 += step
#         x1 -= step
#         y0 += step
#         y1 -= step
#         start = end
#         end = (x0 + step, y0)
#     return doc
#     # for color in range(1, 25):
#     #     msp.add_lwpolyline(
#     #         [start, (x0, y1), (x1, y1), (x1, y0), end], dxfattribs={"color": color}
#     #     )
#     #     x0 += 0.1
#     #     x1 -= 0.1
#     #     y0 += 0.1
#     #     y1 -= 0.1
#     #     start = end
#     #     end = (x0, y0)
#     # return doc


# def export_png(doc):
#     msp = doc.modelspace()
#     # 1. create the render context
#     context = RenderContext(doc)
#     # 2. create the backend
#     #backend = svg.SVGBackend()
#     backend = pymupdf.PyMuPdfBackend()
#     # create a new configuration for a white background and and a black foreground color
#     cfg = config.Configuration(
#         background_policy=config.BackgroundPolicy.WHITE,
#         color_policy=config.ColorPolicy.COLOR,
#     )
#     # 3. create the frontend
#     frontend = Frontend(context, backend, config=cfg)
#     # 4. draw the modelspace
#     frontend.draw_layout(msp)
#     # 5. create an A4 page layout, not required for all backends
#     page = layout.Page(210, 297, layout.Units.mm, margins=layout.Margins.all(20))
#     # # 6. get the SVG rendering as string - this step is backend dependent
#     #svg_string = backend.get_string(page)
#     # 6. get the PNG rendering as bytes
#     png_bytes = backend.get_pixmap_bytes(page, fmt="png", dpi=96)
#     with open("C:/Users/HP/Desktop/wettability coating UV trearment/program to create dxf/square_500um_5loops.png", "wb") as fp:
#         fp.write(png_bytes)
#     # with open("output.svg", "wt", encoding="utf8") as fp:
#     #     fp.write(svg_string)


# def export_dark_bg(doc):
#     msp = doc.modelspace()
#     # 1. create the render context
#     context = RenderContext(doc)
#     # 2. create the backend
#     backend = pymupdf.PyMuPdfBackend()
#     # 3. create the frontend
#     frontend = Frontend(context, backend)
#     # 4. draw the modelspace
#     frontend.draw_layout(msp)
#     # 5. create an A4 page layout

#     page = layout.Page(10.5, 15, layout.Units.mm, margins=layout.Margins.all(2))
#     # page = layout.Page(0, 0, layout.Units.mm, margins=layout.Margins.all(2))

#     # 6. get the PDF rendering as bytes
#     pdf_bytes = backend.get_pdf_bytes(page)
#     with open("2square.pdf", "wb") as fp:
#         fp.write(pdf_bytes)

# def export(doc):
#     export_doc = ezdxf.new()
#     msp = doc.modelspace()
#     # 1. create the render context
#     context = RenderContext(doc)
#     # 2. create the backend
#     backend = dxf.DXFBackend(export_doc.modelspace())
#     # 3. create the frontend
#     frontend = Frontend(context, backend)
#     # 4. draw the modelspace
#     frontend.draw_layout(msp)
#     # 5. save or return DXF document
#     export_doc.saveas("C:/Users/HP/Desktop/wettability coating UV trearment/program to create dxf/square_500um_5loops.dxf")

# if __name__ == "__main__":
#     export(example_doc())
#     # export_dark_bg(example_doc())
#     export_png(example_doc())
# def paralel_lines():
#     doc = ezdxf.new()
#     msp = doc.modelspace()
#     x0, y0, x1= 0, 0, 1
#     step= 0.001

#     for color in range(1, 500):
#         msp.add_lwpolyline(
#             [(x0, y0), (x1, y0)], dxfattribs={"color": color}
#         )
#         msp.add_lwpolyline(
#             [(x1, y0  + step), (x0, y0+ step)], dxfattribs={"color": color}
#         )

#         y0 += 2*step
def paralel_lines():
    doc = ezdxf.new()
    msp = doc.modelspace()
    x0, y0, x1 = 0, 0, 0.4

    for color in range(1, 2):
        msp.add_lwpolyline(
            [(x0, y0), (x1, y0)], dxfattribs={"color": color}
        )

        y0 += 0.4

    return doc


def export_png(doc):
    msp = doc.modelspace()
    # 1. create the render context
    context = RenderContext(doc)
    # 2. create the backend
    #backend = svg.SVGBackend()
    backend = pymupdf.PyMuPdfBackend()
    # create a new configuration for a white background and and a black foreground color
    cfg = config.Configuration(
        background_policy=config.BackgroundPolicy.WHITE,
        color_policy=config.ColorPolicy.COLOR,
    )
    # 3. create the frontend
    frontend = Frontend(context, backend, config=cfg)
    # 4. draw the modelspace
    frontend.draw_layout(msp)
    # 5. create an A4 page layout, not required for all backends
    page = layout.Page(210, 297, layout.Units.mm,
                       margins=layout.Margins.all(20))
    # # 6. get the SVG rendering as string - this step is backend dependent
    #svg_string = backend.get_string(page)
    # 6. get the PNG rendering as bytes
    png_bytes = backend.get_pixmap_bytes(page, fmt="png", dpi=96)
    with open("C:/Users/HP/Desktop/wettability coating UV trearment/program to create dxf/400umline.png", "wb") as fp:
        fp.write(png_bytes)
    # with open("output.svg", "wt", encoding="utf8") as fp:
    #     fp.write(svg_string)
  

def export(doc):
    export_doc = ezdxf.new()
    msp = doc.modelspace()
    # 1. create the render context
    context = RenderContext(doc)
    # 2. create the backend
    backend = dxf.DXFBackend(export_doc.modelspace())
    # 3. create the frontend
    frontend = Frontend(context, backend)
    # 4. draw the modelspace
    frontend.draw_layout(msp)
    # 5. save or return DXF document
    export_doc.saveas(
        "C:/Users/HP/Desktop/wettability coating UV trearment/program to create dxf/400umline.dxf")


if __name__ == "__main__":
    export(paralel_lines())
    # export_dark_bg(example_doc())
    export_png(paralel_lines())
