---
layout: default
title: "Bài 9 — GitHub, Zenodo và DOI"
description: Quản lý phiên bản và công bố mã nguồn, dữ liệu nghiên cứu có DOI.
---

# Bài 9 — Công bố mã nguồn và dữ liệu có DOI

Sau khi hoàn thiện quy trình phân tích, chúng ta học cách lưu trữ mã nguồn, quản lý phiên bản và cấp **mã định danh đối tượng số (DOI)** để người khác có thể truy cập, kiểm tra và trích dẫn kết quả nghiên cứu.

## 1. Git và GitHub

[GitHub](https://github.com/) là nền tảng lưu trữ kho mã nguồn và cộng tác phát triển. Các dự án được tổ chức thành **repository**, có thể công khai hoặc riêng tư. GitHub xây dựng trên [Git](https://git-scm.com/), hệ thống quản lý phiên bản ghi nhận thay đổi của tệp và thư mục.

Trong buổi học này, chúng ta sẽ:

1. Tập hợp mã nguồn, dữ liệu đầu vào, môi trường và hình đầu ra của một dự án trong cấu trúc thư mục có thể tái lập.
2. Thiết lập Git trên máy tính và tạo kho mã nguồn trên GitHub.
3. Ghi nhận những phiên bản ổn định của dự án bằng commit và release.
4. Liên kết bản phát hành với Zenodo để lưu trữ lâu dài và cấp DOI.

### Tổ chức dự án trước khi công bố

Gợi ý cấu trúc thư mục:

~~~text
du-an-nghien-cuu/
├── README.md
├── requirements.txt
├── notebooks/
├── src/
├── data/
└── figures/
~~~

Tệp <code>README.md</code> nên trình bày nguồn dữ liệu, cách cài đặt, thứ tự chạy chương trình và kết quả mong đợi. Tài liệu môi trường như <code>requirements.txt</code> giúp tái lập phiên bản thư viện.

Với bộ dữ liệu lớn, cần kiểm tra giới hạn lưu trữ của GitHub; xem xét Git LFS hoặc kho lưu trữ dữ liệu chuyên dụng thay vì đẩy toàn bộ tệp lớn vào lịch sử Git. Không đưa thông tin cá nhân nhạy cảm, mật khẩu hoặc khóa API vào kho công khai.

### Cài đặt và đẩy dự án lên GitHub

- [Cài đặt Git](https://github.com/git-guides/install-git).
- [Tạo tài khoản GitHub](https://github.com/signup).
- [Hướng dẫn thêm dự án có sẵn lên GitHub](https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-locally-hosted-code-to-github#adding-a-local-repository-to-github-using-git).

Từ thư mục dự án, có thể bắt đầu như sau:

~~~bash
git init
git add .
git commit -m "Initial research release"
~~~

Tiếp tục thiết lập kho từ xa và đẩy nhánh theo hướng dẫn GitHub. Trước khi chạy <code>git add .</code>, nhớ kiểm tra <code>.gitignore</code> để loại bỏ tệp tạm và dữ liệu không được phép chia sẻ.

## 2. Zenodo và mã DOI

[Zenodo](https://zenodo.org/) là kho lưu trữ mở dành cho dữ liệu, phần mềm và sản phẩm nghiên cứu. Zenodo có khả năng cấp **DOI** cho các bản ghi hoặc phiên bản đã xuất bản.

[DOI](https://www.doi.org/) là mã định danh bền vững giúp tìm, trích dẫn và truy vết phiên bản của tài liệu số. Công bố mã nguồn và dữ liệu với DOI hỗ trợ minh bạch quy trình nghiên cứu và cho phép người khác trích dẫn chính xác tài nguyên đã sử dụng.

### Liên kết GitHub với Zenodo

Khi dự án đã có phiên bản ổn định trên GitHub:

1. Chuẩn bị README, hướng dẫn tái lập kết quả, thông tin tác giả và quyền sử dụng phù hợp.
2. Đăng nhập Zenodo và bật liên kết tới kho GitHub (nếu sử dụng cơ chế tích hợp).
3. Tạo **GitHub Release** cho phiên bản muốn lưu trữ.
4. Kiểm tra bản ghi được Zenodo tiếp nhận, hoàn thiện siêu dữ liệu rồi công bố.
5. Ghi DOI vào README, báo cáo hoặc bài báo nghiên cứu.

Xem [tài liệu GitHub về trích dẫn nội dung của kho](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content). Cơ chế liên kết, cấp DOI và quy trình xuất bản có thể thay đổi; hãy đối chiếu tài liệu chính thức tại thời điểm thực hiện.

> **Lưu ý về bản quyền và dữ liệu:** Chỉ công bố dữ liệu mà bạn được phép chia sẻ. Với dữ liệu hạn chế truy cập, có thể công bố mã nguồn, siêu dữ liệu hoặc bộ dữ liệu thay thế phù hợp.

## Bài tập tổng kết

Hoàn thiện dự án của bạn, tạo một kho GitHub với hướng dẫn chạy lại phân tích, phát hành phiên bản chính thức và đăng ký DOI thông qua Zenodo. Hoàn thiện bài thuyết trình ngắn và bản tóm tắt mở rộng có hình minh họa tạo bằng Python.

---

**Điều hướng:** [← Bài 8](./day8.html) · [Tổng kết khóa học tại nguồn gốc ↗](https://geomorphlab.github.io/medaes/).
