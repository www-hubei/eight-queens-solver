import pytest
from src.eight_queens import solve_n_queens

def test_n_queens_valid_input():
    """测试合法输入的解的数量和正确性"""
    assert solve_n_queens(1) == [[0]]
    assert solve_n_queens(2) == []
    assert solve_n_queens(3) == []
    assert len(solve_n_queens(4)) == 2
    assert [1, 3, 0, 2] in solve_n_queens(4)
    assert [2, 0, 3, 1] in solve_n_queens(4)
    assert len(solve_n_queens(8)) == 92

def test_n_queens_invalid_input():
    """测试非法输入的异常抛出（提升代码健壮性）"""
    with pytest.raises(ValueError):
        solve_n_queens(0)
    with pytest.raises(ValueError):
        solve_n_queens(-5)
    with pytest.raises(ValueError):
        solve_n_queens(3.5)
