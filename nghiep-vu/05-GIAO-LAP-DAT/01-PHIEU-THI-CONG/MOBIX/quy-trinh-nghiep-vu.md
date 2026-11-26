# MOBIX — App xử lý phiếu thi công của kỹ thuật TIN/PNC

> Thư mục con của [Phiếu thi công](../quy-trinh-nghiep-vu.md). MobiX = Mobinet (Mobinet Nextgen), QC xác nhận 19/11/2026.
> Nguồn: tài liệu QC cung cấp 26/11/2026 trong [`input/`](input/README.md) — chỉ lấy quy trình tổng quan, không lấy đặc tả màn hình.

---

## Tổng quan

- **Là gì:** app của nhân sự TIN/PNC (NVKT, KTV, đội trưởng). App lấy dữ liệu từ Inside để hiện các ca vụ được phân công (triển khai, bảo trì), vật tư, thanh toán.
- **Vai trò trong luồng bán hàng:** đơn hàng có triển khai ⇒ tạo PTC ⇒ phân tuyến trên Inside new v5 ⇒ **KTV nhận ca và xử lý trên MobiX** ⇒ hoàn tất PTC ⇒ tín hiệu giao hàng về INVOICE.
- **Đồng bộ trạng thái:** MobiX và Inside new v5 dùng chung trạng thái ticket. Trạng thái được truyền sang SR, SPF, HiFPT.

## Quy trình xử lý ticket triển khai trên MobiX

> Nguồn: `MBX - V2.3 - FTQ - Mô tả thay đổi tình trạng ticket TKBT` (bảng quy trình mục 1).

| # | Bước | Ai / ở đâu | Trạng thái ticket |
|---|---|---|---|
| 1 | Tạo ticket triển khai: đơn bán mới, bán thêm, SR; đã thanh toán nếu hình thức khác COD | SPF, SR | Chưa phân công |
| 2 | Phân tuyến: hệ thống phân công cho nhân viên chuyên trách; không phân cho người off ngày hẹn. Đội trưởng chỉnh phân công được trên MobiX. **Phân công cho nhân sự nào thì PTC hiện ở Ca tồn trên app MobiX của nhân sự đó** | Inside new v5 · MobiX (đội trưởng) | Đã phân công |
| 3 | **Nhận ca:** KTV nhận tuyến, gọi khách chốt lịch hẹn; khách đổi lịch thì tích hẹn lại | MobiX | Đã nhận ca |
| 4 | **Xác nhận di chuyển** tới nhà khách (tạm thời không bắt buộc; hủy được khi chưa check-in) | MobiX | Đang di chuyển |
| 5 | **Check-in** tại nhà khách ⇒ thu tiền, ký BBĐT, up hồ sơ (nếu có) ⇒ triển khai | MobiX | Đang xử lý |
| 6 | Chờ đơn vị khác bổ sung (vd bổ sung vật tư trên PTC) | MobiX / Inside | Đã xử lý và đang theo dõi |
| 7a | **Không triển khai được** ⇒ chọn nguyên nhân trả về; đơn vị liên quan xử lý trong 24 giờ | MobiX | Chờ xác minh (PTC NOT OK) |
| 7b | **Triển khai được** ⇒ chụp ảnh thi công ⇒ nghiệm thu dịch vụ ⇒ hoàn tất ticket | MobiX | Đã xử lý hoàn tất |

**Nhánh phụ trên ca:** nhả tuyến (chọn nguyên nhân, phiếu rời khỏi danh sách của KTV) · ghép cặp (cần 2 người) · xem lịch sử nhận / nhả tuyến.

## Gông khi xử lý và hoàn tất PTC trên MobiX

