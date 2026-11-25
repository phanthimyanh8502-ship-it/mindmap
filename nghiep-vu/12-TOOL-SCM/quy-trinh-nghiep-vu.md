# RULE CHỦ THỂ — TOOL SCM (KHO)

> Kho SCM: nguồn tạm ứng vật tư cho Tool Quản lý vật tư và Tool Quản lý vật tư quầy. **Cần host** trước khi truy cập.
> Tách từ `../01-DON-HANG/kenh-ban/00-CHUNG.md`; số mục (§) giữ theo file gốc.
> Bổ sung 19/11/2026 — quy trình tổng quan **Tích hợp Inside** (bạn chốt chỉ cần phần này): mục lục IX của `Quy-trình-SCM.docx` + 2 URD vật tư.

---

## Quy trình tổng quan — Tích hợp Inside

> Bạn chốt 19/11/2026: quy trình tổng quan của Tool SCM chỉ cần phần **Tích hợp Inside** (luồng vật tư giữa tool vật tư và kho FTELSCM). "Inside" là tên mục trong tài liệu; **Tool Quản lý vật tư và Quản lý vật tư quầy nằm ở Fox ERP** (bạn xác nhận 19/11/2026).
> Nguồn: `Quy-trình-SCM.docx` (hướng dẫn sử dụng FTELSCM 1.5) — mục lục **IX. Tích hợp Inside** có 5 quy trình (tạm ứng, hoàn ứng, trả vật tư, bồi thường vật tư, thu hồi vật tư) nhưng không có nội dung; vai trò và bước lấy từ URD Resource Equipment V1.0 (vật tư TIN/PNC), URD Retail-Counter V1.0 (vật tư quầy) và thao tác STG bạn cung cấp. Chỗ đánh dấu *(chưa rõ)* là tài liệu không nói.

**Hai đầu:** tool vật tư trên **Fox ERP** (Quản lý vật tư — TIN/PNC — NVKT/KTV thao tác qua Mobinet = MobiX; Vật tư quầy — giao dịch viên) ⇄ kho **FTELSCM** (thủ kho FMD). Kế toán **FAF** xác nhận trên Fox ERP.

| # | Quy trình | Bắt đầu ở Fox ERP | Xác nhận | Kết quả trên SCM |
|---|---|---|---|---|
| 1 | **Tạm ứng** | Đội trưởng / NVKT (TIN/PNC) hoặc giao dịch viên (quầy) **đề nghị tạm ứng** | **FMD xác nhận tạm ứng** trên FTELSCM (Quản lý kho › Xác nhận tạm ứng từ Inside; xuất theo MAC / số lượng) | Vật tư chuyển sang **kho tạm** của nhân viên / đối tác / quầy; tool vật tư nhận vật tư |
| 2 | **Hoàn ứng** | Sau khi dùng vật tư (triển khai, bảo trì, giao dịch thiết bị) ⇒ **đề nghị hoàn ứng** (PTC hoàn tất thì hoàn ứng tự động) | **FAF xác nhận hoàn ứng**, xác nhận tổng hợp | SCM ghi nhận **hoàn ứng**, **tổng hợp phiếu xuất** — vật tư đã dùng trừ khỏi kho tạm |
| 3 | **Trả vật tư** | Vật tư không dùng ⇒ **đề nghị nhập / trả vật tư** | **FMD xác nhận nhập** | **Nhập kho**, tồn cộng lại |
| 4 | **Bồi thường vật tư** | Vật tư mất ⇒ **đề nghị bồi thường** | **FAF xác nhận bồi thường** | Cách ghi trên SCM *(chưa rõ)* |
| 5 | **Thu hồi vật tư** | Thiết bị thu hồi từ khách ⇒ phiếu thu hồi ⇒ cập nhật kết quả thu hồi | Thủ kho | **Nhập kho thu hồi** |
| — | **Đối soát kho tạm** | Định kỳ | FAF, FMD | Tồn kho tạm khớp giữa Fox ERP và FTELSCM ⇒ FAF xác nhận **Dataload ORC ERP** |

**Lưu ý:** "Kế toán xác nhận" trên SCM là xác nhận **chứng từ kho** (phiếu nhập / phiếu xuất); **xác nhận tạm ứng do FMD (thủ kho)** làm, không phải kế toán.

---

### 5.5 Vật tư cho phiếu & kho SCM

> Nguồn: thông tin user cung cấp ngày 04/11/2026.

**Luồng vật tư:** Kho SCM ⇒ (tạm ứng) ⇒ Tool vật tư ⇒ (load vật tư) ⇒ Giao & lắp đặt.

1. Tool vật tư **đề nghị tạm ứng**.
2. Tool **kho SCM** (https://ftelscm-uat.fpt.net — **cần host**):
   - **Quản lý kho › Nhập kho › Tạo phiếu nhập** hàng hóa (kho **KTN test MAC**).
   - **Quản lý kho › Xác nhận tạm ứng từ Inside**.
3. Vật tư được tạm ứng về tool vật tư.
4. Giao & lắp đặt **load vật tư** từ tool vật tư.

| Tool vật tư | Phiếu load vật tư từ tool này |
|---|---|
| **Quản lý vật tư quầy** | Phiếu giao dịch thiết bị tại quầy (bước đề nghị tạm ứng: xem §5.3, trường hợp chưa có MAC) |
| **Quản lý vật tư** | Phiếu thi công TIN/PNC (chưa có các bước chi tiết) |

---

### 5.2 Hoàn tất phiếu giao hàng tại quầy có shipper giao hàng
1. Vào tool **Quản lý chuỗi cung ứng › Giao dịch thiết bị** → tìm hợp đồng.
2. **Nhận xử lý** phiếu.
3. Chọn kho xuất **KTN test**.
4. **Đề nghị xuất vật tư**.
5. Trên tool **SCM** (https://ftelscm-uat.fpt.net — **cần host**): **Quản lý kho › Nhập kho › Tạo phiếu nhập** với hàng hóa đang cần giao, chọn kho **KTN test MAC**.
6. **Quản lý kho › Xác nhận tạm ứng từ Inside**.
7. Quay lại phiếu giao dịch thiết bị → chọn **Lưu và đóng hàng**.
8. Trên tool GHTK (https://khachhang-staging.ghtklab.com/web/): **Thông tin tài khoản › Cấu hình API**.
9. **Webhook** → chọn **Test** → nhập **mã vận đơn** vào ô Mã đơn hàng.
10. Chọn **cập nhật trạng thái 5**.
