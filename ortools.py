import time
from typing import List, Tuple
from ortools.algorithms.python import knapsack_solver

class Item(object):
    def __init__(self, value: int, weight: int) -> None:
        self.value: int = value
        self.weight: int = weight

    def __str__(self) -> str:
        return f"Value: {self.value} | Weight: {self.weight}"

def solve_knapsack_or_tools(values: List[int], weights: List[int], max_weight: int) -> int:
    # Khởi tạo solver knapsack từ thư viện OR-Tools
    solver = knapsack_solver.KnapsackSolver(
            knapsack_solver.SolverType.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,"KnapsackExample")
    # Khởi tạo knapsack solver với các giá trị và trọng lượng đã cho
    solver.init(values, [weights], [max_weight])
    # Giải bài toán knapsack và trả về giá trị tối ưu
    computed_value = solver.solve()
    return computed_value

if __name__ == "__main__":
    # Khởi tạo danh sách giá trị và trọng lượng của các mặt hàng
    values = []  # Danh sách giá trị của các mặt hàng
    weights = []  # Danh sách trọng lượng của các mặt hàng

    # Nhập số lượng đồ và max_weight, chuyển đổi sang kiểu số nguyên
    num = int(input())  # Nhập số lượng mặt hàng
    max_weight = int(input())  # Nhập trọng lượng tối đa cho ba lô

    # Nhập giá trị và trọng lượng của các mặt hàng
    for i in range(num):  # Lặp qua số lượng mặt hàng
        value, weight = map(int, input().split())  # Nhập giá trị và trọng lượng của mặt hàng
        values.append(value)  # Thêm giá trị vào danh sách
        weights.append(weight)  # Thêm trọng lượng vào danh sách


    start_time = time.time()
    # Gọi hàm solve_knapsack_or_tools để giải bài toán knapsack
    computed_value_or_tools = solve_knapsack_or_tools(values, weights, max_weight)
    end_time = time.time()
    elapsed_time_or_tools = end_time - start_time

    # In kết quả
    print("Total value:", computed_value_or_tools)  # In tổng giá trị tối ưu của các mặt hàng đã chọn
    print("Elapsed time:", elapsed_time_or_tools)  # In thời gian thực thi của thuật toán
