# VNFaker
VNFaker is a Python package that generates fake data about fullname, address, phone, date_of_birth,... in Viet Nam.

Basic Usage
-----------

Install with pip:

```sh
pip install vnfaker
```
Use ``vnfaker.VNFaker()`` to create and initialize a VNFaker
generator, which can generate data by accessing properties named after
the type of data you want.
```sh
from vnfaker import VNFaker

vnfaker = VNFaker()

vnfaker.fullname()
# Nguyễn Văn Thương
vnfaker.name()
# Thương
vnfaker.date_of_birth(minimum_age=10, maximum_age=30, timestamp=False)
# 1997-02-18
```
Each call to method ``vnfake.fullname()`` yields the same result. If you want different (random) result, you need to initialize a new VNFaker.
```sh
for _ in range(10):
    vnfaker = VNFaker()
    print(vnfaker.fullname())
# Hoàng An Thịnh
# Bạch Cát Mạnh
# Châu Kiệt Thái
# Trần Uy Bửu
# Đặng Thông Trạch
# Bùi Phi Hợp
# Đào Khương Hợp
# Nguyễn Tấn Liêm
# Đặng Lạc Hỷ
# Phạm Yên Hãn
```
License
-------

VNFaker is released under the MIT License. See the bundled [LICENSE](https://github.com/phanducquang/vnfaker/blob/master/LICENSE.txt) file
for details.