# RULE — PHIẾU GIAO DỊCH THIẾT BỊ TẠI QUẦY

> Loại triển khai: Quầy (có shipper giao qua ĐVVC hoặc khách nhận tại quầy), Sale. Viết lại theo góc nhìn BA ngày 19/11/2026.
> Nguồn ([`input/`](input/README.md)): URD Resource Equipment v2.2 — **chỉ mục "Quy trình giao hàng qua đơn vị vận chuyển"** (bảng B1–B11 + sơ đồ) · thông tin QC cung cấp 04/11/2026 (thao tác STG). Quy tắc chung ở [tổng quan Giao & lắp đặt](../quy-trinh-nghiep-vu.md).
> Ký hiệu: **[URD B*n*]** = bước trong bảng quy trình của URD · **⚠ BA** = điểm cần xác nhận, xem §3 · **✅ BA-n** = bạn đã xác nhận ngày 19/11/2026.
> **Phiếu giao tại quầy của đơn SPF là "phiếu bán thiết bị"** trong Tool quầy (URD Retail-Counter) — QC xác nhận 19/11/2026.

---

## 1. Phiếu giao dịch thiết bị — Giao hàng qua đơn vị vận chuyển (ĐVVC)

> Nguồn: URD Resource Equipment v2.2, mục "Quy trình giao hàng qua đơn vị vận chuyển" (bảng B1–B11 và sơ đồ).

### 1.1 Thuật ngữ

| Thuật ngữ | Ý nghĩa |
|---|---|
| Phiếu giao | Phiếu giao dịch thiết bị loại **Giao hàng**: cập nhật thông tin đóng hàng từ FTEL |
| Phiếu xuất | Gắn với phiếu tạm ứng vật tư, để tạm ứng và xuất vật tư từ kho tổng giao cho khách |
| ĐVVC | Đơn vị vận chuyển (GHTK, Ahamove…) |
| Vendor (vận chuyển) | Hệ thống trung gian kết nối ĐVVC: tạo vận đơn, tracking, đối soát. Theo bạn (19/11/2026) là **cùng hệ thống Vendor** với [Phiếu giao hàng NCC](../03-DON-DAT-HANG-VENDOR/quy-trinh-nghiep-vu.md) nhưng chưa chắc chắn, xem BA-10 |
| Mã vận đơn | Mã giao dịch vận chuyển do hệ thống ĐVVC sinh ra |
| Phát lại | ĐVVC đã lấy hàng chưa giao, hoặc giao không thành công đã hoàn về kho, nhưng khách vẫn cần ⇒ giao lại |
| Hoàn hàng | ĐVVC đã lấy hàng nhưng không giao được, trả hàng về FTEL |
| Bồi thường | ĐVVC làm mất hàng, phát sinh nghĩa vụ bồi thường |
| Thanh lý TSD | Hủy đơn qua NOK V3 / SR (cả đơn hoặc 1 phần) |

### 1.2 Tác nhân và hệ thống

| Hệ thống | Tác nhân | Vai trò trong quy trình |
|---|---|---|
| SPF | Sale / kênh bán | Tạo đơn bán thiết bị giao qua shipper, đơn thanh toán thành công; xử lý hủy đơn |
| QLVT — Giao dịch thiết bị (GDTB) | System, Thủ kho | Tạo và xử lý phiếu giao; nhận trạng thái vận chuyển; hoàn ứng |
| Quản lý vật tư quầy | Thủ kho, System | Tạm ứng, hoàn ứng / nhập trả vật tư quầy |
| SCM (FTELSCM) | Thủ kho, System | Xác nhận tạm ứng, xuất vật tư theo MAC; nhận nhập trả |
| Vendor vận chuyển | System, FAF | Tạo vận đơn, kết nối ĐVVC, SMS/ZNS cho khách, tracking, đối soát |
| ĐVVC | — | Lấy hàng, giao hàng, hoàn hàng, bồi thường |
| Bill (INVOICE) | System | Xuất hóa đơn thiết bị |
| QLVT | FAF | Tổng hợp chi phí (hạch toán) |
| TL TSD (NOK V3 / SR) | DVKH | Hủy đơn hàng |

