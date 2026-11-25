# RULE — PHIẾU GIAO HÀNG NCC

> Loại triển khai: NCC Samsung / Sony / Casper — thiết bị lẻ mua từ nhà cung ứng (NCU) bán lại (TV…). Viết lại theo góc nhìn BA ngày 19/11/2026.
> Nguồn ([`input/`](input/README.md)): URD INSIDE M-Vendor Cooperation V1.1 — **chỉ mục "Quản lý giao hàng"** (Iteration 2: workflow, diễn giải các bước, BR01–BR02, màn hình danh sách phiếu giao hàng) · List HT triển khai · URD Xuất hóa đơn REQ-XHD-043 · thông tin QC cung cấp (BBĐT, tool GH Vendor). Quy tắc chung ở [tổng quan Giao & lắp đặt](../quy-trinh-nghiep-vu.md).
> **⚠ BA** = điểm cần xác nhận, xem §6.

---

## 1. Phạm vi

| Mục | Nội dung |
|---|---|
| Áp dụng | Thiết bị lẻ có hình thức triển khai **NCC Samsung / Sony / Casper** (khai báo trên chính sách bán hàng) |
| Khi nào sinh | Chỉ sau khi đơn **đã thanh toán**, với mọi PTTT ([BR-PTK-03](../quy-trinh-nghiep-vu.md)) |
| Đầu ra | Đơn đặt hàng với NCU (**PO**) + **phiếu giao hàng (PGH)** + mã vận đơn |
| Người giao | Nhà cung ứng (NCU) |
| Hệ thống | **Vendor** — màn hình Quản lý NCU › Giao hàng, triển khai NCU nằm ở **Fox ERP** (QC xác nhận 19/11/2026; URD ghi Inside) — gọi tắt M-Vendor |
| BBĐT | Tự động ký |
| Hoàn tất | Vendor gửi tín hiệu giao hàng hoàn tất về INVOICE ⇒ xuất hóa đơn thiết bị (REQ-XHD-043) |

## 2. Thuật ngữ (URD M-Vendor)

| Thuật ngữ | Ý nghĩa |
|---|---|
| NCU | Nhà cung ứng |
| SO | Đơn mua hàng của khách hàng (đơn FTEL) |
| PO | Đơn đặt hàng với nhà cung ứng |
| PGH | Phiếu giao hàng |
| SPF | Sale Platform |

## 3. Màn hình Quản lý phiếu giao hàng

Menu **Quản lý NCU › Giao hàng, triển khai NCU** có 2 tab: *Quản lý đơn đặt hàng* · **Quản lý phiếu giao hàng**. Mục này chỉ dùng tab Quản lý phiếu giao hàng.

**Danh sách phiếu giao hàng** (có bộ lọc, phân trang) gồm các cột: STT · Nhà cung ứng · **Mã đơn hàng FTEL** (bấm để mở chi tiết) · Mã PO NCU · Mã PGH · Thông tin KH · Ngày tạo · **Tình trạng giao hàng** · Acc tạo.

**Tình trạng giao hàng** (QC xác nhận 19/11/2026 ✅ BA-11): **Chưa giao hàng** → **Đang giao hàng** → **Đã hoàn tất**, hoặc **Đã hủy** (khi chọn Hủy đơn hàng — **chỉ khi phiếu còn Chưa giao hàng**; đã sang Đang giao hàng thì không cập nhật được Đã hủy, QC xác nhận 19/11/2026).

## 4. Quy trình cập nhật tình trạng giao hàng

| # | Bước | Người thực hiện | Kết quả | Điều kiện |
|---|---|---|---|---|
| 1 | Đăng nhập (URD ghi Inside; thực tế **Fox ERP** ✅ BA-14) | User | Hiển thị giao diện | Được cấp tài khoản |
| 2 | Vào menu **Quản lý NCU › Giao hàng, triển khai NCU › QL Giao hàng** | User | Hiển thị tab *Quản lý phiếu giao hàng* | Được cấp quyền vào menu |
| 3 | Bấm **Mã đơn hàng** cần cập nhật tình trạng giao | User | Hiển thị **Chi tiết phiếu giao hàng** | Được cấp quyền cập nhật tình trạng đơn hàng |
| 4 | Bấm **Cập nhật** | User | Popup cập nhật tình trạng, có 3 nút: **Chắc chắn** · **Hủy đơn hàng** · **Đóng** | — |
| 5 | Chọn **Chắc chắn** (cập nhật tình trạng) hoặc **Hủy đơn hàng** | User | Vendor kiểm tra điều kiện cập nhật tình trạng đơn hàng (mục URD không mô tả điều kiện ✅ BA-12). Chuyển **Đang giao hàng** phải nhập **hóa đơn NCU** và **hóa đơn điện tử** ✅ BA-15 | Hóa đơn bắt buộc nhập, **không kiểm tra tồn tại** |
| 6a | Không đạt điều kiện | Vendor | **Thông báo lỗi**, kết thúc | — |
| 6b | Đạt điều kiện | Vendor | Lưu dữ liệu, **thông báo cập nhật thành công** | — |

