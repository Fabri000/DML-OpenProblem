def scalar_multiply(
    matrix: list[list[int | float]],
    scalar: int | float,
) -> list[list[int | float]]:
    # Multiply each element by the scalar
    return [[element * scalar for element in row] for row in matrix]

def test_scalar_multiply() -> None:
    # Test cases for scalar_multiply function

    # Test case 1
    matrix = [[1, 2], [3, 4]]
    scalar = 2
    assert scalar_multiply(matrix, scalar) == [[2, 4], [6, 8]]

    # Test case 2
    matrix = [[0, -1], [1, 0]]
    scalar = -1
    assert scalar_multiply(matrix, scalar) == [[0, 1], [-1, 0]]

    # Test case  3
    assert scalar_multiply([[5, -1], [0, 2]], 1) == [[5, -1], [0, 2]]

    # Test case  4
    assert scalar_multiply([[1, -2], [-3, 4]], -3) == [[-3, 6], [9, -12]]

    # Test case  5
    assert scalar_multiply([[7]], 3) == [[21]]

    # Test case  6
    assert scalar_multiply([], 5) == []

    # Test case  7
    assert scalar_multiply([[]], 2) == [[]]

    # Test case  8
    assert scalar_multiply([[1, 2, 3], [4, 5, 6]], 2) == [[2, 4, 6], [8, 10, 12]]

if __name__ == "__main__":
    test_scalar_multiply()
    print("All scalar_multiply tests passed.")
