---
layout: default
title: "Bài 8 — Hình minh họa cho công bố khoa học"
description: Thiết kế hình nhiều ô và xuất ảnh theo yêu cầu tạp chí.
---

# Bài 8 — Thiết kế hình minh họa cho công bố khoa học

Bài này tập trung vào việc tạo những hình ảnh **rõ ràng, chính xác và đáp ứng yêu cầu xuất bản** từ dữ liệu và mã nguồn Python.

## 1. Các thành phần của một hình khoa học

Cũng như bài viết, hình minh họa cần giúp người đọc nắm được câu hỏi và kết quả nghiên cứu. Một hình tốt có thể truyền tải thông tin ngay cả khi người đọc chỉ xem các trục, ký hiệu, chú giải và chú thích.

Mỗi tạp chí có yêu cầu riêng về:

- Họ phông chữ, cỡ chữ và độ dày đường.
- Kích thước hình một cột hoặc hai cột; bố cục các ô con.
- Nhãn ô như (a), (b), (c); chú giải và thang màu.
- Định dạng tệp, độ phân giải, cách xuất hình vector hoặc raster.

Bài học lấy [hướng dẫn hình minh họa của Nature](https://www.nature.com/documents/Final_guide_to_authors.pdf) làm ví dụ. **Hãy kiểm tra quy định hiện hành của tạp chí đích trước khi nộp bài**, vì yêu cầu xuất bản có thể thay đổi.

## 2. Triển khai bằng Matplotlib

Chúng ta tiếp tục sử dụng Matplotlib nhưng kiểm soát kỹ hơn những tham số trình bày: kích thước, vị trí, căn chỉnh, trục tọa độ, độ phân giải và cách xuất ảnh.

Quy trình đề xuất:

1. Phác thảo bố cục toàn hình trên giấy: số ô, tỷ lệ, thông điệp chính của từng ô.
2. Xác định các yếu tố dùng chung như kiểu chữ, bảng màu, khoảng cách và hệ tọa độ.
3. Tạo biến cho những vị trí có quan hệ với nhau để việc căn chỉnh được nhất quán.
4. Viết mã vẽ từng ô, bổ sung nhãn và chú giải; kiểm tra khả năng đọc ở kích thước in thực tế.
5. Xuất thử và kiểm tra tệp theo chuẩn của tạp chí.

Một số thiết lập cơ bản:

~~~python
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.size': 8,
    'figure.dpi': 150,
    'savefig.dpi': 300,
})
~~~

Các giá trị trên chỉ là **minh họa**. Bản thực hành đi sâu vào việc kết hợp nhiều ô biểu đồ và định vị các thành phần một cách có kiểm soát.

## Notebook thực hành số 8

- [Xem Notebook bài 8](https://github.com/xulytiengviet/pygeo/blob/gh-pages/day8/day8.ipynb).
- [Tải Notebook và dữ liệu gốc](./day8/day8.zip).

## Bài tập tự luyện

Tạo một hình chất lượng công bố từ dữ liệu của bạn. Kiểm tra nhãn trục, đơn vị đo, màu sắc, chú giải, kích thước và độ phân giải. Tiếp tục hoàn thiện bài thuyết trình ngắn và bản tóm tắt mở rộng cuối khóa.

---

**Điều hướng:** [← Bài 7](./day7.html) · [Bài 9 — GitHub, Zenodo và DOI →](./day9.html).
