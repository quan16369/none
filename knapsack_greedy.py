from typing import List, Tuple  # Import các kiểu dữ liệu List và Tuple từ module typing
import time  # Import module time để đo thời gian thực thi

class Item(object):  # Định nghĩa lớp Item
    def __init__(self, value: int, weight: int) -> None:  # Hàm khởi tạo của lớp Item
        self.value: int = value  # Giá trị của mặt hàng
        self.weight: int = weight  # Trọng lượng của mặt hàng

    def __str__(self) -> str:  # Định nghĩa phương thức __str__ để in ra thông tin của mặt hàng
        return f"Value: {self.value} | Weight: {self.weight}"  # Trả về chuỗi thông tin của mặt hàng

def knapsack_greedy(items: List[Item], maxweight: int) -> int:  # Hàm giải bài toán knapsack dùng phương pháp tham lam
    sorted_items = sorted(items, key=lambda item: item.value / item.weight, reverse=True)  # Sắp xếp các mặt hàng theo tỷ lệ giá trị/trọng lượng giảm dần
    selected_items = []
    total_weight = 0  # Khởi tạo tổng trọng lượng được chọn ban đầu
    total_value = 0  # Khởi tạo tổng giá trị được chọn ban đầu

    for item in sorted_items:  # Duyệt qua từng mặt hàng đã sắp xếp
        if total_weight + item.weight <= maxweight:  # Kiểm tra nếu thêm mặt hàng này vào không vượt quá trọng lượng tối đa
            selected_items.append(item)
            total_weight += item.weight  # Cập nhật tổng trọng lượng
            total_value += item.value  # Cập nhật tổng giá trị

    return total_value  # Trả về tổng giá trị của các mặt hàng đã chọn

if __name__ == "__main__":  # Khối chương trình chính
    values = []  # Danh sách giá trị của các mặt hàng
    weights = []  # Danh sách trọng lượng của các mặt hàng

    # Nhập số lượng đồ và max_weight, chuyển đổi sang kiểu số nguyên
    num = int(input())  # Nhập số lượng mặt hàng
    max_weight = int(input()) # Nhập trọng lượng tối đa cho ba lô

    # Nhập giá trị của các đồ
    for i in range(num):  # Lặp qua số lượng mặt hàng
        value, weight = map(int, input().split())  # Nhập giá trị và trọng lượng của mặt hàng
        values.append(value)  # Thêm giá trị vào danh sách
        weights.append(weight)  # Thêm trọng lượng vào danh sách

    # Tạo danh sách các đồ từ giá trị và trọng lượng đã nhập
    items = [Item(value, weight) for value, weight in zip(values, weights)]

    # Gọi hàm knapsack_greedy và tính thời gian thực thi
    start_time = time.time()  # Bắt đầu đo thời gian
    total_value = knapsack_greedy(items, max_weight)  # Gọi hàm giải bài toán knapsack
    end_time = time.time()  # Kết thúc đo thời gian
    elapsed_time_or_tools = end_time - start_time  # Tính thời gian thực thi

    # In kết quả
    print("Total value:", total_value)  # In tổng giá trị của các mặt hàng đã chọn
    print("Elapsed time:", elapsed_time_or_tools)  # In thời gian thực thi của thuật toán