**Sau khi cập nhật** (theo tổng quan Giao & lắp đặt, không thuộc mục URD này): phiếu **Đã hoàn tất** ⇒ Vendor gửi tín hiệu giao hàng hoàn tất về INVOICE (khóa mã đơn + ServiceCode + SubserviceType + phương thức triển khai) ⇒ xuất hóa đơn thiết bị ⚠ BA-13.

## 5. Quy tắc nghiệp vụ

| Mã | Quy tắc | Nguồn |
|---|---|---|
| BR01 | Danh sách phiếu giao hàng dùng chung cho phiếu của **FPL, SPF, SCM**; bổ sung **kết nối giao hàng đối tác SCM** | URD M-Vendor |
| BR02 | Màn hình chi tiết phiếu giao hàng có **Hủy đơn hàng**: nút "Hủy đơn hàng" trên popup cập nhật tình trạng | URD M-Vendor |
| BR-VD-01 | Chỉ user có quyền vào menu mới xem danh sách; chỉ user có quyền **cập nhật tình trạng đơn hàng** mới mở được chi tiết để cập nhật | URD M-Vendor (điều kiện bước 2, 3) |
| BR-VD-02 | Phiếu giao hàng NCC chỉ sinh sau khi đơn đã thanh toán; BBĐT tự động ký | Thông tin QC cung cấp |
| BR-VD-03 | Chuyển **Đang giao hàng**: bắt buộc user nhập **hóa đơn NCU** và **hóa đơn điện tử**; hệ thống **không kiểm tra tồn tại** của hóa đơn | QC xác nhận 19/11/2026 |
| BR-VD-04 | Tình trạng giao hàng: Chưa giao hàng · Đang giao hàng · Đã hoàn tất · Đã hủy | QC xác nhận 19/11/2026 |
| BR-VD-05 | Chỉ hủy được (→ **Đã hủy**) khi phiếu đang **Chưa giao hàng**; sau khi chuyển **Đang giao hàng** thì không cập nhật được Đã hủy | QC xác nhận 19/11/2026 |

**Thao tác trên STG (thông tin QC cung cấp):** tool QC **GH Vendor** chạy nhanh luồng cập nhật phiếu giao hàng NCU: nhập mã đơn hàng FTEL → tự chuyển **Đang giao hàng** (kèm hóa đơn NCU, hóa đơn điện tử) → **Đã hoàn tất**. Tool đăng nhập **Fox ERP** (đúng nơi có màn hình ✅ BA-14).

## 6. Điểm cần xác nhận với BA / PO

| Mã | Vấn đề | Đề xuất |
|---|---|---|
| BA-11 | Mục Quản lý giao hàng không có danh sách tình trạng giao hàng; 3 tình trạng trên chỉ lấy từ ảnh màn hình mẫu | ✅ Chưa giao hàng · Đang giao hàng · Đã hoàn tất · Đã hủy |
| BA-12 | Bước kiểm tra điều kiện (bước 10 trong URD) không nêu điều kiện là gì; không nói "Chắc chắn" chuyển sang tình trạng nào | ✅ Mục Quản lý giao hàng không mô tả điều kiện ⇒ không cần (theo bạn) |
| BA-13 | Mục không nói khi nào Vendor gửi tín hiệu giao hàng hoàn tất cho INVOICE, cũng không nói Hủy đơn hàng ở đây có báo về SPF không | Xác nhận tín hiệu ra (INVOICE, SPF) khi Đã hoàn tất và khi Hủy đơn hàng |
| BA-14 | URD đặt menu trong **Inside**, tool GH Vendor trên STG lại thao tác trên **Fox ERP** | ✅ Ở **Fox ERP** |
| BA-15 | Tool GH Vendor ghi "Đang giao hàng (**kèm hóa đơn**)": URD mục này không nói gì về hóa đơn NCU | ✅ Hóa đơn **NCU** và **hóa đơn điện tử**, bắt buộc user nhập, không kiểm tra tồn tại |
| BA-10 | BR01 "kết nối giao hàng đối tác SCM" cho thấy **cùng hệ thống Vendor** cũng là nơi kết nối ĐVVC cho phiếu giao tại quầy ([Phiếu giao dịch thiết bị tại quầy](../02-PHIEU-GIAO-DICH-THIET-BI-TAI-QUAY/quy-trinh-nghiep-vu.md)) | 🟡 Bạn trả lời 19/11/2026: **là 1 hệ thống** nhưng chưa chắc chắn — cần xác nhận lại |
