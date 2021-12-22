"""
Day X: Name
"""
import functools
from copy import deepcopy
from unittest import TestCase


def enhance(image, enhancement_algorithm):
    enhanced_image = [['.' for _ in range(len(image[0]))] for _ in range(len(image))]
    bright_count = 0
    for r in range(len(image)):
        for c in range(len(image[r])):
            enhanced_pixel = enhancement_algorithm[pixel_ref_code(image, r, c)]
            enhanced_image[r][c] = enhanced_pixel
            if '#' == enhanced_pixel:
                bright_count += 1
    return enhanced_image, bright_count


def paint_image(img):
    print()
    for line in img:
        print(''.join(line))


def zoom_out(image, pixels_per_side=2):
    new_len = len(image) + (2 * pixels_per_side)
    bigger_image = []
    for _ in range(pixels_per_side):
        bigger_image.append(['.' for _ in range(new_len)])
    for r in range(len(image)):
        row = ['.' for _ in range(pixels_per_side)]
        for pixel in image[r]:
            row.append(pixel)
        for _ in range(pixels_per_side):
            row.append('.')
        bigger_image.append(row)
    for _ in range(pixels_per_side):
        bigger_image.append(['.' for _ in range(new_len)])
    return bigger_image


def pixel_ref_code(image, row, col):
    digits = ''
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            try:
                digits += '1' if '#' == image[r][c] else '0'
            except IndexError:
                digits += '0'
    return int(digits, 2)


def multiple_enhance(image, enhancement_algorithm, times=2):
    current_image = zoom_out(image, pixels_per_side=times * 2)
    for _ in range(times):
        current_image, bright_count = enhance(current_image, enhancement_algorithm)
    return current_image, bright_count


def parse_file(file_name):
    image, enhancement_algorithm = [], ''
    with open(file_name, 'r') as input_file:
        for line in input_file:
            clean = line.strip()
            if 0 < len(clean):
                if 0 == len(enhancement_algorithm):
                    enhancement_algorithm = clean
                else:
                    image.append(list(clean))
    return image, enhancement_algorithm


class TestThing(TestCase):
    example_data = parse_file('example.txt')
    input_data = parse_file('input.txt')

    @classmethod
    def setUpClass(cls) -> None:
        print(f'\nExecuting {cls.__name__}')

    def setUp(self) -> None:
        self.current_result = False
        print(f'\t Running {self._testMethodName}', end='\n\t\t')

    def assertion(self, test_passes) -> None:
        self.current_result = test_passes
        assert test_passes

    def tearDown(self) -> None:
        test_result = 'PASS' if self.current_result else 'FAIL'
        self.current_result = False
        print('\t\t' + test_result)

    def test_one_example(self):
        _, count = multiple_enhance(*self.example_data)
        self.assertion(35 == count)

    def test_one_data(self):
        image, count = multiple_enhance(*self.input_data)
        self.assertion(5349 == count)

    def test_two_example(self):
        _, count = multiple_enhance(*self.example_data, times=50)
        self.assertion(3351 == count)

    def test_two_data(self):
        image, count = multiple_enhance(*self.input_data, times=50)
        self.assertion(15806 == count)
