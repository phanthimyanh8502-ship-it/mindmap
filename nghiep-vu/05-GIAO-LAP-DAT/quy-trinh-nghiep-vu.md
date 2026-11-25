# RULE CHỦ THỂ — GIAO & LẮP ĐẶT

> Tổng quan giao & lắp đặt: các loại phiếu, quy tắc chung, tín hiệu sang xuất hóa đơn. Viết lại theo góc nhìn BA ngày 19/11/2026.
> Nguồn: [`input/`](input/README.md) (List HT triển khai, URD Xuất hóa đơn REQ-XHD-043, thông tin QC cung cấp 04/11 và 17/11/2026).

**Mỗi loại triển khai 1 thư mục** (mỗi thư mục có `input/` và `quy-trinh-nghiep-vu.md` riêng):

| Thư mục | Loại phiếu | Hình thức triển khai | Tool |
|---|---|---|---|
| [`01-PHIEU-THI-CONG`](01-PHIEU-THI-CONG/quy-trinh-nghiep-vu.md) | Phiếu thi công | TIN/PNC, TIN/PNC giao hàng, FTI | SPF Web admin / app MobiX |
| [`02-PHIEU-GIAO-DICH-THIET-BI-TAI-QUAY`](02-PHIEU-GIAO-DICH-THIET-BI-TAI-QUAY/quy-trinh-nghiep-vu.md) | Phiếu giao dịch thiết bị tại quầy (có / không shipper) | Quầy, Sale | QLVT Giao dịch thiết bị · SCM · Vendor vận chuyển |
| [`03-DON-DAT-HANG-VENDOR`](03-DON-DAT-HANG-VENDOR/quy-trinh-nghiep-vu.md) | Phiếu giao hàng NCC | NCC Samsung / Sony / Casper | M-Vendor (Quản lý NCU) |

---

## 1. Phạm vi và các loại phiếu

Giao & lắp đặt là đầu ra của đơn hàng cho phần **thiết bị**. Loại phiếu phụ thuộc **hình thức triển khai** khai báo trên chính sách bán hàng (Tool BP). Hoàn tất phiếu sinh **tín hiệu giao hàng hoàn tất** để INVOICE xuất hóa đơn thiết bị.

| Hình thức triển khai | Áp dụng cho | Loại phiếu | Tool xử lý | Người xử lý | Gửi tín hiệu hoàn tất |
|---|---|---|---|---|---|
| TIN/PNC | Thiết bị cần triển khai, kích hoạt tại địa chỉ | Phiếu thi công, loại **Triển khai** | SPF Web admin / app MobiX | TIN/PNC | Phiếu thi công |
| TIN/PNC giao hàng | Chỉ Camera Offnet, thiết bị lẻ | Phiếu thi công, loại **Giao hàng** | SPF Web admin / app MobiX | TIN/PNC | Phiếu thi công |
| FTI | SPDV đặc thù, dự án (OnCall, Camera B2B, ListLine…) | Phiếu thi công, loại Triển khai | SPF Web admin / app MobiX | Đối tác FTI | Phiếu thi công |
| Quầy (có shipper) | Chỉ Camera Offnet, thiết bị lẻ | **Phiếu giao dịch thiết bị — Giao hàng qua ĐVVC** (= phiếu bán thiết bị) ([thư mục 02](02-PHIEU-GIAO-DICH-THIET-BI-TAI-QUAY/quy-trinh-nghiep-vu.md)) | QLVT (Giao dịch thiết bị) + SCM + Vendor vận chuyển | Thủ kho | Phiếu giao tại quầy |
| Quầy (không shipper), Sale | Camera Offnet, thiết bị lẻ (Sale: thiết bị lẻ quản lý MAC) | Phiếu giao dịch thiết bị tại quầy ([thư mục 02](02-PHIEU-GIAO-DICH-THIET-BI-TAI-QUAY/quy-trinh-nghiep-vu.md)) | Tool quầy (Giao dịch thiết bị) | DVKH CN / nhân viên bán hàng | Phiếu giao tại quầy |
| NCC Samsung / Sony / Casper | Thiết bị lẻ mua từ NCC bán lại (TV…) | Phiếu giao hàng NCC ([thư mục 03](03-DON-DAT-HANG-VENDOR/quy-trinh-nghiep-vu.md)) | M-Vendor | Nhà cung cấp | Vendor |
| Không / None | Dịch vụ không cần triển khai (vd Code SA) | Không có phiếu | — | — | Qua phiếu quầy; quầy không gửi thì không xuất hóa đơn |

