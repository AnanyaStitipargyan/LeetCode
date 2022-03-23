class Zigzag_Conversion_Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # List of numRows lists to record the characters of each row
        data = [[] for i in range(numRows)]

        # The zig-zag row sequence: 0, 1, 2, ..., numRows-1, ..., 2, 1
        sequence = list(range(numRows)) + list(range(numRows - 2, 0, -1))

        # Distribute the characters in s across the rows following the sequence
        n = len(sequence)
        for i in range(len(s)):
            row_number = sequence[i % n]
            data[row_number].append(s[i])

        # Combine the rows to prepare the result
        output = []
        for sublist in data:
            output.extend(sublist)
        return "".join(output)