**Chuỗi theo sơ đồ URD** (mindmap vẽ 14 bước này; riêng **Hủy đơn hàng** vẽ thành nhánh ngoại lệ — hủy vận đơn, nhập trả vật tư về SCM, không đi tới Xuất hóa đơn — theo bảng B10, 19/11/2026): Tạo đơn, thanh toán (SPF) → Tạo phiếu GDTB (System) → Xử lý thông tin giao hàng (Thủ kho) → Xử lý hàng hóa, khai tiền bồi thường (Thủ kho) → Xuất hàng (SCM) → Đóng hàng (Thủ kho) → Tạo vận đơn, tracking (Vendor) → Map trạng thái vận đơn (GDTB) → Hoàn ứng / nhập vật tư (QL vật tư quầy, SCM) → Hủy đơn (TL TSD, DVKH) → Xuất hóa đơn (Bill) → Tổng hợp chi phí (QLVT, FAF) → Collect data, đối soát ĐVVC (Vendor).

### 1.3 Tiền điều kiện
- Chính sách bán hàng khai báo hình thức triển khai **Quầy — chính sách shipper giao hàng** cho thiết bị (Camera Offnet, thiết bị lẻ).
- Đơn **không** có SPDV TIN/PNC ([BR-PTK-01](../quy-trinh-nghiep-vu.md)).
- Đơn đã **thanh toán thành công** ([BR-PTK-03](../quy-trinh-nghiep-vu.md)). Riêng **đơn sàn TMĐT (Shopee, TikTok)**: phiếu giao tạo **ngay sau khi tạo đơn hàng** ✅ BA-8.
- Thiết bị trên đơn cần giao và có **vật tư chính**.

### 1.4 Luồng chính

| # | Bước | Tác nhân · hệ thống | Mô tả | Điều kiện | Kết quả · trạng thái phiếu |
|---|---|---|---|---|---|
| 1 | Tạo phiếu giao [URD B1] | System · SPF → QLVT | SPF có đơn bán thiết bị giao qua shipper đã thanh toán (đơn TMĐT: ngay sau khi tạo đơn ✅ BA-8) ⇒ QLVT tạo phiếu GDTB loại hỗ trợ **Giao hàng**; tự đẩy **vật tư phụ** đi kèm vật tư chính vào phiếu; gửi **email** cho thủ kho của khu vực | Đơn đã thanh toán (TMĐT: đã tạo đơn) · có vật tư chính | Phiếu giao, trạng thái **1. Chờ xác nhận** ✅ BA-2 |
| 2 | Xử lý thông tin giao hàng [URD B2] | Thủ kho · QLVT | Mở chi tiết phiếu: chọn **kho** (trong danh sách được phân quyền); người gửi mặc định *Công ty Cổ phần Viễn thông FPT (FPT Telecom)*; nhập **SĐT** (kiểm tra đúng định dạng), **địa chỉ lấy hàng**, ghi chú giao hàng | Kho thủ kho được phân quyền · đã nhập người gửi, địa chỉ | **2. Đang xử lý** · hiện nút "Đề nghị xuất kho giao hàng" |
| 3 | Xử lý hàng hóa [URD B3] | Thủ kho · QLVT → SCM | Bấm "Đề nghị xuất kho giao hàng" ⇒ tạo **đề nghị tạm ứng** sang SCM (SL đề nghị = SL vật tư trên phiếu; kho tạm ứng = kho chọn trên phiếu) ⇒ thủ kho **xác nhận xuất vật tư theo MAC và SL** trên SCM ⇒ QLVT ghi nhận vật tư, MAC đã xuất. QLVT so vật tư đã xuất với phiếu: **chưa khớp** ⇒ tự tạo đề nghị xuất phần còn thiếu; **khớp** ⇒ khóa nút đề nghị xuất | Thủ kho có quyền xác nhận tạm ứng trên SCM | Tạm ứng **đủ** vật tư trên phiếu |
| 4 | Khai báo tiền bồi thường [URD B4] | Thủ kho · QLVT | Khai báo tiền bồi thường hàng hóa nếu thất thoát | Chưa khai báo | Tiền bồi thường hiển thị trên phiếu |
| 5 | Đóng hàng [URD B5] | Thủ kho · QLVT | Chọn **đối tác vận chuyển** (trong danh sách ĐVVC), nhập **số lượng, trọng lượng** kiện, chọn **loại hình vận chuyển XFast / Express**. Đủ trường bắt buộc ⇒ mở nút "Đã đóng hàng hoàn tất" | Đã khai báo bồi thường · đủ trường bắt buộc | Hiện nút **Đã đóng hàng hoàn tất** |
| 6 | Tạo vận đơn [URD B6] | Thủ kho · QLVT → Vendor | Thủ kho bấm **Đã đóng hàng hoàn tất** ⇒ Vendor tạo **vận đơn** từ phiếu và kết nối ĐVVC ⇒ trả kết quả cho QLVT ⇒ gửi **SMS/ZNS** cho khách ⇒ QLVT mở chức năng **In vận đơn** ⇒ Vendor tracking tiến độ giao | Đủ thông tin vận đơn · kết nối ĐVVC thành công | **3. Đã đóng hàng hoàn tất** · có mã vận đơn |
| 7 | Cập nhật trạng thái giao [URD B7] | System · ĐVVC → Vendor → QLVT | ĐVVC đổi trạng thái ⇒ QLVT tự nhận qua Vendor ⇒ thông báo cho thủ kho và vận hành kênh bán / sale | Có thay đổi trạng thái | Trạng thái 4 → 9 theo thực tế (§1.6) |
| 8 | Giao thành công, hoàn ứng [URD B8] | System · QLVT, QL vật tư quầy, SCM | ĐVVC báo **giao hàng thành công** ⇒ QLVT chuyển phiếu sang **Giao hàng thành công** ✅ BA-1 ⇒ **hoàn ứng tự động** thiết bị của phiếu ⇒ bắn tín hiệu cho **SPF ghi nhận đơn hàng đã hoàn tất** (mọi đơn) ✅ BA-6 ⇒ bắn **MAC** sang **SM** nếu dịch vụ là **FPT Camera Combo** (kích hoạt trên App Camera) ⇒ đẩy thông tin vào **hạch toán chi phí** | Giao thành công | **Giao hàng thành công** · thiết bị đã hoàn ứng · SPF ghi nhận đơn hoàn tất → xuất hóa đơn thiết bị (Bill) |
| 9 | Đối soát ĐVVC [URD B11] | System, FAF · Vendor | Vendor gom vào trạng thái **Chờ đối soát**: đơn đã giao thành công; đơn ĐVVC đã lấy hàng / giao không thành công, có yêu cầu hủy giao và **đã hoàn hàng**. Đơn có phát lại tính theo **từng mã vận đơn**. Người dùng Vendor xác nhận đối soát | Đơn thỏa điều kiện đối soát | Đối soát và thanh toán ĐVVC hoàn tất |

