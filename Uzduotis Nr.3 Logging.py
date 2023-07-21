import logging
logging.basicConfig(
    level=logging.DEBUG
    filename='log_file.log'
    level=logging.INFO
    logging.critical()
)
def calculate_rectangle_properties(length, width):
    area = length * width
    perimeter = (length + width) * 2

    return area, perimeter

length = float(input('Enter the lenngth of the rectangle: '))
width = float(input('Enter the width of the rectangle: '))

area, perimeter = calculate_rectangle_properties(length, width)
print(area)
print(perimeter)