---
layout: default
title: "Bài 5 — Nội suy và tái lập lưới"
description: Tái lập lưới một chiều, hai chiều và dữ liệu phân bố không đều.
---

# Bài 5 — Nội suy và tái lập lưới dữ liệu

Dữ liệu đo đạc thường có độ phân giải, hệ lưới hoặc khoảng cách lấy mẫu không giống nhau. Bài này giới thiệu cách **nội suy và tái lập lưới (regridding)** để so sánh hoặc kết hợp các bộ dữ liệu khoa học.

## 1. Tái lập lưới trên tuyến

Chuỗi thời gian, mặt cắt địa hình hoặc tuyến khảo sát có thể được thu thập ở những bước lấy mẫu khác nhau. Ví dụ, hai bộ dữ liệu có độ phân giải khác nhau cần được đưa về những vị trí tương ứng trước khi so sánh trực tiếp.

Chúng ta sử dụng <code>scipy.interpolate</code> để xây dựng tuyến lấy mẫu đều với độ phân giải mong muốn. Notebook cũng hướng dẫn tạo hàm trích xuất tuyến qua dữ liệu không gian hai chiều theo một hướng được chỉ định.

Ví dụ minh họa đơn giản:

~~~python
import numpy as np
from scipy.interpolate import interp1d

x = np.array([0, 2, 5, 9])
z = np.array([1.0, 2.5, 2.0, 4.0])
x_moi = np.linspace(x.min(), x.max(), 50)
noi_suy = interp1d(x, z, kind='linear')
z_moi = noi_suy(x_moi)
~~~

Đối với dữ liệu có khoảng trống, ngoại lệ hoặc độ chính xác vị trí không đồng nhất, cần xem xét xử lý trước khi nội suy.

## 2. Tái lập lưới trên bề mặt

Nguyên tắc tương tự áp dụng cho dữ liệu hai chiều. Chúng ta khai thác [xarray](https://docs.xarray.dev/en/stable/) để đọc và nội suy dữ liệu không gian lưu trong tệp NetCDF (<code>.nc</code>).

Ví dụ, phương thức <code>DataArray.interp</code> cho phép lấy mẫu theo các tọa độ mới khi hệ tọa độ và cấu trúc dữ liệu phù hợp.

~~~python
import xarray as xr

ds = xr.open_dataset('du_lieu.nc')
# Xem Notebook để biết tên tọa độ và cách nội suy của bộ dữ liệu mẫu.
print(ds.coords)
~~~

> **Chú ý:** Tái lập lưới không tự động đồng nghĩa với chuyển đổi hệ quy chiếu. Nếu hai bộ dữ liệu có CRS khác nhau, cần xử lý phép chuyển đổi tọa độ trước hoặc trong quy trình ghép dữ liệu.

## 3. Tái lập lưới dữ liệu phân bố không đều

Trong thực địa hoặc thí nghiệm, chúng ta hiếm khi có thể lấy mẫu hoàn toàn đều theo cả thời gian và không gian. Tuy nhiên, một số kỹ thuật như FFT thường yêu cầu lưới đều.

Notebook sử dụng **phương pháp láng giềng gần nhất (nearest-neighbour)** để chuyển bộ điểm phân bố không đều sang lưới có khoảng cách cố định. Khi chọn phương pháp nội suy, cần cân nhắc mật độ mẫu, độ trơn mong muốn, biên khu vực và mức sai số có thể chấp nhận.

## Notebook thực hành số 5

- [Xem Notebook bài 5](https://github.com/xulytiengviet/pygeo/blob/gh-pages/day5/day5.ipynb).
- [Tải Notebook và dữ liệu thực hành gốc](./day5/day5.zip).

## Bài tập tự luyện

Nạp một bộ dữ liệu của bạn và thử tái lập lưới nếu phù hợp. So sánh kết quả trước và sau nội suy, mô tả phương pháp đã chọn, kích thước ô lưới và giới hạn của kết quả. Nếu chưa có dữ liệu thích hợp, tiếp tục chuẩn bị bài thuyết trình ngắn và bản tóm tắt mở rộng.

---

**Điều hướng:** [← Bài 4](./day4.html) · [Bài 6 — Tối ưu hóa →](./day6.html).