## 2. Quy tắc chung

| Mã | Quy tắc | Nguồn |
|---|---|---|
| BR-PTK-01 | Đơn có ≥1 SPDV hình thức TIN/PNC trộn với Quầy/Sale ⇒ **cả đơn** đi luồng TIN/PNC (thiết bị giao tại quầy cũng chờ phiếu thi công). Trộn "Không" + TIN/PNC ⇒ theo phiếu thi công | List HT triển khai, REQ-XHD-043 |
| BR-PTK-02 | **Phiếu thi công** sinh ngay sau khi tạo đơn khi PTTT = Thanh toán khi triển khai (không chờ thanh toán); PTTT Online ⇒ sau khi khách thanh toán (Desktop/Mobile) hoặc ngay khi tạo đơn đã thanh toán (DKOL) | Thông tin QC cung cấp |
| BR-PTK-03 | **Phiếu giao dịch thiết bị (quầy) và phiếu giao hàng NCC chỉ sinh sau khi đơn đã thanh toán**, với mọi PTTT. Ngoại lệ: **đơn sàn TMĐT** tạo phiếu giao **ngay sau khi tạo đơn hàng** (QC xác nhận 19/11/2026) | Thông tin QC cung cấp · [URD B1] trigger "Đơn hàng thanh toán thành công" |
| BR-PTK-04 | Mỗi loại phiếu hoàn tất trên **tool của phiếu đó**: phiếu thi công trên SPF Web admin / MobiX; phiếu giao tại quầy trên Tool quầy / QLVT; phiếu giao hàng NCC trên M-Vendor | Thông tin QC cung cấp 17/11/2026 |
| BR-PTK-05 | Hoàn tất PTC **không** còn điều kiện "đã ký BBĐT + khoản thu đã thanh toán" (bỏ rule cũ) | Thông tin QC cung cấp 17/11/2026 |
| BR-PTK-06 | Tín hiệu giao hàng hoàn tất đi thẳng về INVOICE, map theo khóa **mã đơn + ServiceCode + SubserviceType + phương thức triển khai**; chỉ xuất hóa đơn thiết bị có trong tín hiệu | URD XHD BR-DB-02, BR-DB-07 |
| BR-PTK-07 | Luồng **không bán Smart TV** ⇒ **không có nhánh Vendor** (vd DKOL F-citizen, AM, Tri ân CAND) | Thông tin QC cung cấp 23/11/2026 |
| BR-PTK-08 | Bán **combo Internet–truyền hình, Triple Internet–truyền hình–Camera** ⇒ **chỉ có phiếu thi công (TIN/PNC)**: không có Vendor, phiếu giao tại quầy, không phiếu (vd DKOL Tri ân CAND) | Thông tin QC cung cấp 23/11/2026 |

---

## 7. Hoàn tất phiếu → xuất hóa đơn thiết bị

| Hình thức triển khai | Nguồn tín hiệu giao hàng hoàn tất (REQ-XHD-043) |
|---|---|
| TIN/PNC, TIN/PNC giao hàng, FTI | Phiếu thi công ("Đã xử lý hoàn tất") |
| NCC Samsung / Sony / Casper | Vendor |
| Quầy, Sale (kể cả giao qua ĐVVC) | Phiếu giao tại quầy |
| Không / None | Qua phiếu quầy; quầy không gửi thì không xuất hóa đơn |
