# RULE CHỦ THỂ — TOOL QUẢN LÝ VẬT TƯ QUẦY

> Cung cấp vật tư cho phiếu giao dịch thiết bị tại quầy; vật tư tạm ứng từ Tool SCM.
> Tách từ `../01-DON-HANG/kenh-ban/00-CHUNG.md`; số mục (§) giữ theo file gốc.
> Bổ sung 19/11/2026 — quy trình tổng quan từ URD Retail-Counter V1.0 (`ISC_INSIDE_Retail-Counter-V1.0_URD_V1.0_18072024.docx`) — chỉ mục **Tổng quan › Quy trình nghiệp vụ**.

---

## Quy trình tổng quan

> Nguồn: URD INSIDE Retail-Counter V1.0 (18/07/2024), mục "Tổng quan › Quy trình nghiệp vụ" (sơ đồ *Tổng quan* và *Quy trình giao dịch thiết bị – Quản lý vật tư quầy*). Không lấy đặc tả từng chức năng.

**Chuỗi nghiệp vụ Vật tư quầy – Giao dịch thiết bị** (hệ thống chính: Inside › Vật tư quầy):

| # | Nghiệp vụ | Người thực hiện | Hệ thống |
|---|---|---|---|
| 1 | Khai báo thông tin vật tư | FTQ / INF | Inside – Vật tư quầy |
| 2 | Phân quyền đối tác – kho: giao dịch viên, kế toán, thủ kho | FTQ, trưởng đơn vị | Inside – Vật tư quầy |
| 3 | Tạo định mức vật tư | FAF | Inside – Vật tư quầy |
| 4 | Đề nghị tạm ứng | Giao dịch viên | Inside – Vật tư quầy |
| 5 | Xác nhận tạm ứng | FMD (thủ kho) | FTELSCM |
| 6 | Bàn giao vật tư | Trưởng đơn vị | Inside – Vật tư quầy |
| 7 | **Giao dịch thiết bị**: bán thiết bị, thuê có thu hồi, bảo hành… | Sale, CS, KDPP… | Saleclub · Inside đại lý / KC · Inside – Vật tư quầy |
| 8 | Đề nghị hoàn ứng | CS, KDPP… | Inside – Vật tư quầy |
| 9 | Xác nhận hoàn ứng, tổng hợp phiếu xuất | FAF | Inside – Vật tư quầy |
| 10 | Đề nghị / xác nhận hoàn ứng điều chỉnh | CS, KDPP… / TP, PP | Inside – Vật tư quầy |
| 11 | Đề nghị / xác nhận nhập vật tư | CS, KDPP… / FMD | Inside – Vật tư quầy |
| 12 | Đề nghị / xác nhận bồi thường vật tư | CS, KDPP… / FAF | Inside – Vật tư quầy |
| 13 | Xác nhận ORC ERP | FAF | Inside – Vật tư quầy |
| 14 | Đối soát, báo cáo | FAF, FMD | Inside – Vật tư quầy |

**Các khối trong sơ đồ quy trình:**
- **Phiếu giao tại quầy của đơn SPF = phiếu bán thiết bị** (QC xác nhận 19/11/2026), xem [Phiếu giao dịch thiết bị tại quầy](../05-GIAO-LAP-DAT/02-PHIEU-GIAO-DICH-THIET-BI-TAI-QUAY/quy-trinh-nghiep-vu.md).
- **Giao dịch thiết bị** (giao dịch viên, theo nhu cầu sử dụng): kiểm tra thiết bị · bán thiết bị · thuê thiết bị có / không thu hồi thiết bị cũ · đổi bảo hành / đổi bảo hành 7 ngày (BGĐ phê duyệt) · xuất thiết bị theo confirm BGĐ · đổi thiết bị mới / đổi chênh lệch · xuất thiết bị HĐ khôi phục dịch vụ ⇒ cập nhật thông tin hóa đơn (Inside – Hóa đơn) ⇒ **hoàn tất phiếu**. Phiếu có thu hồi ⇒ cập nhật thông tin thu hồi.
- **Thu hồi – vật tư thu hồi:** tạo phiếu thu hồi tại quầy ⇒ cập nhật kết quả thu hồi ⇒ nhập kho thu hồi.
- **Khai báo & phân quyền:** khai báo vật tư · mã khoản thu · đối tác, tổ · kho kết nối FTELSCM · định mức vật tư · phân quyền đối tác – GDV, đối tác – kho.
- **Vận hành vật tư:** tạm ứng ⇒ bàn giao ⇒ hoàn ứng / hoàn ứng điều chỉnh ⇒ phiếu xuất tổng hợp ⇒ nhập vật tư · bồi thường · đối soát kho tạm · dataload Compact ⇒ ORC ERP.
- **Hệ thống liên quan:** Inside – QLCS (khai báo chính sách bán hàng) · Saleclub / AM và Inside đại lý, kênh chuỗi (khách tạo đơn ⇒ lên đơn thành công ⇒ phiếu bán thiết bị) · FTELSCM (tạm ứng, hoàn ứng, tổng hợp phiếu xuất, nhập kho, đối soát kho tạm) · ORC ERP.

---

### 5.5 Vật tư cho phiếu & kho SCM

> Nguồn: thông tin QC cung cấp ngày 04/11/2026.

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

### 5.3 Hoàn tất phiếu giao hàng tại quầy không có shipper giao hàng

**Trường hợp đã có MAC:**
1. Vào tool **Quản lý chuỗi cung ứng › Giao dịch thiết bị** → tìm hợp đồng.
2. Chọn đối tác **Bến Thành**, **Tổ 300**.
3. Chọn **Chỉnh sửa** → chọn **danh sách MAC** → nhấn **Lưu**.
4. Chọn kết quả xử lý **Hoàn tất**.
5. Nhấn **Xác nhận**.

**Trường hợp chưa có MAC** (tạo MAC trước, rồi làm lại các bước trên):
1. Vào tool **Quản lý vật tư quầy**.
2. Chọn **Tạm ứng vật tư**.
3. Chọn **Đề nghị tạm ứng**.
4. Chọn đối tác, tổ, vật tư muốn tạm ứng.
5. Nhấn **Tạo phiếu**.
6. Nhập số lượng → **Xác nhận**.
7. Trên tool **SCM** (https://ftelscm-uat.fpt.net — **cần host**): **Quản lý kho › Nhập kho › Tạo phiếu nhập** với hàng hóa đang cần giao, chọn kho **KTN test MAC**.
8. **Quản lý kho › Xác nhận tạm ứng từ Inside**.
9. Chọn kho **KTN test MAC**, tích **Bảo hành V2**.
10. Chọn **phiếu tạm ứng** → nhập **MAC vừa tạo ở phiếu nhập**.
11. Nhấn **Xác nhận V2**.
