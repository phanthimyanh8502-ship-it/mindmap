# RULE CHỦ THỂ — TOOL QUẢN LÝ VẬT TƯ

> Cung cấp vật tư cho phiếu thi công TIN/PNC; vật tư tạm ứng từ Tool SCM.
> Tách từ `../01-DON-HANG/kenh-ban/00-CHUNG.md`; số mục (§) giữ theo file gốc.
> Bổ sung 19/11/2026 — quy trình tổng quan từ URD INSIDE Resource Equipment V1.0 (`ISC_INSIDE-Resource-Equipment V1.0_URD_V1.0.docx`) — chỉ mục **Thông tin chung** và **Tổng quan › Quy trình nghiệp vụ**.

---

## Quy trình tổng quan

> Nguồn: URD INSIDE Resource Equipment V1.0 (ReInvent M-Equipment, Milestone 1 — vật tư TIN/PNC), mục "Thông tin chung" và "Tổng quan › Quy trình nghiệp vụ" (sơ đồ *Tổng quan*, sơ đồ *Quản lý vật tư TIN/PNC* và bảng bước – người thực hiện). Không lấy đặc tả từng chức năng.

**Hệ thống:** Inside – Vật tư TIN/PNC (khai báo, xác nhận, báo cáo) và app **MobiX** (NVKT/KTV đề nghị tạm ứng, chuyển vật tư, hoàn ứng, nhập vật tư); xác nhận tạm ứng trên **FTELSCM**; vật tư dùng khi **triển khai** (Inside/MobiX – Triển khai, theo phiếu thi công) và **bảo trì** (Inside/MobiX – Bảo trì).

| # | Nghiệp vụ | Người thực hiện | Hệ thống |
|---|---|---|---|
| 1 | Khai báo thông tin vật tư. Với **loại hình bán thiết bị**: **QLCS lấy dữ liệu từ Quản lý vật tư rồi trả ra cho SPF** (QC xác nhận 19/11/2026) | FTQ / INF | Inside |
| 2 | Phân quyền kho – đối tác: điều hành, kế toán, thủ kho | FTQ / QLĐV | Inside |
| 3 | Khai báo định mức vật tư | FAF / kế toán trưởng | Inside |
| 4 | Khóa chuyển vật tư | FAF | Inside |
| 5 | Đề nghị tạm ứng | Đội trưởng, NVKT / KTV (điều hành) | MobiX, Inside |
| 6 | Xác nhận tạm ứng | FMD (thủ kho) | FTELSCM |
| 7 | Vật tư đã xác nhận tạm ứng **lưu vào kho tạm của KTV** (QC cung cấp 26/11/2026) | — | MobiX |
| 8 | Dùng vật tư khi thực hiện **triển khai** hoặc **bảo trì**: phiếu chọn MAC từ **kho tạm của KTV** | NVKT / KTV | Inside/MobiX – Triển khai, Bảo trì |
| 9 | Đề nghị hoàn ứng (hoàn ứng triển khai / hoàn ứng bảo trì) | Đội trưởng, NVKT / KTV | MobiX, Inside |
| 10 | Xác nhận hoàn ứng, xác nhận tổng hợp (phiếu xuất tổng hợp) | FAF | Inside |
| 11 | Đề nghị / xác nhận hoàn ứng điều chỉnh | Đội trưởng / TP, PP kỹ thuật | Inside |
| 12 | Gửi / xác nhận / phê duyệt yêu cầu BGĐ CN xác nhận sử dụng vật tư | Đội trưởng, NVKT / TP, PP / BGĐ CN | Inside |
| 13 | Đề nghị / xác nhận nhập vật tư | Đội trưởng, NVKT / FMD | MobiX, Inside |
| 14 | Đề nghị / xác nhận bồi thường vật tư | Đội trưởng / FAF | Inside |
| 15 | Xác nhận Dataload ORC ERP | FAF | Inside ⇒ ORC ERP |
| 16 | Lịch sử vật tư – điều chỉnh vật tư | CUS HO, CS, TIN/PNC | Inside |
| 17 | Báo cáo, đối soát vật tư (đối soát kho tạm với FTELSCM) | TIN/PNC, FAF, FMD | Inside, FTELSCM |

> **Kho tạm của KTV (QC cung cấp 26/11/2026):** sau khi FMD xác nhận tạm ứng, vật tư vào thẳng kho tạm của KTV; phiếu triển khai / bảo trì lấy MAC từ kho tạm này, **không qua bước chuyển vật tư**. **Chuyển vật tư** (MobiX) là nhánh phụ: chỉ dùng khi KTV chuyển vật tư cho nhân sự khác cùng chi nhánh (bên nhận xác nhận nhận vật tư).

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
