from typing import List

def solve_n_queens(n: int) -> List[List[int]]:
    if not isinstance(n, int) or n < 1:
        raise ValueError("n必须是大于等于1的整数")
    
    solutions: List[List[int]] = []
    
    def backtrack(
        row: int,
        queens: List[int],
        cols: set[int],
        diag1: set[int],
        diag2: set[int]
    ) -> None:
        """回溯递归函数，逐行尝试放置皇后。"""
        # 终止条件：所有行完成放置，记录方案
        if row == n:
            solutions.append(queens.copy())
            return
        
        # 遍历当前行的所有列，尝试放置
        for col in range(n):
            # 冲突校验：列、主对角线、副对角线均无冲突时才放置
            if col not in cols and (row - col) not in diag1 and (row + col) not in diag2:
                # 做出选择
                queens.append(col)
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                
                # 递归到下一行
                backtrack(row + 1, queens, cols, diag1, diag2)
                
                # 回溯：撤销选择
                queens.pop()
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
    
    # 初始化回溯：从第0行开始，空皇后列表，空冲突集合
    backtrack(0, [], set(), set(), set())
    return solutions

# 本地测试入口（便于截图）
if __name__ == "__main__":
    # 测试用例执行
    test_cases = [1, 2, 3, 4, 8]
    for case in test_cases:
        res = solve_n_queens(case)
        print(f"{case}皇后问题的解数量：{len(res)}")
        if case == 4:
            print(f"{case}皇后的具体解：{res}")
