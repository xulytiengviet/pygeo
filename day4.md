---
layout: default
title: "Bài 4 — Phân tích phổ và FFT"
description: Phổ công suất, biến đổi Fourier nhanh và mẫu hình không gian.
---

# Bài 4 — Phân tích phổ và FFT

Hôm nay chúng ta sử dụng **phổ công suất** và **biến đổi Fourier nhanh (FFT)** để nhận diện chu kỳ theo thời gian hoặc các cấu trúc lặp theo không gian.

## 1. Phổ công suất (power spectrum)

Phổ công suất cho biết năng lượng hoặc phương sai của tín hiệu phân bố theo tần số ra sao. Trong chuỗi thời gian, nó giúp tìm những chu kỳ nổi bật; trong dữ liệu không gian, nó hỗ trợ phát hiện thang kích thước và bước sóng của mẫu hình.

Bài thực hành sử dụng thư viện <code>scipy.signal</code> để tính và trực quan hóa phổ. Từ dữ liệu mẫu, bạn sẽ so sánh phổ gốc, phổ làm trơn và nhận diện dải tần số cần phân tích.

### Khớp hàm lũy thừa

Áp dụng kỹ thuật hồi quy từ bài 3 để khảo sát sự thay đổi của phổ công suất theo tần số trong **một khoảng được chọn**. Đồ thị log–log giúp nhận diện quy luật lũy thừa khi dữ liệu phù hợp với giả định đó.

### Xác định cực đại phổ

Tìm đỉnh phổ và tần số tại đó công suất đạt giá trị lớn nhất. Khi phân tích chuỗi thời gian, cần xem xét tần suất lấy mẫu, xu thế nền và khả năng xuất hiện các đỉnh giả do nhiễu.

## 2. Mẫu hình không gian và FFT

FFT hỗ trợ phân tích các cấu trúc có tính tuần hoàn trong trường dữ liệu không gian hai chiều, ví dụ dữ liệu địa hình.

Bài thực hành dùng <code>numpy.fft</code> để chuyển từ miền không gian sang miền tần số, sau đó khám phá tự tương quan của trường dữ liệu mẫu.

### FFT hai chiều

Với raster hai chiều, có thể tính FFT theo cả hàng và cột:

~~~python
import numpy as np

pho_2d = np.fft.fft2(raster)
pho_dich_tam = np.fft.fftshift(pho_2d)
~~~

Đoạn trên minh họa thao tác biến đổi; cách tính **hàm tự tương quan** đầy đủ, chuẩn hóa và xử lý giá trị thiếu được trình bày trong Notebook thực hành.

### Hướng và bước sóng trội

Sau khi xác định hàm tự tương quan, chúng ta khảo sát vị trí các cực đại để suy ra hướng ưu thế và bước sóng đặc trưng của mẫu hình hai chiều.

## Notebook thực hành số 4

- [Xem Notebook bài 4](https://github.com/xulytiengviet/pygeo/blob/gh-pages/day4/day4.ipynb).
- [Tải dữ liệu và Notebook gốc](./day4/day4.zip).

## Bài tập tự luyện

Chọn một bộ dữ liệu của bạn để tính phổ công suất hoặc tự tương quan, nếu phương pháp phù hợp. Nếu dữ liệu chưa đáp ứng các giả định cần thiết, hãy tiếp tục hoàn thiện bài thuyết trình ngắn và bản tóm tắt mở rộng cuối khóa.

---

**Điều hướng:** [← Bài 3](./day3.html) · [Bài 5 — Nội suy và tái lập lưới →](./day5.html).
