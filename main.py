from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 255, 165, 0 ]
matrix = new_matrix(0, 0)
change_matrix = new_matrix()
ident(change_matrix)

add_edge(matrix, 150, 20, 0, 290, 346, 0)
add_edge(matrix, 210, 160, 0, 320, 160, 0) #one leg
add_edge(matrix, 320, 160, 0, 260, 20, 0)
add_edge(matrix, 280, 323, 0, 390, 323, 0)
add_edge(matrix, 285, 335, 0, 150, 430, 0)
add_edge(matrix, 390, 323, 0, 315, 376, 0)
add_edge(matrix, 250, 363, 0, 330, 329, 0)
add_edge(matrix, 250, 363, 0, 284, 443, 0)
add_edge(matrix, 330, 329, 0, 364, 409, 0)
add_edge(matrix, 284, 443, 0, 364, 409, 0)
print_matrix(matrix)
#print(matrix)
draw_lines( matrix, screen, color )

color = [0, 255, 0]
change_matrix = scale(0.9)
matrix_mult(change_matrix, matrix)
print_matrix(matrix)
draw_lines(matrix, screen, color)

color = [255, 0, 0]
change_matrix = scale(0.8)
matrix_mult(change_matrix, matrix)
print_matrix(matrix)
draw_lines(matrix, screen, color)

color = [0, 0, 255]
change_matrix = scale(0.7)
matrix_mult(change_matrix, matrix)
print_matrix(matrix)
draw_lines(matrix, screen, color)

color = [165, 255, 0]
change_matrix = scale(0.6)
matrix_mult(change_matrix, matrix)
print_matrix(matrix)
draw_lines(matrix, screen, color)

color = [255, 0, 165]
change_matrix = scale(0.5)
matrix_mult(change_matrix, matrix)
print_matrix(matrix)
draw_lines(matrix, screen, color)

color = [0, 255, 165]
change_matrix = scale(0.4)
matrix_mult(change_matrix, matrix)
print_matrix(matrix)
draw_lines(matrix, screen, color)

color = [0, 165, 255]
change_matrix = scale(0.3)
matrix_mult(change_matrix, matrix)
print_matrix(matrix)
draw_lines(matrix, screen, color)

color = [165, 255, 0]
change_matrix = scale(0.2)
matrix_mult(change_matrix, matrix)
print_matrix(matrix)
draw_lines(matrix, screen, color)

color = [255, 255, 255]
change_matrix = scale(0.1)
matrix_mult(change_matrix, matrix)
print_matrix(matrix)
draw_lines(matrix, screen, color)

save_ppm(screen, "dab.ppm")
save_extension(screen, "test.ppm")
display(screen)
