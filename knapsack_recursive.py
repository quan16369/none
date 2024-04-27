from typing import List, Tuple
import time

class Item(object):
    def __init__(self, value: int, weight: int) -> None:
        # Khởi tạo đối tượng Item với giá trị và trọng lượng
        self.value: int = value  # Giá trị của mặt hàng
        self.weight: int = weight  # Trọng lượng của mặt hàng

    def __str__(self) -> str:
        # Phương thức để biểu diễn chuỗi của đối tượng Item
        return f"Value: {self.value} | Weight: {self.weight}"

def knapsack_recursive(items: List[Item], maxweight: int, index: int) -> Tuple[List[Item], int]:
    # Hàm giải bài toán knapsack sử dụng phương pháp đệ quy
    if index == 0 or maxweight == 0:
        # Nếu chỉ số hoặc trọng lượng tối đa bằng 0, trả về danh sách rỗng và tổng giá trị là 0
        return [], 0

    if items[index - 1].weight > maxweight:
        # Nếu trọng lượng của mặt hàng vượt quá trọng lượng tối đa, không chọn mặt hàng này
        return knapsack_recursive(items, maxweight, index - 1)

    # Trường hợp chọn hoặc không chọn mặt hàng đang xét
    without_this_item, without_this_value = knapsack_recursive(items, maxweight, index - 1)
    with_this_item, with_this_value = knapsack_recursive(items, maxweight - items[index - 1].weight, index - 1)
    with_this_value += items[index - 1].value

    # So sánh giữa việc chọn và không chọn mặt hàng đang xét để chọn giải pháp tốt nhất
    if with_this_value > without_this_value:
        return with_this_item + [items[index - 1]], with_this_value
    else:
        return without_this_item, without_this_value

if __name__ == "__main__":
    # Phần chính của chương trình
    values = []  # Danh sách giá trị của các mặt hàng
    weights = []  # Danh sách trọng lượng của các mặt hàng

    num = int(input())  # Số lượng mặt hàng
    max_weight = int(input())  # Trọng lượng tối đa của ba lô

    # Nhập giá trị và trọng lượng của các mặt hàng
    for i in range(num):
        value, weight = map(int, input().split())
        values.append(value)
        weights.append(weight)

    # Tạo danh sách các đối tượng Item từ giá trị và trọng lượng đã nhập
    items = [Item(value, weight) for value, weight in zip(values, weights)]

    # Gọi hàm knapsack_recursive và đo thời gian thực thi
    start_time = time.time()
    selected_items, total_value = knapsack_recursive(items, max_weight, len(items))
    end_time = time.time()
    elapsed_time_or_tools = end_time - start_time  # Thời gian thực thi của thuật toán

    # In kết quả
    print("Total value:", total_value)  # In tổng giá trị của các mặt hàng đã chọn
    print("Elapsed time:", elapsed_time_or_tools)  # In thời gian thực thi của thuật toán
