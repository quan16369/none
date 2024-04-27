from typing import List, Tuple
import time

class Item(object):
    def __init__(self, value: int, weight: int) -> None:
        self.value: int = value
        self.weight: int = weight

    def __str__(self) -> str:
        return f"Value: {self.value} | Weight: {self.weight}"

def knapsack_dynamic(items: List[Item], maxweight: int) -> int:
    # Khởi tạo ma trận lưu giá trị tối ưu của các mặt hàng
    # dp[i][j] sẽ lưu giá trị lớn nhất có thể đạt được với i mặt hàng và trọng lượng tối đa j
    dp = [[0] * (maxweight + 1) for _ in range(len(items) + 1)]

    # Tính toán giá trị tối ưu cho từng trọng lượng từ 0 đến maxweight
    for i in range(1, len(items) + 1):
        for j in range(1, maxweight + 1):
            # Nếu trọng lượng của mặt hàng i lớn hơn trọng lượng tối đa j, không thể chọn mặt hàng này
            if items[i - 1].weight > j:
                dp[i][j] = dp[i - 1][j]
            else:
                # Nếu có thể chọn mặt hàng này, so sánh giữa việc chọn và không chọn mặt hàng này
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[i - 1].weight] + items[i - 1].value)

    return dp[len(items)][maxweight]

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

    # Tạo danh sách các đối tượng Item từ giá trị và trọng lượng đã cho
    items = [Item(value, weight) for value, weight in zip(values, weights)]

    # Đo thời gian thực thi của thuật toán
    start_time = time.time()
    max_value = knapsack_dynamic(items, max_weight)
    end_time = time.time()
    elapsed_time = end_time - start_time

    # In kết quả
    print("Max value:", max_value)
    print("Elapsed time:", elapsed_time)
