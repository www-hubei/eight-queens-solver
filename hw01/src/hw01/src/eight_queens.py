def solve_n_queens(n: int) -> list[list[int]]:
    if n < 1:
        return []
    
    solutions = []
    
    def backtrack(row: int, queens: list[int], 
                  cols: set[int], diag1: set[int], diag2: set[int]) -> None:
        if row == n:
            solutions.append(queens.copy())
            return
        
        for col in range(n):
            if col not in cols and (row - col) not in diag1 and (row + col) not in diag2:
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                queens.append(col)
                
                backtrack(row + 1, queens, cols, diag1, diag2)
                
                queens.pop()
                diag2.remove(row + col)
                diag1.remove(row - col)
                cols.remove(col)
    
    backtrack(0, [], set(), set(), set())
    return solutions