| Gông | Rule |
|---|---|
| Check trùng hợp đồng | PTC triển khai mới: hệ thống tự check trùng khách hàng (CCCD / MST) và địa chỉ lắp đặt với hợp đồng cũ. Kết quả theo số bill nợ, thời gian ngưng dịch vụ, trả trước, thiết bị đã thu hồi chưa: **tiếp tục triển khai** (thu hồi thiết bị cũ nếu chưa thu hồi), hoặc **ngưng triển khai** (khách phải trả trước / đóng nợ, hoặc thuộc nhóm khôi phục dịch vụ ⇒ tạo SR KPDV) |
| CCCD khách hàng | Đơn **bán mới** của đơn vị bán ĐKOL, TLS, CS: phải cập nhật CCCD trên PTC mới hoàn tất được. SPF báo hợp đồng nào cần cập nhật |
| Check-in / check-out | Tọa độ chênh lệch ≤ 50 m (xem [điều kiện hoàn tất PTC](../quy-trinh-nghiep-vu.md)) |
| Vật tư bàn giao | MAC chọn từ danh sách thiết bị **đã tạm ứng trong kho tạm của KTV**; không nhập tay |
| Vật tư thu hồi | Đổi bảo hành, swap, triển khai có thu hồi: MAC chọn từ danh sách thiết bị **đã hoàn ứng cho hợp đồng** |
| Khoản thu | Tài khoản TIN/PNC **bắt buộc thanh toán khoản thu của PTC**; khoản thu khác không bắt buộc |
| SR | Ca có hướng xử lý cần tạo SR: phải tạo SR thành công trên MobiX mới hoàn tất phiếu |

## Thanh toán trên MobiX (SDK thanh toán)

> Nguồn: `ISC_Thanh toan v2.0_URD`, `Rule tồn tạm New`, `ISC_MBX_v2.9_PRD` (FR05 – FR08).

**Hình thức thanh toán:**
- **Tiền mặt tạm:** KTV thu tiền mặt. Giao dịch đẩy vào **hợp đồng đại diện** để gạch nợ bổ sung, trừ hạn mức của KTV.
- **Online từ tài khoản nhân viên:** Ví FPT Pay đã liên kết.
- **Online từ khách hàng:** QR Pay – VNPay. KTV đưa mã QR cho khách tự quét.

**Rule chính:**
- Thanh toán hóa đơn xa nhất trước. Tối đa 6 hóa đơn / khoản thu mỗi lần.
- Hợp đồng còn **HĐĐT / PLHĐ / BBĐT chưa ký** thì không xác nhận thu tiền được. Khách ký trên HiFPT / fpt.vn / member trước.
- Hạn mức tiền mặt: tổng tiền không vượt hạn mức còn lại. Có cấp hạn mức bổ sung theo điều kiện.
- **Tồn tạm:** tiền mặt tạm phải nộp về công ty trước 10 giờ ngày làm việc kế tiếp (thu sau 16 giờ thứ 6 thì nộp vào thứ 2). Quá hạn ⇒ MobiX **khóa thu tiền tạm và online** đến khi nộp đủ. Tồn tạm quá 48 giờ ⇒ **không cho xuất vật tư**.
- Thanh toán tạm và gạch nợ đi qua **Billing Hub (BLH)**, không qua Payment Gate (v2.9). DVKH HO gạch nợ online / gạch nợ tạm trên Fox ERP — xem [Gạch nợ & hậu kỳ](../../../08-GACH-NO-HAU-KY/quy-trinh-nghiep-vu.md).
- Xác nhận thanh toán gửi khách qua HiFPT hoặc Zalo / SMS (1 số điện thoại tối đa 10 lần / tháng).

## Vật tư trên MobiX

> Nguồn: `FTP_MobinetNextgen_v1.0_URD_Quanlyvattu_v1.1`, `ĐTYC_Quản lý mac theo ngày xuất`. Quy trình đầy đủ ở [Tool Quản lý vật tư](../../../10-QUAN-LY-VAT-TU/quy-trinh-nghiep-vu.md).

- KTV xem kho tạm của mình, tạo phiếu **tạm ứng** (chỉ kho chi nhánh đang trực thuộc, theo quota), **nhập trả**, **chuyển** cho nhân sự cùng chi nhánh, **nhận** vật tư được chuyển.
- Quản lý MAC theo ngày nhận (xuất trước dùng trước). Vật tư giữ quá 15 ngày ⇒ cảnh báo; từ 30 ngày ⇒ khóa tạm ứng thêm / sử dụng / chuyển, chỉ được nhập trả về kho.