### 1.5 Luồng thay thế và ngoại lệ

**A. Gỡ vật tư đã xuất** [URD B3] — chỉ khi phiếu **2. Đang xử lý**: tạo đề nghị nhập trả theo chủng loại, thiết bị đã gỡ ⇒ trả vật tư khả dụng về kho SCM.

**B. Hủy giao hàng** [URD B9] — thủ kho bấm "Hủy giao hàng":

| Trường hợp | Áp dụng khi phiếu ở trạng thái | Hệ thống xử lý | Trạng thái sau | Vật tư về |
|---|---|---|---|---|
| TH1 — hàng chưa rời kho | 4. ĐVVC chưa tiếp nhận · 5. ĐVVC đã tiếp nhận · 6. ĐVVC đang lấy hàng · 8. Lấy hàng không thành công | Vendor gửi hủy giao cho ĐVVC và **hủy mã vận đơn** | **13. Hủy giao hàng** | Kho tạm |
| TH2 — hàng đã ở ĐVVC | 7. ĐVVC đã lấy hàng · 9. ĐVVC đang giao hàng · 11. Giao không thành công | Vendor gửi hủy giao, yêu cầu ĐVVC **thu hồi hàng về FTEL**, không phát cho khách | **11. Giao không thành công** → khi Vendor nhận "Đã đối soát trả hàng" ⇒ **12. Đã hoàn hàng** ⇒ tự đề nghị nhập trả ⇒ thủ kho xác nhận nhập trả | Kho tổng |

**C. Cập nhật phiếu giao** [URD B9] — áp dụng khi phiếu **12. Đã hoàn hàng / 13. Hủy giao hàng / 16. ĐVVC bồi thường hàng hóa** **và** **trạng thái đơn hàng** = **BÌNH THƯỜNG** ✅ BA-9: xuất vật tư mới thay vật tư trên phiếu ⇒ xác nhận cập nhật (kiểm tra rule như luồng chính) ⇒ lưu thông tin cập nhật cuối của thủ kho.

**D. Phát lại hàng hóa** [URD B9] — áp dụng khi phiếu **12. Đã hoàn hàng / 13. Hủy giao hàng** **và** trạng thái đơn hàng **BÌNH THƯỜNG**: đẩy yêu cầu mới sang ĐVVC như từ bước 6 ⇒ **tạo vận đơn mới**. Phải **nhập trả hoàn tất** mới được đề nghị vật tư tiếp lên phiếu.

