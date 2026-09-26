---
layout: default
title: "Bài 1 — Nhập môn và cài đặt"
description: Cài đặt Python, JupyterLab và tạo biểu đồ đầu tiên.
---

# Bài 1 — Nhập môn và cài đặt

Trong buổi đầu, chúng ta làm quen với khóa học, thiết lập môi trường làm việc và tạo biểu đồ đầu tiên bằng Python.

## Tổng quan

Giáo trình tập trung vào các kỹ thuật **xử lý, phân tích và trình bày dữ liệu khoa học Trái Đất bằng Python**. Người học sử dụng dữ liệu thực tế được cung cấp hoặc bộ dữ liệu trong nghiên cứu của chính mình. Những nội dung chính gồm phân tích tương quan, phổ công suất, tái lập lưới và khớp đường cong.

Mục tiêu cuối cùng là giúp bạn tự tin tạo các hình minh họa đạt chất lượng công bố khoa học từ dữ liệu riêng, đồng thời lưu lại quy trình phân tích để người khác có thể tái lập kết quả.

## Chuẩn bị phần mềm

### Python

Python là ngôn ngữ lập trình sử dụng xuyên suốt khóa học. Tải phiên bản phù hợp với hệ điều hành từ [trang chính thức của Python](https://www.python.org/downloads/). Trên Windows, hãy đánh dấu tùy chọn thêm Python vào PATH nếu trình cài đặt cung cấp.

Kiểm tra cài đặt trong Terminal hoặc PowerShell:

~~~bash
python --version
~~~

### pip — Trình quản lý gói

<code>pip</code> giúp cài đặt và cập nhật thư viện Python. Phần lớn bản cài Python hiện nay đã bao gồm pip. Kiểm tra bằng:

~~~bash
python -m pip --version
~~~

Nếu chưa có pip, xem [hướng dẫn cài đặt chính thức](https://pip.pypa.io/en/stable/installation/).

### JupyterLab — Môi trường thực hành

JupyterLab cho phép viết mã, chạy từng ô lệnh, xem biểu đồ và ghi chú trong cùng một tệp Notebook.

~~~bash
python -m pip install jupyterlab
~~~

[Tài liệu JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)

### NumPy — Tính toán số

NumPy hỗ trợ mảng nhiều chiều, phép toán ma trận và nhiều thao tác tính toán khoa học.

~~~bash
python -m pip install numpy
~~~

[Tài liệu NumPy](https://numpy.org/install/)

### pandas — Xử lý bảng dữ liệu

pandas giúp đọc, lọc, biến đổi và tổng hợp dữ liệu dạng bảng như CSV và Excel.

~~~bash
python -m pip install pandas
~~~

[Tài liệu pandas](https://pandas.pydata.org/docs/getting_started/install.html)

### Matplotlib — Trực quan hóa

Matplotlib hỗ trợ biểu đồ đường, phân tán, bản đồ raster và những hình minh họa phức hợp.

~~~bash
python -m pip install matplotlib
~~~

[Tài liệu Matplotlib](https://matplotlib.org/stable/users/installing/index.html)

> **Gợi ý:** Có thể cài các gói thực hành cơ bản bằng một lệnh: <code>python -m pip install jupyterlab numpy pandas matplotlib</code>. Với dự án nghiên cứu, nên sử dụng môi trường ảo để tránh xung đột thư viện.

## Notebook thực hành số 1

Mở JupyterLab bằng lệnh:

~~~bash
jupyter lab
~~~

Trình duyệt sẽ mở giao diện JupyterLab. Bạn có thể tạo Notebook mới hoặc mở ví dụ của bài này:

- [Xem Notebook bài 1 trong kho PyGeo](https://github.com/xulytiengviet/pygeo/blob/gh-pages/day1/day1.ipynb).
- [Tải bộ Notebook và dữ liệu mẫu gốc](./day1/day1.zip).

Notebook giới thiệu cách nạp thư viện, khai báo hàm và hằng số, đọc dữ liệu, phân tích và trực quan hóa.

## Bài tập tự luyện

Tạo một Notebook tương tự, nhưng **đọc bảng dữ liệu của chính bạn** và vẽ ít nhất một biểu đồ thể hiện mối quan hệ giữa các biến. Lưu lại mã nguồn, biểu đồ và nguồn dữ liệu để có thể chạy lại.

---

**Bài tiếp theo:** [Bài 2 — Đọc và xử lý dữ liệu](./day2.html).
