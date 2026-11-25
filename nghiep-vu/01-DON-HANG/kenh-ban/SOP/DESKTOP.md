# KÊNH DESKTOP (SaleChannelID 2)

> Tách từ `RULE-CHINH-SACH-KENH-BAN.md` (nguồn: QC cung cấp 03/11/2026). Rule chung: [00-CHUNG.md](../00-CHUNG.md) · Rule XHD: [`../../../../RULE-XHD.md`](../../../../RULE-XHD.md).

## Thông tin chung

| Mục | Nội dung |
|---|---|
| Owner | KhiemBT |
| Nơi tạo đơn | Web SOP — https://portal-sop-stg.fpt.vn/user/login/basic-auth |
| Loại đơn | Bán mới + bán thêm |

## Dịch vụ (19)
Internet, FPT Camera Only, FPT Camera Combo, FPT Play Stands Alone, Sản phẩm khác, FPT Play, Tổng đài Oncall, FPT Smart Home, Ultra Fast Stand Alone, FPro, FSafe Go, VioEdu Stand Alone, VIP 247, SIM data, Pay Wifi, Ultra Fast, FPT Camera B2B, HyperFast, FPT AI Wi-Fi

## Cách tạo đơn
1. Chọn **Thêm khách hàng**.
2. Nhập thông tin đầy đủ.
3. Chọn **Tạo và lên đơn** → bấm **Xác nhận**.
4. Lựa chọn đơn bán thêm / bán mới.
5. Chọn menu **Đơn hàng**.
6. Tại tab bán thêm / bán mới chọn dấu **+**.

### Bán mới
1. Chọn **+** ở bán mới
2. Nhấn icon tìm kiếm ở thông tin địa chỉ
3. Chọn/nhập địa chỉ
4. Nhấn **Xác nhận**
5. Chọn đối tượng khách hàng (nếu muốn thay đổi)
6. Chọn dịch vụ cần mua
7. Nhấn **Chi tiết giỏ hàng** → chọn **Xác nhận**
8. Cập nhật thông tin khách hàng
9. Chọn **Tạo báo giá**
10. Chọn **Tạo hợp đồng**
11. Có thể cập nhật hợp đồng nếu muốn

### Bán thêm (nguồn: QC cung cấp 20/11/2026)
Bán thêm **không qua báo giá**.
1. Chọn **+** ở bán thêm
2. Tìm kiếm hợp đồng → chọn HĐ bán thêm
3. Nhấn icon **+**
4. Chọn dịch vụ cần mua
5. Sang màn hình **Tạo đơn** — có sẵn **số hợp đồng**
6. Nhấn **Tạo đơn hàng** ⇒ hệ thống tạo đơn hàng, chuyển sang màn hình **Chi tiết đơn hàng**
7. Cập nhật đơn hàng (nếu có)
8. Nhấn **Gen BBĐT/PLHD** ⇒ gen xong mới có **khoản thu** và **BBĐT**

Giao & lắp đặt của đơn bán thêm (theo PTTT — QC cung cấp 20/11/2026):
- **Thanh toán khi triển khai:** Gen BBĐT/PLHD xong **luôn có phiếu thi công**, không chờ ký BBĐT hay thanh toán.
- **Online:** **ký BBĐT** ⇒ khách **thanh toán** xong ⇒ mới gen phiếu theo hình thức triển khai.
- Phần sau (hoàn tất phiếu, hóa đơn, gạch nợ theo cọc, add tiền trả trước) **giống bán mới**.

## Hình thức triển khai
Theo chính sách khai báo trên tool BP — xem bảng [00-CHUNG.md §2](../00-CHUNG.md#2-quy-tắc-hình-thức-triển-khai-thiết-bị). Cách hoàn tất phiếu: [00-CHUNG.md §5](../00-CHUNG.md#5-cách-hoàn-tất-phiếu-giao-hàng--triển-khai-stg).

## Thanh toán & khoản thu
- **PTTT = Thanh toán khi triển khai:** gen đồng thời khoản thu, phiếu thi công, biên bản điện tử; đơn = **Chưa thanh toán**.
- **PTTT Online:** tạo báo giá (có mã đơn, **Chưa thanh toán**) ⇒ bấm **Tạo hợp đồng** mới có khoản thu **Chưa thanh toán** và **biên bản điện tử** (chưa thanh toán đã có BBĐT — QC xác nhận 19/11/2026) ⇒ khách thanh toán xong ⇒ mới gen **phiếu thi công**.
- Sau khi thanh toán: khoản thu **Đã thanh toán**, tiền **đẩy vào cọc**. Kiểm tra: Inside › Foxpay › Thanh toán online › Đối soát khoản thu online.
- **Thanh toán → cọc → hóa đơn → gạch nợ** (nguồn: QC cung cấp 17/11/2026): giống DKOL — khoản thu **Đã thanh toán** ⇒ **nhập cọc** ⇒ nhận tín hiệu thì xuất hóa đơn ⇒ có cọc thì **gạch nợ**, hóa đơn **Đã thanh toán** ⇒ dịch vụ **trả trước** thì **add tiền trả trước**. Chi tiết: [00-CHUNG.md §4.3](../00-CHUNG.md#43-sau-khi-thanh-toán-khoản-thu).

## Phạm vi test XHD
Bán mới + bán thêm, 19 nhóm (trừ nhóm 25 Prepaid 3) — `RULE-XHD.md` §1.1.

## Báo giá
PTTT chọn trước khi bấm Tạo báo giá (QC xác nhận 19/11/2026). Bấm **Tạo báo giá** là có mã đơn hàng; phải bấm **Tạo hợp đồng** mới có hợp đồng (và khoản thu với PTTT Online) — QC xác nhận 19/11/2026. Quy trình tổng quan: [`../quy-trinh-nghiep-vu.md`](../../quy-trinh-nghiep-vu.md) mục Báo giá SOP (nguồn URD Báo giá v1.0).