**E. ĐVVC bồi thường** — phiếu ở **16. ĐVVC bồi thường hàng hóa**: được cập nhật phiếu (C) hoặc thanh lý (F). Mục quy trình của URD không nói tiền bồi thường khai báo ở bước 4 được dùng thế nào khi ĐVVC bồi thường.

**F. Hủy đơn hàng — Thanh lý TSD cả đơn** [URD B10] (NOK V3 / SR; SPF xử lý hủy đơn và gửi tín hiệu sang phiếu giao):

| Trường hợp | Trạng thái phiếu lúc hủy | Xử lý |
|---|---|---|
| TH1 | 1. Chờ xác nhận · 2. Đang xử lý | Phiếu → **Đơn hàng đã hủy** (chỉ xem, không cập nhật) |
| TH2 | 3. Đã đóng hàng hoàn tất · 4 · 5 · 6 · 8 · 13 | Vendor **hủy vận đơn** ⇒ phiếu → Đơn hàng đã hủy ⇒ **tự tạo và tự xác nhận nhập trả** vật tư về kho SCM |
| TH3 | 7. ĐVVC đã lấy hàng | Vendor hủy vận đơn, yêu cầu ĐVVC **thu hồi hàng về FTEL**, về **kho đã chọn lúc xác nhận** xuất hàng ✅ BA-5 (không giao cho khách) ⇒ phiếu → Đơn hàng đã hủy |
| TH4 | 11. Giao không thành công · 12. Đã hoàn hàng · 13. Hủy giao hàng | Phiếu → Đơn hàng đã hủy |
| Bồi thường | 16. ĐVVC bồi thường hàng hóa | Phiếu → Đơn hàng đã hủy |

Nhập trả tự động về kho SCM (tài khoản nhập trả là thủ kho, tồn cộng lại kho tổng) khi phiếu → **Đơn hàng đã hủy** và trạng thái liền trước là: Đã hoàn hàng, Đã đóng hàng hoàn tất, ĐVVC chưa tiếp nhận, ĐVVC đã tiếp nhận, ĐVVC đang lấy hàng, Lấy hàng không thành công.

**G. Hủy 1 phần đơn hàng** [URD B10] — chỉ khi phiếu **1. Chờ xác nhận / 2. Đang xử lý / 12. Đã hoàn hàng**; SPF gửi tín hiệu hủy 1 phần và thành phần hủy:
- **Chưa xuất vật tư:** đề nghị tạm ứng ghi nhận SL, chủng loại **sau khi trừ phần đã hủy**.
- **Đã xuất vật tư:** thủ kho **nhập trả phần đã hủy** trước; khi xác nhận Phát lại / Đóng hàng hoàn tất, hệ thống kiểm tra SL đã xuất khớp SL đơn sau điều chỉnh.

### 1.6 Trạng thái phiếu giao

Số thứ tự lấy theo cách URD đánh số trong bảng quy trình. URD **không có** trạng thái số 10, 14, 15 — giữ đúng URD ✅ BA-3:

| # | Trạng thái | Do ai chuyển |
|---|---|---|
| 1 | Chờ xác nhận ✅ BA-2 | System khi tạo phiếu |
| 2 | Đang xử lý | Thủ kho cập nhật thông tin giao hàng |
| 3 | Đã đóng hàng hoàn tất | Thủ kho |
| 4 | ĐVVC chưa tiếp nhận | ĐVVC (qua Vendor) |
| 5 | ĐVVC đã tiếp nhận | ĐVVC |
| 6 | ĐVVC đang lấy hàng | ĐVVC |
| 7 | ĐVVC đã lấy hàng | ĐVVC |
| 8 | Lấy hàng không thành công | ĐVVC |
| 9 | ĐVVC đang giao hàng | ĐVVC |
| 11 | Giao không thành công (cũng là "Giao hàng không thành công" khi thủ kho hủy giao TH2) ✅ BA-4 | ĐVVC · QLVT khi hủy giao TH2 |
| 12 | Đã hoàn hàng | Vendor nhận "Đã đối soát trả hàng" |
| 13 | Hủy giao hàng | Thủ kho (TH1) |
| 16 | ĐVVC bồi thường hàng hóa | ĐVVC |
| — | Giao hàng thành công ✅ BA-1 | QLVT khi ĐVVC báo giao thành công (B8) |
| — | Đơn hàng đã hủy | QLVT khi SPF hủy đơn |

