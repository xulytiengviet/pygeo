---
layout: default
title: "Bài 6 — Tối ưu hóa tham số"
description: Hạ gradient, khớp mô hình và phân tích độ nhạy điều kiện ban đầu.
---

# Bài 6 — Tối ưu hóa tham số mô hình

Bài này tập trung vào cách khớp những hàm **không dễ đưa về dạng đa thức** với dữ liệu quan sát. Chúng ta tìm giá trị tham số sao cho mô hình giảm thiểu sai khác so với dữ liệu thực nghiệm.

## 1. Ví dụ thuyết trình ngắn

Trong khóa học gốc, giảng viên trình bày một bài thuyết trình ngắn mẫu trước khi chuyển sang nội dung tối ưu hóa. Người học có thể sử dụng cấu trúc bài này làm tham khảo khi chuẩn bị báo cáo về dữ liệu nghiên cứu của mình.

## 2. Hạ gradient (gradient descent)

Giả sử mô hình có hai tham số tự do, cần điều chỉnh để dự đoán tốt nhất dữ liệu quan sát. Với mỗi cặp giá trị tham số, ta có thể tính một **hàm mục tiêu** đo độ sai khác giữa mô hình và dữ liệu.

Hãy hình dung một bề mặt mà trục ngang biểu thị hai tham số và độ cao biểu thị giá trị hàm mục tiêu. Mục tiêu là tìm một điểm thấp nhất trong miền khảo sát, tương ứng với sai số nhỏ nhất theo tiêu chí đã chọn.

**Hạ gradient** là một họ phương pháp tối ưu sử dụng thông tin hướng biến thiên của hàm mục tiêu để cập nhật tham số. Trong bài thực hành, chúng ta sử dụng <code>scipy.optimize</code> và xây dựng những hàm Python cần thiết để tìm hai tham số tự do từ dữ liệu mẫu.

~~~python
from scipy.optimize import minimize

def ham_muc_tieu(tham_so):
    x, y = tham_so
    return (x - 2)**2 + (y + 1)**2

ket_qua = minimize(ham_muc_tieu, x0=[0, 0])
print(ket_qua.x)
~~~

Đây là ví dụ tối giản minh họa bài toán tối ưu. Notebook của khóa học sử dụng một mô hình và bộ dữ liệu khoa học thực tế hơn.

## 3. Độ nhạy đối với điều kiện ban đầu

Bề mặt hàm mục tiêu có thể chứa nhiều cực tiểu cục bộ. Một thuật toán tối ưu cục bộ có thể hội tụ về các nghiệm khác nhau nếu bắt đầu từ những điểm khác nhau; cực tiểu tìm được không nhất thiết là **cực tiểu toàn cục**.

Vì vậy, một bước kiểm tra quan trọng là chạy tối ưu từ **nhiều bộ tham số khởi tạo**, sau đó so sánh nghiệm thu được và giá trị hàm mục tiêu. Chúng ta sẽ thực hiện phân tích độ nhạy trong Notebook để kiểm tra độ ổn định của kết quả.

Trong nghiên cứu thực tế, cần cân nhắc thêm miền giá trị hợp lý về mặt vật lý, khả năng xác định tham số và độ bất định của dữ liệu.

## Notebook thực hành số 6

- [Xem Notebook bài 6](https://github.com/xulytiengviet/pygeo/blob/gh-pages/day6/day6.ipynb).
- [Tải Notebook và dữ liệu gốc](./day6/day6.zip).

## Bài tập tự luyện

Chọn một hàm có ý nghĩa với bộ dữ liệu của bạn, xây dựng hàm mục tiêu và thử tối ưu tham số. Thực hiện ít nhất vài lần chạy từ những điều kiện ban đầu khác nhau, rồi trình bày mức độ ổn định của nghiệm. Tiếp tục hoàn thiện bài thuyết trình và bản tóm tắt mở rộng cuối khóa.

---

**Điều hướng:** [← Bài 5](./day5.html) · [Bài 7 — Trực quan hóa dữ liệu địa hóa →](./day7.html).
