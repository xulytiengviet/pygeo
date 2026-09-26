---
layout: default
title: "Bài 2 — Hàm Python và đọc dữ liệu"
description: Đối số hàm và cách đọc CSV, GeoTIFF, NetCDF, MAT.
---

# Bài 2 — Hàm Python và đọc dữ liệu

Bài này giúp bạn hiểu cách truyền đối số cho hàm Python và nhập các định dạng dữ liệu thường gặp trong nghiên cứu khoa học Trái Đất.

## 1. Hàm trong Python

### Hàm cơ bản

Hàm sau tính tỷ số giữa hai đại lượng:

~~~python
def fluxdirectionality(dp, rdp):
    return rdp / dp
~~~

Hàm nhận hai biến đầu vào và trả về một kết quả. Các thư viện như NumPy cung cấp sẵn rất nhiều hàm có cấu trúc tương tự:

~~~python
import numpy as np
a = [1, 2, 3]
np.sum(a)  # Kết quả: 6
~~~

Dòng đầu nhập thư viện NumPy với bí danh <code>np</code>. Thay vì viết tên đầy đủ, ta gọi hàm bằng cú pháp <code>np.sum</code>.

### Đối số vị trí (positional arguments)

Hai đối số <code>dp</code> và <code>rdp</code> trong hàm <code>fluxdirectionality</code> đều bắt buộc, đồng thời **thứ tự truyền vào có ý nghĩa**. Chúng được gọi là đối số vị trí. Ví dụ, <code>np.sum(a)</code> sử dụng <code>a</code> làm đối số vị trí. Thiếu một đối số bắt buộc sẽ gây lỗi.

### Đối số mặc định (default arguments)

Không phải đối số nào cũng bắt buộc. [Tài liệu hàm <code>numpy.sum</code>](https://numpy.org/doc/stable/reference/generated/numpy.sum.html) cho biết ngoài đối số <code>a</code>, hàm còn có đối số mặc định như <code>axis</code>.

~~~python
a = [[1, 2, 3], [4, 5, 6]]
y1 = np.sum(a)         # 21 — tổng tất cả phần tử
y2 = np.sum(a, axis=0) # [5, 7, 9] — tổng theo trục 0
~~~

Trong ví dụ này, nếu không chỉ định <code>axis</code>, NumPy cộng tất cả giá trị. Khi đặt <code>axis=0</code>, phép cộng được thực hiện theo trục 0. Có thể khai báo rõ tên tham số thay vì phụ thuộc thứ tự, chẳng hạn <code>np.sum(a, dtype=int)</code>.

Ta cũng có thể định nghĩa hàm với đối số mặc định:

~~~python
def cartesian_to_polar(x, y, thetaunit='rad'):
    r = (x**2 + y**2)**0.5
    theta = np.arctan2(y, x)
    if thetaunit == 'rad':
        pass
    elif thetaunit == 'deg':
        theta = theta * 180 / np.pi
    return r, theta
~~~

Nếu không truyền <code>thetaunit</code>, góc được trả về theo radian. Đặt <code>thetaunit='deg'</code> để chuyển sang độ. Ví dụ áp dụng có trong Notebook của bài học.

### Đối số biến thiên

Python còn hỗ trợ <code>*args</code> và <code>**kwargs</code> khi số lượng đối số có thể thay đổi. Khi đọc tài liệu hàm, cần phân biệt các đối số vị trí, đối số có giá trị mặc định và tham số bổ sung. Một ví dụ là [hàm <code>matplotlib.pyplot.scatter</code>](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html), cho phép tùy chỉnh kích thước, màu sắc và cách hiển thị điểm.

## 2. Đọc những định dạng dữ liệu thường gặp

### Bảng tính và CSV

Dữ liệu dạng bảng thường có đuôi <code>.csv</code>, <code>.xlsx</code> hoặc <code>.txt</code>. Thư viện pandas cung cấp <code>read_csv</code> và <code>read_excel</code> để nạp chúng vào DataFrame.

~~~python
import pandas as pd
df = pd.read_csv('du_lieu.csv')
print(df.head())
~~~

Tùy nguồn, cần kiểm tra dấu phân tách, bảng mã UTF-8, tên cột và cách biểu diễn số thập phân.

### GeoTIFF — Dữ liệu raster có tham chiếu không gian

GeoTIFF chứa dữ liệu raster kèm thông tin địa lý như **hệ quy chiếu, phép chiếu, phạm vi không gian và các kênh raster**. Định dạng này thường gặp ở ảnh vệ tinh, mô hình số độ cao (DEM) và bản đồ chuyên đề.

Ta có thể đọc GeoTIFF bằng [GDAL](https://gdal.org/). Cách cài đặt phụ thuộc hệ điều hành và phiên bản GDAL hiện có. Nếu sử dụng Conda, có thể cài bằng:

~~~bash
conda install -c conda-forge gdal
~~~

Sau khi cài đặt, nhập thư viện:

~~~python
from osgeo import gdal
dataset = gdal.Open('du_lieu.tif')
~~~

Nếu cài bằng pip, cần chọn phiên bản gói Python tương thích với thư viện GDAL trên máy. Không nên cố định một phiên bản cũ khi chưa kiểm tra môi trường.

### NetCDF — Dữ liệu khoa học đa chiều

NetCDF có thể chứa dữ liệu không gian, chuỗi thời gian, thông tin nguồn, đơn vị đo và siêu dữ liệu. Định dạng này rất phổ biến trong khí hậu học, hải dương học và mô hình môi trường.

Sử dụng [xarray](https://docs.xarray.dev/en/stable/) cùng công cụ đọc NetCDF:

~~~bash
python -m pip install xarray netCDF4
~~~

~~~python
import xarray as xr
ds = xr.open_dataset('du_lieu.nc')
print(ds)
~~~

xarray cho phép lựa chọn biến, lát cắt thời gian và tọa độ theo cách thuận tiện cho dữ liệu nhiều chiều.

### MAT — Dữ liệu MATLAB

Các tệp <code>.mat</code> thường do MATLAB tạo ra. Với định dạng MAT tương thích, có thể dùng SciPy để đọc:

~~~bash
python -m pip install scipy
~~~

~~~python
from scipy.io import loadmat
data = loadmat('du_lieu.mat')
~~~

**Lưu ý:** Không phải mọi phiên bản MAT đều hỗ trợ trực tiếp trong <code>loadmat</code>; tệp MATLAB v7.3 thường cần thư viện đọc HDF5 như <code>h5py</code>.

## Notebook thực hành số 2

- [Xem Notebook bài 2 trong kho PyGeo](https://github.com/xulytiengviet/pygeo/blob/gh-pages/day2/day2.ipynb).
- [Tải bộ dữ liệu và Notebook gốc](./day2/day2.zip).

Bạn sẽ thử nạp dữ liệu bảng, raster GeoTIFF, NetCDF và MAT, sau đó kiểm tra cấu trúc, kích thước và trực quan hóa dữ liệu.

## Bài tập tự luyện

Dùng ít nhất một bộ dữ liệu của bạn, viết Notebook đọc dữ liệu và tạo biểu đồ hoặc bản đồ đơn giản. Với dữ liệu không gian, hãy ghi rõ hệ quy chiếu, phạm vi và đơn vị đo.

---

**Điều hướng:** [← Bài 1](./day1.html) · [Bài 3 — Hồi quy và thống kê →](./day3.html).
