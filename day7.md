---
layout: default
title: "Bài 7 — Trực quan hóa địa hóa"
description: Chuẩn hóa bảng mẫu, biểu đồ tương quan và khớp đường đẳng thời.
---

# Bài 7 — Trực quan hóa dữ liệu địa hóa

Bài thực hành hướng dẫn cách tổ chức bảng phân tích địa hóa, so sánh hàm lượng nguyên tố hoặc tỷ số đồng vị và xây dựng biểu đồ phục vụ suy luận về tuổi địa chất.

## 1. Chuẩn bị bảng dữ liệu mẫu

Trong nghiên cứu, dữ liệu nhận từ bài báo, đồng nghiệp hoặc kho dữ liệu thường chưa được tổ chức theo cấu trúc phù hợp với chương trình phân tích.

Với bảng tính, chúng ta có hai cách tiếp cận:

1. **Chuẩn hóa bảng tính trước khi đọc:** chỉnh sửa trực tiếp trong Excel hoặc phần mềm tương tự để các cột, hàng và tên trường tương thích với <code>pandas.read_csv</code> hoặc <code>pandas.read_excel</code>.
2. **Xử lý khi nhập dữ liệu:** giữ nguyên bảng tính gốc, sử dụng tham số của pandas hoặc mã xử lý để đọc và chuyển đổi sang cấu trúc cần thiết.

Lựa chọn phụ thuộc số lượng tệp, độ lặp lại và yêu cầu truy vết nguồn dữ liệu. Nếu có hàng trăm bảng cùng cấu trúc, tự động hóa khâu nhập dữ liệu thường tiết kiệm thời gian hơn.

Hãy đối chiếu những tệp bảng tính trong thư mục bài 7 do các cộng tác viên Lucas và Erick cung cấp để hiểu cách chuẩn hóa dữ liệu đầu vào.

## 2. Biểu đồ tham số

Trong phân tích địa hóa, chúng ta thường đo hàm lượng của nhiều nguyên tố hoặc đồng vị trên một tập mẫu. Quan hệ giữa những đại lượng này hỗ trợ giải thích các quá trình và điều kiện mà mẫu đã trải qua.

Để khảo sát dữ liệu ban đầu, một phương pháp trực quan là **ma trận biểu đồ phân tán**: mỗi ô biểu diễn mối quan hệ giữa hai nguyên tố hoặc hai đồng vị, còn mỗi điểm là một mẫu phân tích.

Notebook cung cấp hàm <code>parascatter</code> để vẽ trực tiếp ma trận cho một tập biến được chọn. Hãy đọc định nghĩa hàm và thử điều chỉnh theo tên cột, thang trục, ký hiệu điểm hoặc sai số đo trong dữ liệu của bạn.

## 3. Khớp dữ liệu để ước tính tuổi

Một số hệ đồng vị phóng xạ cho phép ước tính tuổi địa chất dựa trên quan hệ tỷ số đồng vị và quy luật phân rã, với điều kiện đáp ứng những giả định của hệ định tuổi.

Bài này sử dụng **hệ rubidi–stronti (Rb–Sr)**. Bạn sẽ khảo sát tỷ số đồng vị, thực hiện phép khớp phù hợp và tính tuổi theo công thức được trình bày trong Notebook.

Khi diễn giải kết quả, cần lưu ý sai số đo, sự phù hợp của các mẫu và các giả định về hệ địa hóa. Một đường hồi quy không tự động xác nhận mọi điều kiện của phương pháp định tuổi.

## Notebook thực hành số 7

- [Xem Notebook bài 7](https://github.com/xulytiengviet/pygeo/blob/gh-pages/day7/day7.ipynb).
- [Tải bộ dữ liệu bảng tính và Notebook gốc](./day7/day7.zip).

## Bài tập tự luyện

Đọc dữ liệu mẫu của bạn và trực quan hóa bằng những biểu đồ phù hợp. Nếu có dữ liệu địa hóa, hãy thử ma trận biểu đồ phân tán hoặc khớp đường liên quan đến bài toán nghiên cứu. Song song đó, hoàn thiện bài thuyết trình và bản tóm tắt mở rộng.

---

**Điều hướng:** [← Bài 6](./day6.html) · [Bài 8 — Thiết kế hình công bố →](./day8.html).