### 1.7 Quy tắc nghiệp vụ

| Mã | Quy tắc |
|---|---|
| BR-GH-01 | Phiếu giao chỉ tạo khi đơn **đã thanh toán** (đơn TMĐT: ngay sau khi tạo đơn) và có **vật tư chính**; vật tư phụ tự đẩy theo vật tư chính |
| BR-GH-02 | **1 phiếu giao — 1 ĐVVC** |
| BR-GH-03 | Thủ kho chỉ chọn kho trong danh sách được phân quyền; SĐT người gửi phải đúng định dạng |
| BR-GH-04 | SL đề nghị tạm ứng = SL vật tư trên phiếu; chỉ đóng hàng khi đã xuất **đủ và khớp** (theo MAC) |
| BR-GH-05 | Chỉ gỡ vật tư đã xuất khi phiếu **Đang xử lý** |
| BR-GH-06 | Phải khai báo **tiền bồi thường** trước khi đóng hàng |
| BR-GH-07 | Loại hình vận chuyển: XFast hoặc Express; bắt buộc số lượng, trọng lượng kiện |
| BR-GH-08 | Tạo vận đơn thành công thì Vendor gửi SMS/ZNS cho khách và QLVT cho in vận đơn |
| BR-GH-09 | Mọi thay đổi trạng thái từ ĐVVC đều báo cho thủ kho và vận hành kênh bán / sale |
| BR-GH-10 | Cập nhật phiếu / phát lại chỉ khi **trạng thái đơn hàng** = **BÌNH THƯỜNG** ✅ BA-9; phát lại phải nhập trả xong mới đề nghị vật tư tiếp |
| BR-GH-11 | Hủy giao trước khi ĐVVC lấy hàng ⇒ vật tư về **kho tạm**; sau khi đã lấy hàng ⇒ thu hồi về **kho tổng** |
| BR-GH-12 | Phiếu "Đơn hàng đã hủy" chỉ xem, không cập nhật |
| BR-GH-13 | Đối soát ĐVVC tính theo **từng mã vận đơn** (đơn phát lại có nhiều mã) |

### 1.8 Tín hiệu sang hệ thống khác

| Thời điểm | Gửi tới | Nội dung |
|---|---|---|
| Có phiếu giao mới | Thủ kho khu vực | Email thông báo |
| Tạo vận đơn xong | Khách hàng | SMS / ZNS (Vendor gửi) |
| ĐVVC đổi trạng thái | Thủ kho, vận hành kênh bán / sale | Thông báo |
| Giao thành công | SPF | QLVT gửi tín hiệu để **SPF ghi nhận đơn hàng đã hoàn tất** (mọi đơn) ✅ BA-6 |
| Giao thành công, dịch vụ FPT Camera Combo | SM | MAC thiết bị, để kích hoạt trên App Camera |
| Giao thành công | INVOICE (Bill) | Xuất hóa đơn thiết bị theo tín hiệu giao hàng hoàn tất của phiếu giao tại quầy (URD XHD REQ-XHD-043) |
| Giao thành công | Hạch toán chi phí (QLVT, FAF) | Thông tin giao dịch thiết bị |

### 1.9 Thao tác trên STG (thông tin QC cung cấp)

Map với luồng chính ở §1.4:

