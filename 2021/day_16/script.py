"""
Day 16: Packet Decoder
"""
import operator
import re
from functools import reduce
from unittest import TestCase


class StringQueue:

    def __init__(self, input_string, is_binary=False):
        if is_binary:
            self.data = input_string
        else:
            self.data = hex_to_binary(input_string)

    def get_chars(self, count, as_int=False):
        output, self.data = self.data[:count], self.data[count:]
        # print(output, as_int)
        return int(output, 2) if as_int else output

    @classmethod
    def hex_to_binary(cls, hex_string):
        binary_string = ''
        for h in hex_string:
            binary_string += str(bin(int(h, 16)))[2:].zfill(4)
        return binary_string

    def __str__(self):
        return self.data

    def __len__(self):
        return len(self.data)

    def is_finished(self):
        return '1' not in self.data


class Packet:

    def __init__(self, packet_string, from_binary=False):
        self.binary_string = StringQueue(packet_string, from_binary)

        # Header info
        self.version = self.binary_string.get_chars(3, as_int=True)
        self.type_id = self.binary_string.get_chars(3, as_int=True)
        self.version_sum = self.version

        if 4 == self.type_id:  # literal packet
            self.__process_literal__()
        else:  # operator packet
            self.length_type_id = self.binary_string.get_chars(1, as_int=True)
            self.subpackets = []
            if 0 == self.length_type_id:
                self.__process_fixed_length__()
            elif 1 == self.length_type_id:
                self.__process_fixed_count__()
            else:
                print(f'Length_type unkown: {self.length_type_id}')

    def __process_literal__(self):
        # print('Processing literal for ', self.binary_string)
        bits = []
        while True:
            lead = self.binary_string.get_chars(1, as_int=True)
            bit = self.binary_string.get_chars(4)
            bits.append(bit)
            if 0 == lead:
                break
        self.literal_value = int(''.join(bits), 2)

    def __process_fixed_length__(self):
        self.subpacket_length = self.binary_string.get_chars(15, as_int=True)
        # print(f'0 Length_type with Subpacket Length: {self.subpacket_length}')
        self.subpackets = []
        subpacket_string = self.binary_string.get_chars(self.subpacket_length)
        while '1' in subpacket_string:
            subpacket = Packet(subpacket_string, from_binary=True)
            self.subpackets.append(subpacket)
            # print(subpacket)
            subpacket_string = str(subpacket.binary_string)
            self.version_sum += subpacket.version_sum

    def __process_fixed_count__(self):
        self.subpacket_count = self.binary_string.get_chars(11, as_int=True)
        # print(f'1 Length_type with subpacket_count: {self.subpacket_count}')
        self.subpackets = []
        for _ in range(self.subpacket_count):
            subpacket = Packet(str(self.binary_string), from_binary=True)
            self.subpackets.append(subpacket)
            self.binary_string = subpacket.binary_string
            self.version_sum += subpacket.version_sum

    def __repr__(self):
        representation = f'\tVersion: {self.version}\n'
        representation += f'\tType: {self.type_id}\n'
        if 4 == self.type_id:
            representation += f'\tLiteral Value: {self.literal_value}\n'
        else:
            representation += f'\tLength ID: {self.length_type_id}\n'
            if 0 == self.length_type_id:
                representation += f'\tSubpacket Length: {self.subpacket_length}\n'
            else:
                representation += f'\tSubpacket Count: {self.subpacket_count}\n'
            representation += '\tSubpackets:'
            for subpacket in self.subpackets:
                representation += '\t' + str(subpacket) + '\n'
        return representation

    @property
    def value(self):
        if 4 == self.type_id:
            return self.literal_value
        if 0 == self.type_id:  # sum
            return sum([pack.value for pack in self.subpackets])
        if 1 == self.type_id:  # product
            return reduce(operator.mul, [pack.value for pack in self.subpackets])
        if 2 == self.type_id:  # minimum
            return min([pack.value for pack in self.subpackets])
        if 3 == self.type_id:  # maximum
            return max([pack.value for pack in self.subpackets])
        if 5 == self.type_id:  # greater than
            first_is_greater = self.subpackets[0].value > self.subpackets[1].value
            return 1 if first_is_greater else 0
        if 6 == self.type_id:  # less than
            first_is_less = self.subpackets[0].value < self.subpackets[1].value
            return 1 if first_is_less else 0
        if 7 == self.type_id:  # equal to
            are_equal = self.subpackets[0].value == self.subpackets[1].value
            return 1 if are_equal else 0



def hex_to_binary(hex_string):
    binary_string = ''
    for h in hex_string:
        binary_string += str(bin(int(h, 16)))[2:].zfill(4)
    return binary_string


def parse_file(file_name):
    data = ''
    with open(file_name, 'r') as input_file:
        for line in input_file:
            data = line.strip()
    return data


class TestPacketDecoder(TestCase):
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

    def test_literal_packet(self):
        # literal type
        packet = Packet('D2FE28')
        self.assertion(2021 == packet.literal_value)
        packet = Packet('11010001010', from_binary=True)

    def test_operator_type_zero(self):
        # length_type == 0
        packet = Packet('38006F45291200')
        self.assertion(1 == packet.version)
        self.assertion(6 == packet.type_id)
        self.assertion(0 == packet.length_type_id)
        self.assertion(27 == packet.subpacket_length)
        self.assertion([10, 20] == [pack.literal_value for pack in packet.subpackets])

    def test_operator_type_one(self):
        # length_type == 1
        packet = Packet('EE00D40C823060')
        self.assertion(7 == packet.version)
        self.assertion(3 == packet.type_id)
        self.assertion(1 == packet.length_type_id)
        expected_literals = [1, 2, 3]
        found_literals = [pack.literal_value for pack in packet.subpackets]
        self.assertion(expected_literals == found_literals)

    def test_one_example(self):
        packets = {
            '8A004A801A8002F478': 16,
            '620080001611562C8802118E34': 12,
            'C0015000016115A2E0802F182340': 23,
            'A0016C880162017C3686B18A3D4780': 31,
        }
        for given, expected in packets.items():
            packet = Packet(given)
            self.assertion(expected == packet.version_sum)

    def test_one_data(self):
        packet = Packet(self.input_data)
        self.assertion(991 == packet.version_sum)

    def test_two_example(self):
        data = {
            'C200B40A82': 3,
            '04005AC33890': 54,
            '880086C3E88112': 7,
            'CE00C43D881120': 9,
            'D8005AC2A8F0': 1,
            'F600BC2D8F': 0,
            '9C005AC2F8F0': 0,
            '9C0141080250320F1802104A08': 1,
        }
        for given, expected in data.items():
            packet = Packet(given)
            # print(f'Given {given} resulted in {packet.value}, expected: {expected}')
            self.assertion(expected == packet.value)

    def test_two_data(self):
        packet = Packet(self.input_data)
        self.assertion(1264485568252 == packet.value)
