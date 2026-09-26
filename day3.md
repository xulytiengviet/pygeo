---
layout: default
title: "Bài 3 — Hồi quy và thống kê"
description: Hồi quy tuyến tính, hệ số xác định, phân vị và phần dư.
---

# Bài 3 — Hồi quy và thống kê

Bài học giới thiệu hồi quy tuyến tính, khớp hàm lũy thừa và một số công cụ thống kê giúp đánh giá mối quan hệ giữa các biến trong dữ liệu khoa học.

## 1. Đường hồi quy phù hợp nhất

Hồi quy tuyến tính dùng để mô tả mối quan hệ giữa một biến phụ thuộc và một biến độc lập. Đây là công cụ giúp lượng hóa cách một đại lượng thay đổi theo đại lượng khác, nhưng bản thân hồi quy **không chứng minh quan hệ nhân quả**.

Trong NumPy, hàm <code>polyfit</code> có thể tìm đường thẳng phù hợp với dữ liệu:

~~~python
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2.0, 4.2, 5.8, 8.1, 9.9])
he_so = np.polyfit(x, y, deg=1)
gia_tri_du_doan = np.polyval(he_so, x)
~~~

Trong Notebook, chúng ta thực hành hồi quy tuyến tính trên dữ liệu mẫu và tận dụng phép biến đổi logarit để tìm **hàm lũy thừa** phù hợp. Xem [tài liệu <code>numpy.polyfit</code>](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html).

## 2. Hệ số xác định R²

Hệ số xác định R² biểu thị tỷ phần biến thiên của biến phụ thuộc được giải thích bởi mô hình, theo định nghĩa R² đang sử dụng. Đây là một trong nhiều chỉ số cần cân nhắc khi đánh giá độ phù hợp; chỉ số cao không tự động bảo đảm khả năng dự báo tốt.

Trong bài thực hành, R² được tính từ phần dư của đường hồi quy. Bạn cũng có thể sử dụng <code>scipy.stats.linregress</code> cho hồi quy tuyến tính đơn; giá trị <code>rvalue</code> bình phương cho R² trong trường hợp tương ứng.

## 3. Phân vị (percentile)

Phân vị cho biết vị trí của một giá trị trong phân bố dữ liệu. Ví dụ, phân vị thứ 75 là ngưỡng mà khoảng 75% quan sát nằm không lớn hơn ngưỡng đó, tùy quy ước tính.

NumPy cung cấp hàm <code>percentile</code>:

~~~python
p25, p50, p75 = np.percentile(y, [25, 50, 75])
~~~

Có thể trực quan hóa phân vị bằng **biểu đồ hộp** (box plot) hoặc đồ thị phân bố tích lũy, chẳng hạn qua hàm <code>matplotlib.pyplot.boxplot</code>.

## 4. Phân bố phần dư

**Phần dư** là hiệu giữa giá trị quan sát và giá trị mô hình dự đoán. Khảo sát phần dư giúp phát hiện các cấu trúc chưa được mô hình giải thích, ngoại lệ và dấu hiệu vi phạm giả định thống kê.

Trong một số mô hình, giả định phần dư có phân bố gần chuẩn là quan trọng. Ta có thể so sánh hàm mật độ xác suất (PDF) của phần dư với phân bố chuẩn được ước lượng theo trung bình và phương sai. [Kiểm định Kolmogorov–Smirnov](https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test) là một công cụ so sánh phân bố, nhưng cách sử dụng và hiệu chỉnh phụ thuộc việc các tham số phân bố có được ước lượng từ chính dữ liệu hay không.

Notebook trình bày ví dụ đối chiếu phân bố phần dư của hai phép khớp đường cong.

## 5. Công cụ thống kê mở rộng

Các lĩnh vực nghiên cứu khác nhau cần những phép kiểm định và mô hình khác nhau. Bạn có thể tìm hiểu thêm:

- [<code>scipy.stats</code>](https://docs.scipy.org/doc/scipy/reference/stats.html) — các phép kiểm định và phân bố xác suất.
- [scikit-learn](https://scikit-learn.org/stable/) — mô hình học máy, đánh giá và quy trình xử lý dữ liệu.

Hãy lựa chọn phương pháp dựa trên câu hỏi nghiên cứu, chất lượng dữ liệu và giả định của từng mô hình.

## Notebook thực hành số 3

- [Xem Notebook bài 3](https://github.com/xulytiengviet/pygeo/blob/gh-pages/day3/day3.ipynb).
- [Tải gói dữ liệu và Notebook gốc](./day3/day3.zip).

## Bài tập tự luyện

Nhập dữ liệu của bạn, khảo sát phân bố và thử hồi quy tuyến tính hoặc hàm lũy thừa nếu phù hợp. Trình bày **hệ số hồi quy, R² và phần dư** kèm nhận xét về giả định mô hình.

---

**Điều hướng:** [← Bài 2](./day2.html) · [Bài 4 — Phân tích phổ và FFT →](./day4.html).