| Thao tác STG | Bước |
|---|---|
| 1. Tool **Quản lý chuỗi cung ứng › Giao dịch thiết bị** → tìm hợp đồng | 1 |
| 2. **Nhận xử lý** phiếu · 3. Chọn kho xuất **KTN test** | 2 |
| 4. **Đề nghị xuất vật tư** | 3 |
| 5. SCM (https://ftelscm-uat.fpt.net — **cần host**): Quản lý kho › Nhập kho › **Tạo phiếu nhập** hàng cần giao, kho **KTN test MAC** (chuẩn bị tồn kho test) · 6. Quản lý kho › **Xác nhận tạm ứng từ Inside** | 3 |
| 7. Quay lại phiếu → **Lưu và đóng hàng** | 5, 6 |
| 8. GHTK staging (https://khachhang-staging.ghtklab.com/web/): Thông tin tài khoản › **Cấu hình API** · 9. **Webhook** → Test → nhập **mã vận đơn** · 10. **Cập nhật trạng thái 5** (giả lập ĐVVC báo trạng thái) | 7, 8 |

> ⚠ BA-7: "trạng thái 5" ở bước 10 là **mã trạng thái của GHTK**, không phải số 5 "ĐVVC đã tiếp nhận" trong §1.6.

---

## 2. Phiếu giao dịch thiết bị tại quầy — không có shipper

Hình thức Quầy (khách nhận tại quầy) hoặc Sale. Hoàn tất trên Tool quầy.

**Đã có MAC:** Quản lý chuỗi cung ứng › Giao dịch thiết bị → tìm hợp đồng → chọn đối tác **Bến Thành**, **Tổ 300** → **Chỉnh sửa** → chọn danh sách MAC → **Lưu** → kết quả xử lý **Hoàn tất** → **Xác nhận**.

**Chưa có MAC** (tạo MAC rồi làm lại các bước trên): Tool **Quản lý vật tư quầy** › Tạm ứng vật tư › Đề nghị tạm ứng → chọn đối tác, tổ, vật tư → **Tạo phiếu** → nhập số lượng → **Xác nhận** → SCM (cần host): Nhập kho › Tạo phiếu nhập (kho **KTN test MAC**) → Xác nhận tạm ứng từ Inside → chọn kho KTN test MAC, tích **Bảo hành V2** → chọn phiếu tạm ứng → nhập **MAC vừa tạo** → **Xác nhận V2**.

---

## 3. Điểm cần xác nhận với BA / PO

| Mã | Vị trí | Vấn đề | Đề xuất |
|---|---|---|---|
| BA-1 | URD B8 | Trigger là "ĐVVC chuyển tình trạng giao hàng **thành công**" nhưng mô tả ghi "QLVT chuyển trạng thái phiếu giao về **Giao hàng không thành công**" | ✅ Đã chốt: chuyển phiếu về **Giao hàng thành công** |
| BA-2 | URD B1 ↔ B10 | B1 ghi trạng thái ban đầu "**Chờ xử lý**", B10 liệt kê "1. **Chờ xác nhận**" | ✅ Đã chốt: trạng thái ban đầu là **Chờ xác nhận** |
| BA-3 | URD B9, B10 | Trạng thái được đánh số 1–16 nhưng mục quy trình không nêu số **10, 14, 15** | ✅ Đã chốt: **không có** trạng thái 10, 14, 15 — giữ đúng URD |
| BA-4 | URD B9 TH2 | Có cả "Giao **hàng** không thành công" (QLVT đặt) và "11. Giao không thành công" (ĐVVC đặt); câu "QLVT chuyển trạng thái… Giao hàng không thành công" lặp 2 lần | ✅ Đã chốt: **là 1 trạng thái** |
| BA-5 | URD B10 TH3 | Phiếu "7. ĐVVC đã lấy hàng" khi hủy đơn: "cancel vận đơn **và giao hàng tới KH**" — mâu thuẫn (đã hủy đơn mà vẫn giao), và không nói vật tư về đâu | ✅ Đã chốt: **thu hồi về FTEL**, về kho đã chọn lúc xác nhận |
| BA-6 | Sơ đồ URD ↔ URD XHD | Sơ đồ có bước "Xuất hóa đơn" (Bill) sau hoàn ứng, nhưng bảng B8 chỉ nói tín hiệu cho SPF (đơn TMĐT) và SM. URD XHD yêu cầu tín hiệu giao hàng đi **thẳng về INVOICE** từ phiếu giao tại quầy | ✅ Đã chốt: QLVT gửi tín hiệu cho **SPF ghi nhận đơn hàng đã hoàn tất** |
| BA-7 | STG ↔ URD | Webhook GHTK "trạng thái 5" là mã của GHTK | Cần bảng map mã trạng thái GHTK / Ahamove → trạng thái phiếu giao |
| BA-8 | URD B1 ↔ rule TMĐT | Đơn Shopee/TikTok không có khoản thu (dùng Order Transaction). Chưa rõ "đơn thanh toán thành công" của đơn sàn là thời điểm nào để tạo phiếu giao | ✅ Đã chốt: tạo phiếu giao **sau khi tạo đơn hàng** |
| BA-9 | URD B9 C, D | "Đơn hàng BÌNH THƯỜNG" là tình trạng của đơn hay của hợp đồng | ✅ Đã chốt: là **trạng thái của đơn hàng** |
| BA-10 | Tổng quan ↔ URD | URD gọi chung "Vendor" cho hệ thống kết nối ĐVVC, trùng tên với Vendor NCC (M-Vendor) | 🟡 Bạn trả lời 19/11/2026: **là 1 hệ thống** nhưng chưa chắc chắn — cần xác nhận lại |
