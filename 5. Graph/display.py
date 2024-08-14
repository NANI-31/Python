import tkinter as tk
import math

def display_graphical(graph):
    window = tk.Tk()
    window.title("Graph Representation")
    canvas = tk.Canvas(window, width=600, height=600, bg="white")
    canvas.pack()

    node_positions = _calculate_positions(graph.vertices, 300, 300, 200)

    # Draw nodes
    for node, pos in node_positions.items():
        x, y = pos
        canvas.create_oval(x-20, y-20, x+20, y+20, fill="lightblue")
        canvas.create_text(x, y, text=str(node), font=("Arial", 15, "bold"))

    # Draw edges
    edges = graph.get_edges()
    for src, dest in edges:
        x1, y1 = node_positions[src]
        x2, y2 = node_positions[dest]
        canvas.create_line(x1, y1, x2, y2)

    window.mainloop()

def _calculate_positions(vertices, center_x, center_y, radius):
    positions = {}
    angle_gap = 2 * math.pi / vertices
    for i in range(vertices):
        angle = i * angle_gap
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        positions[i] = (x, y)
    return positions
