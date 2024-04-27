import time

class Node:
    def __init__(self, idx, curr_value, curr_weight):
        self.idx = idx
        self.curr_value = curr_value
        self.curr_weight = curr_weight

def knapsack_brute_force_dfs(values, weights, max_weight):
    def dfs(node):
        nonlocal max_value
        # Nếu trọng lượng vượt quá giới hạn hoặc giá trị hiện tại cộng với tổng giá trị của các mặt hàng còn lại nhỏ hơn hoặc bằng giá trị tối đa hiện tại
        if node.curr_weight > max_weight or node.curr_value + (sum(values[node.idx:]) if node.idx < len(values) else 0) <= max_value:
            return
        max_value = max(max_value, node.curr_value)  # Cập nhật giá trị tối đa nếu cần
        if node.idx == len(values):  # Nếu đã duyệt hết tất cả các mặt hàng
            return
        # Chọn mặt hàng tiếp theo và thực hiện duyệt đệ quy
        dfs(Node(node.idx + 1, node.curr_value + values[node.idx], node.curr_weight + weights[node.idx]))
        # Không chọn mặt hàng tiếp theo và thực hiện duyệt đệ quy
        dfs(Node(node.idx + 1, node.curr_value, node.curr_weight))

    max_value = 0
    dfs(Node(0, 0, 0))  # Bắt đầu tìm kiếm từ mặt hàng đầu tiên
    return max_value

if __name__ == "__main__":
    # Khởi tạo danh sách giá trị và trọng lượng của các mặt hàng
    values = []  # Danh sách giá trị của các mặt hàng
    weights = []  # Danh sách trọng lượng của các mặt hàng

    # Nhập số lượng đồ và max_weight, chuyển đổi sang kiểu số nguyên
    num = int(input())  # Nhập số lượng mặt hàng
    max_weight = int(input())  # Nhập trọng lượng tối đa cho ba lôa

    # Nhập giá trị và trọng lượng của các mặt hàng
    for i in range(num):  # Lặp qua số lượng mặt hàng
        value, weight = map(int, input().split())  # Nhập giá trị và trọng lượng của mặt hàng
        values.append(value)  # Thêm giá trị vào danh sách
        weights.append(weight)  # Thêm trọng lượng vào danh sách

    # Đo thời gian thực thi của thuật toán
    start_time = time.time()
    max_value = knapsack_brute_force_dfs(values, weights, max_weight)
    end_time = time.time()
    elapsed_time = end_time - start_time

    #in ra kết quả
    print("Max value:", max_value)
    print("Elapsed time:", elapsed_time)
