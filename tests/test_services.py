from src import services

class TestServices:
    def test_transpose(self):
        transposed_matrix = services.transpose_matrix([[1,2,3],[4,5,6],[7,8,9]])
        assert transposed_matrix == [[1,4,7],[2,5,8],[3,6,9]]