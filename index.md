---
layout: default
title: Trang chủ
description: Giáo trình thực hành phân tích dữ liệu khoa học Trái Đất bằng Python, tiếng Việt.
---

<div class="hero">
  <p class="eyebrow">GIÁO TRÌNH PYTHON CHO KHOA HỌC TRÁI ĐẤT</p>
  <h1>Từ dữ liệu thực tế đến hình ảnh khoa học có thể tái lập</h1>
  <p>Học đọc, phân tích và trực quan hóa dữ liệu địa lý, địa hình, khí hậu và địa hóa bằng Python qua chín bài thực hành. Tài liệu Việt hóa dựa trên khóa học <em>Monash EAE Data Analysis in Earth Sciences</em>.</p>
  <a class="hero-cta" href="{{ '/day1.html' | relative_url }}">Bắt đầu bài học đầu tiên →</a>
  <div class="stats"><span>09 bài học</span><span>08 Jupyter Notebook</span><span>Dữ liệu thực hành đi kèm</span></div>
</div>

## Giới thiệu

PyGeo là bản Việt hóa tài liệu hỗ trợ khóa học chuyên sâu kéo dài hai tuần dành cho học viên nghiên cứu của Trường Khoa học Trái Đất, Khí quyển và Môi trường, Đại học Monash. Trọng tâm là các kỹ thuật xử lý, phân tích và trình bày dữ liệu khoa học bằng **Python**.

Khóa học giới thiệu cách nghiên cứu dữ liệu thực tế hoặc dữ liệu do người học thu thập, từ tương quan, hồi quy, phân tích phổ, nội suy và tái lập lưới đến tối ưu hóa và tạo hình minh họa theo tiêu chuẩn công bố khoa học.

## Mục tiêu học tập

Sau khi học, bạn có thể:

- Thiết lập môi trường Python, JupyterLab và những thư viện phân tích dữ liệu cơ bản.
- Đọc và xử lý bảng dữ liệu, GeoTIFF, NetCDF và dữ liệu MATLAB.
- Thực hiện hồi quy, thống kê, phân tích phổ và nội suy dữ liệu một hoặc hai chiều.
- Tạo biểu đồ khoa học có thể tái lập từ dữ liệu và mã nguồn của chính mình.
- Quản lý mã nguồn trên GitHub và công bố phiên bản dữ liệu/mã nguồn với DOI thông qua Zenodo.

Chương trình gốc được tổ chức dưới hình thức 10 buổi hướng dẫn trực tiếp, mỗi buổi khoảng hai giờ. Bản website này cung cấp nội dung cho **9 bài**; nội dung tổng kết buổi thứ 10 được dẫn về [website gốc](https://geomorphlab.github.io/medaes/).

## Lộ trình 9 bài thực hành

<div class="course-grid">
{% for item in site.data.lessons %}
{% unless item.number == "00" %}
<a class="course-card" href="{{ item.url | relative_url }}"><span class="tag">BÀI {{ item.number }}</span><strong>{{ item.title }}</strong><small>Đọc lý thuyết, mở notebook và tải dữ liệu bài thực hành →</small></a>
{% endunless %}
{% endfor %}
</div>

## Sản phẩm cuối khóa

Mỗi bài có bài tập không chấm điểm để người học luyện tập với dữ liệu của mình. Trong khóa học gốc, học viên lấy tín chỉ hoàn thành một bản tóm tắt mở rộng theo [mẫu DOCX](./assets/modified_lpsc_extended_abstract_template.docx), sử dụng hình minh họa tạo từ các kỹ thuật đã học. Mã nguồn và dữ liệu (nếu điều kiện lưu trữ cho phép) được đưa lên GitHub và gắn DOI qua Zenodo.

![Ví dụ hình minh họa khoa học được tạo bằng Python](./assets/example-fig.png)

> **Lưu ý:** Đây là bản Việt hóa **không chính thức** phục vụ học tập và nghiên cứu, không phải website đại diện của Đại học Monash. Giữ nguyên tên hàm, API, định dạng dữ liệu, thuật toán và nguồn học liệu gốc. Các tệp ZIP đi kèm là gói thực hành từ tài liệu gốc; phiên bản notebook tiếng Việt được cung cấp trực tiếp trong các thư mục bài học.

## Thuật ngữ và nguồn tham khảo

- [Bảng thuật ngữ Anh–Việt chuyên ngành](./GLOSSARY_VI.html).
- [Kho mã nguồn PyGeo](https://github.com/xulytiengviet/pygeo).
- [Giáo trình gốc](https://geomorphlab.github.io/medaes/) do [Andrew Gunn](https://www.geomorphlab.org/people#h.bp27h9m9sgu5d) biên soạn.
