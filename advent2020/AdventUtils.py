# shared utils file for common code
from typing import List, IO


class FileReaderUtils:
    """
    File reading and parsing utilities
    """

    def read(self, filename: str) -> List[str]:
        """
        Reads the specified FILE and returns a LIST of STRs

        :param: The name of the file to parse
        :return: A LIST of STRs
        """
        with open(filename) as file:
            return self.__parse_file_lines(file)

    @staticmethod
    def __parse_file_lines(file: IO):
        """
        Private method:
        Given a file returns all the lines of the file as a list

        :param file: The opened file to read
        :return: All The lines of the file as a list
        """
        return [line.strip() for line in file.readlines()]


class NumberFileReader(FileReaderUtils):
    def read_nums(self, filename: str) -> List[int]:
        """
        Reads the specified FILE and returns a LIST of INTs

        :param: The name of the file to parse
        :return: A LIST of INTs
        """
        lines = self.read(filename)  # get list of file lines
        return list(map(self.__parse_num, lines))  # parse each file line into an int

    def read_nums_sorted(self, filename: str) -> List[int]:
        """
        Reads the specified FILE and returns a sorted LIST of INTs

        :param: The name of the file to parse
        :return: A sorted LIST of INTs
        """
        lst = self.read_nums(filename)
        return sorted(lst + [0, max(lst) + 3])

    @staticmethod
    def __parse_num(val: str) -> int:
        """
        Private method:
        Parse the input STR to an INT

        :param: The STR to parse into an INT
        :return: The parsed INT value
        """
        return int(val.strip('\n'))
