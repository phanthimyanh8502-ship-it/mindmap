# RULE — PHIẾU THI CÔNG (TIN/PNC, FTI)

> Loại triển khai: TIN/PNC, TIN/PNC giao hàng, FTI. Quy tắc chung (BR-PTK-*) ở [tổng quan Giao & lắp đặt](../quy-trinh-nghiep-vu.md).
> Nguồn: thông tin bạn cung cấp 04/11 và 17/11/2026 (xem [`input/`](input/README.md)).
> Bổ sung 19/11/2026 — điều kiện hoàn tất PTC từ `input/validate-completed-deployment.png` (chỉ các nhóm điều kiện); nguồn tạo PTC theo bạn xác nhận.
> Bổ sung 19/11/2026 — quy trình tổng quan từ URD Phát triển phân hệ Triển khai v2.0 (`ISC_Phat-trien-phan-he-Trien-khai_v2.0_URD-v1.0.docx`) — chỉ mục **Tổng quan › Sơ đồ tổng quan**.

---

## Quy trình tổng quan

> Nguồn: URD Phát triển phân hệ Triển khai v2.0, mục "Tổng quan › Sơ đồ tổng quan" (sơ đồ *Tổng quan quy trình triển khai* + danh sách chức năng cấp 1). Màn hình: **Inside New V5 › Hỗ trợ kỹ thuật › Thông tin chung › Triển khai**. Không lấy đặc tả chi tiết từng chức năng.

| # | Bước | Rẽ nhánh |
|---|---|---|
| 1 | Hợp đồng / đơn hàng cần triển khai | Nguồn tạo PTC (bạn xác nhận 19/11/2026): **đơn hàng** (theo flow bán hàng của kênh, xem [Đơn hàng](../../01-DON-HANG/quy-trinh-nghiep-vu.md)) hoặc **hợp đồng** khi tạo **SR chuyển dịch vụ**, **SR chuyển địa điểm**, **SR khôi phục dịch vụ**. **Đơn bán thêm** mà **hợp đồng đang có PTC** ⇒ hệ thống **đẩy thông tin đơn hàng vào PTC hiện có**, không tạo PTC mới (bạn xác nhận 19/11/2026) |
| 2 | Request tạo PTC → **xử lý điều kiện** | Đạt ⇒ 2.1 **Phiếu thi công triển khai** · Không ⇒ 2.2 **Tạo phiếu công trắng** |
| 3 | **Phân công** đối tác và nhân sự | — |
| 4 | **Nhân sự thi công** → kiểm tra điều kiện thi công | Đạt ⇒ 6 · Không ⇒ 5 |
| 5 | Trả về **PTC NOT OK** → 5.1 bộ phận xử lý trả về → xử lý PTC NOT OK | Xử lý được ⇒ 5.2 **Chuyển thi công** (quay lại 2.1) · Không ⇒ 5.3 **Đề nghị hủy PTC** ⇒ kết thúc |
| 6 | **Hoàn tất PTC** → kiểm tra điều kiện hoàn tất | Không đạt ⇒ quay lại 4 · Đạt ⇒ 6.1 |
| 6.1 | **Nghiệm thu vật tư** → xử lý? | Không ⇒ quay lại 6 · Có ⇒ 6.2 |
| 6.2 | Cập nhật vật tư thi công, **thu hồi vật tư** và **hoàn ứng tự động** — hoàn ứng trên [Tool Quản lý vật tư](../../10-QUAN-LY-VAT-TU/quy-trinh-nghiep-vu.md) (bạn xác nhận 19/11/2026) | ⇒ 7 Kết thúc |

**Điều kiện hoàn tất PTC (tổng quan)** — từ sơ đồ `input/validate-completed-deployment.png`, chỉ lấy các nhóm điều kiện:

| Nhóm | Điều kiện chính |
|---|---|
| Tiên quyết | Hợp đồng tình trạng **bình thường** · PTC tình trạng **khác Hoàn tất** |
| Trên tác vụ | [MobiNet = MobiX] gông tọa độ chênh lệch check-in – check-out **≤ 50 m** · đã phân công nhân sự chính cho PTC |
| Trên hợp đồng | Thanh toán (hoàn tất các khoản thu hiển thị trên PTC) ⚠ · cài đặt HiFPT · hợp đồng NET (tín hiệu online, suy hao lastmile, công suất) · Wifi Marketing · online session |
| Trên đơn hàng | Upload ảnh hồ sơ khách hàng (bán mới, đơn vị bán DKOL) · biên bản nghiệm thu · biên bản điện tử · chiều dài cáp LastMile · vật tư (khả dụng trong kho tạm NV, MAC khớp chức năng, MAC triển khai khác MAC thu hồi…) |
| Trên dịch vụ | Dịch vụ active thành công (NET, FPT Play, Camera Bundle, Camera OTT) · MAC online / active = MAC trên PTC (nghiệm thu) · SĐT active trùng SĐT trên đơn (Camera OTT) / SĐT chính chủ (Camera Bundle) |

> ⚠ Sơ đồ có điều kiện "hoàn tất tất cả khoản thu hiển thị trên PTC", trong khi bạn cung cấp ngày 17/11/2026 là **bỏ** rule "khoản thu đã thanh toán + ký BBĐT mới hoàn tất PTC". Cần xác nhận (xem câu hỏi C1).

**Chức năng cấp 1:** tạo mới PTC · thông tin PTC · kiểm tra hoàn tất PTC · hoàn tất PTC · cập nhật thông tin trên PTC · chuyển PTC NOT OK · vật tư triển khai / thu hồi · nghiệm thu vật tư · chuyển lại PTC.

---

## 1. Phiếu thi công

**Thông tin trên PTC:** phân tuyến (từ tool Quản lý đối tác, để phân công nhân sự TIN/PNC) · hợp đồng · đơn hàng · vật tư triển khai (thiết bị khách mua) · vật tư thu hồi · khoản thu.

**Luồng xử lý:** phân tuyến ⇒ phân công nhân sự TIN/PNC ⇒ nhân sự xử lý phiếu trên **app MobiX** ⇒ "Đã xử lý hoàn tất" ⇒ tín hiệu giao hàng về INVOICE. Vật tư của PTC lấy từ **Tool Quản lý vật tư** (tạm ứng từ SCM).

**Hoàn tất PTC trên STG:**
- **Cách 1 — Inside + partner portal:** Inside new v5 › Thông tin chung › Triển khai → nhập số hợp đồng → phân tuyến → http://partner-stag.fpt.net/pt-portal/bypass → Bypass, tích tất cả, nhập hợp đồng, thời gian hết hạn bypass (tối đa 24 giờ), nguyên nhân → Cập nhật → quay lại PTC chọn **Đã xử lý hoàn tất**.
- **Cách 2 — SPF Web admin:** chi tiết đơn hàng › PTC › **Hoàn tất PTC**.

**Thao tác khác:** Hủy PTC / chuyển thi công lại: Inside › Quản lý hợp đồng › HĐ NOT OK V3 › PTC NOT OK · Quota PTC: Fox ERP › Quản lý đối tác › Quản lý Block › Quota PTC - TUT.
