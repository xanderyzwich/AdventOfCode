"""
Day 17: Conway Cubes
"""
from unittest import TestCase

active = '#'
inactive = '.'


class PocketCubes:

    def __init__(self, rules={}, file_name=None, boot=True,):
        self.active_cells = []
        self.range = None
        self.rules = rules
        self.cycles_complete = 0
        if file_name:
            self.read_file(file_name)
        if boot:
            self.boot()

    def read_file(self, file_name):
        with open(file_name, 'r') as input_file:
            x, y, z = 0, 0, 0
            for line in input_file:
                x = 0
                row = list(line.rstrip())
                for cell in row:
                    if cell == active:
                        self.activate(x, y, z)
                    x += 1
                y += 1

    def boot(self):
        self.execute(cycles=6)
        # for _ in range(6):
        #     self.execute()

    def set_rules(self, rule_dict):
        self.rules = rule_dict

    def execute(self, cycles=1):
        # Execute defined number of cycles
        for i in range(cycles):
            print(f'EXECUTING: {cycles-i} cycles left ')
            next_pc = PocketCubes(boot=False)
            neighbor_count = self.neighbor_count()
            for cell in self.active_cells:
                if cell in neighbor_count and self.rules[active](neighbor_count[cell]):
                    next_pc.activate(*cell)
            for cell, count in neighbor_count.items():
                if not self.cell_is_active(*cell) and self.rules[inactive](count):
                    next_pc.activate(*cell)
            self.active_cells = next_pc.active_cells.copy()
            self.range = next_pc.range
            self.cycles_complete += 1
        print(f'Excution of {cycles} cycles is complete')


    def neighbor_count(self):
        active_neighbor_counts = {}
        for base_cell in self.active_cells:
            for neighbor_cell in PocketCubes.neighbor_list(*base_cell):
                if neighbor_cell in active_neighbor_counts.keys():
                    active_neighbor_counts[neighbor_cell] += 1
                else:
                    active_neighbor_counts[neighbor_cell] = 1
        return active_neighbor_counts

    def cell_is_active(self, x, y, z):
        return (x, y, z) in self.active_cells

    def activate(self, x, y, z):
        cell = (x, y, z)
        if cell not in self.active_cells:
            self.active_cells.append(cell)
        self.update_range(*cell)
        
    def update_range(self, col, row, layer):
        if not self.range:
            self.range = [[col, col], [row, row], [layer, layer]]
            return
        for i, q in enumerate([col, row, layer]):
            if q < self.range[i][0]:
                self.range[i][0] = q
            elif q > self.range[i][1]:
                self.range[i][1] = q
        # print(f'Updating range with {col, row, layer}')

    @staticmethod
    def neighbor_list(x, y, z):
        """
        Assemble the list of neighboring cell coords in 3-space
        :params x, y, z: 3d coords of base cell
        :return: list of coordinates for the 26 cells neighboring the base cell
        """
        neighbors = []
        for layer in [z-1, z, z+1]:
            for row in [y-1, y, y+1]:
                for col in [x-1, x, x+1]:
                    if (col, row, layer) != (x, y, z):
                        neighbors.append((col, row, layer))
        return neighbors

    def __repr__(self):
        result = ''
        return str(self.active_cells)

    def __len__(self):
        return len(self.active_cells)

    def print(self):
        from rich.console import Console
        from rich.table import Table
        
        console = Console()
        table = Table(title=f'After {self.cycles_complete} cycle{"s" if self.cycles_complete != 1 else ""}', show_header=True, show_lines=True)
        table.add_column("Z-val")
        table.add_column("Layer")
        
        x_range, y_range, z_range = self.range
        for layer in range(z_range[0], z_range[1]+1):
            temp_str = ''
            for row in range(y_range[0], y_range[1]+1):
                for col in range(x_range[0], x_range[1]+1):
                    # print(col, row, layer)
                    temp_str += f'{active} ' if self.cell_is_active(col, row, layer) else f'{inactive} '
                temp_str += '\n'
            table.add_row(str(layer), temp_str.rstrip())
        print(f'Active cells: {self}')
        print(f'Range: {self.range}')
        console.print(table)


class TestThing(TestCase):

    rules_part1 = {  # return True if cell will be active next turn
        active: lambda count: count in [2, 3],
        inactive: lambda count: count == 3
    }

    def setUp(self) -> None:
        print(f'\n--- Running test: {self._testMethodName} ---')

    def test_one_dev(self):
        pc = PocketCubes(self.rules_part1, file_name='example.txt', boot=False)
        pc.print()
        for i in range(6):
            pc.execute()
            pc.print()
        assert len(pc) == 112

    def test_one_example(self):
        pc = PocketCubes(self.rules_part1, file_name='example.txt', boot=True)
        assert len(pc) == 112

    def test_one_data(self):
        pc = PocketCubes(self.rules_part1, file_name='data.txt')
        print(len(pc))
        assert len(pc) == 267

    def test_two_example(self):
        assert True

    def test_two_data(self):
        assert True
