# MOBIX — App xử lý phiếu thi công của kỹ thuật TIN/PNC

> Thư mục con của [Phiếu thi công](../quy-trinh-nghiep-vu.md). Tài liệu gốc cũ gọi là Mobinet / Mobinet Nextgen (MBN); thống nhất gọi **MobiX** (QC xác nhận là 1 app, 19/11/2026).
> Nguồn: tài liệu QC cung cấp 26/11/2026 trong [`input/`](input/README.md) — chỉ lấy quy trình tổng quan, không lấy đặc tả màn hình.

---

## Tổng quan

- **Là gì:** app của nhân sự TIN/PNC (NVKT, KTV, đội trưởng). App lấy dữ liệu từ Inside để hiện các ca vụ được phân công (triển khai, bảo trì), vật tư, thanh toán.
- **Vai trò trong luồng bán hàng:** đơn hàng có triển khai ⇒ tạo PTC ⇒ phân tuyến trên Inside new v5 ⇒ **KTV nhận ca và xử lý trên MobiX** ⇒ hoàn tất PTC ⇒ tín hiệu giao hàng về INVOICE.
- **Đồng bộ trạng thái:** MobiX và Inside new v5 dùng chung trạng thái ticket. Trạng thái được truyền sang SR, SPF, HiFPT.

## Chức năng chính

> MobiX là luồng riêng, không gộp vào luồng Phiếu thi công: hoàn tất PTC chỉ là 1 chức năng (QC cung cấp 26/11/2026).

| Chức năng | Ai dùng | Kết quả |
|---|---|---|
| **Hoàn tất PTC** (Ca tồn › Triển khai) | KTV TIN/PNC | PTC Đã xử lý hoàn tất ⇒ tín hiệu giao hàng về INVOICE |
| **Hoàn tất bảo trì** (Ca tồn › Bảo trì) | KTV TIN/PNC | Ticket bảo trì (tạo theo quy trình SR hỗ trợ kỹ thuật) hoàn tất |
| **Tạo SR** (Quản lý SR) | NVKT, KTV, đội trưởng, tổ trưởng | Tạo và xem SR ngay trên app; ca cần SR phải tạo SR thành công mới hoàn tất phiếu |
| **Thanh toán hóa đơn, khoản thu** | KTV TIN/PNC | Thu tiền mặt tạm / Ví FPT Pay / QR VNPay ⇒ gạch nợ qua Billing Hub |
| **Vật tư** | KTV TIN/PNC | Tạm ứng, chuyển, nhận, nhập trả; hoàn ứng tự động khi hoàn tất phiếu |
| **Thu hồi thiết bị** (Ca tồn › Thu hồi) | KTV TIN/PNC | Thu hồi thiết bị của khách ⇒ nhập trả về kho |
| **CCDC** (công cụ dụng cụ) | NVKT, KTV | Xem CCDC được cấp, hạn dùng; yêu cầu cấp mới / cấp đổi |
| **Chức năng đội trưởng** | Đội trưởng, TPKT | Báo cáo ca vụ, quản lý ca tồn của KTV, phân tuyến lại, cập nhật port, xem tọa độ nhân sự |

**Hoàn tất bảo trì (tổng quan):** ticket bảo trì ⇒ phân công trên Inside new v5 ⇒ ca hiện ở Ca tồn tab Bảo trì trên MobiX của nhân sự được phân công ⇒ nhận ca, check-in (ca xử lý từ xa không cần check-in) ⇒ xử lý checklist bảo trì (đổi thiết bị: MAC thu hồi lấy từ thiết bị đã hoàn ứng cho hợp đồng) ⇒ Đã xử lý hoàn tất, hoặc Chờ xác minh.

**Thu hồi thiết bị (tổng quan):** nguồn tạo phiếu thu hồi: (1) Inside tạo khi bùng cước, thanh lý hợp đồng tại nhà / tại quầy ⇒ tab **Cần thu hồi**; (2) phiếu triển khai / bảo trì có khai báo vật tư thu hồi ⇒ hoàn tất phiếu thì tự tạo phiếu thu hồi ở tab **Đã thu hồi – chưa nhập kho**. KTV cập nhật tình trạng từng thiết bị (Chưa thu hồi · Đã thu hồi – chưa nhập kho · Đã thu hồi – đã nhập kho · Thu hồi không thành công kèm nguyên nhân) ⇒ kho xác nhận nhập trả ⇒ Đã thu hồi – đã nhập kho. Có tra cứu thiết bị theo MAC / số HĐ / mã QR để thu hồi, nhập kho.

**CCDC (tổng quan):** tài liệu gốc ghi app My PT, dữ liệu CCDC lấy từ SCM. Nhân viên xem danh sách CCDC (tổng, sắp hết hạn, hết hạn) ⇒ tạo yêu cầu **cấp mới** (CCDC chưa có) hoặc **cấp đổi** (CCDC đang có) ⇒ Mới (chờ tiếp nhận) ⇒ đội trưởng cập nhật trên **HO My PT**: Đang xử lý ⇒ Hoàn thành hoặc Từ chối; mỗi lần đổi trạng thái có thông báo về app.

## Hoàn tất PTC — quy trình xử lý ticket triển khai

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

**Sau khi thanh toán thành công (QC cung cấp 26/11/2026):**
- **Hóa đơn:** gạch nợ hóa đơn qua Billing Hub.
- **Khoản thu:** không có bước gạch nợ khoản thu. Khoản thu chuyển **Đã thanh toán**, tiền vào **cọc** của hợp đồng ⇒ INVOICE xuất hóa đơn dịch vụ ⇒ **gạch nợ hóa đơn theo cọc** (xem [Khoản thu](../../../04-KHOAN-THU/quy-trinh-nghiep-vu.md)).
- **Tiền mặt tạm:** gạch nợ tạm qua Billing Hub, đẩy thông tin lên **Inside › Quản lý thu cước › Gạch nợ bổ sung** (Chưa nộp tiền) ⇒ KTV nộp tiền về công ty ⇒ **gạch nợ bổ sung** (Đã nộp tiền).

**Rule chính:**
- Thanh toán hóa đơn xa nhất trước. Tối đa 6 hóa đơn / khoản thu mỗi lần.
- Hợp đồng còn **HĐĐT / PLHĐ / BBĐT chưa ký** thì không xác nhận thu tiền được. Khách ký trên HiFPT / fpt.vn / member trước.
- Hạn mức tiền mặt: tổng tiền không vượt hạn mức còn lại. Có cấp hạn mức bổ sung theo điều kiện.
- **Tồn tạm:** tiền mặt tạm phải nộp về công ty trước 10 giờ ngày làm việc kế tiếp (thu sau 16 giờ thứ 6 thì nộp vào thứ 2). Quá hạn ⇒ MobiX **khóa thu tiền tạm và online** đến khi nộp đủ. Tồn tạm quá 48 giờ ⇒ **không cho xuất vật tư**.
- Thanh toán tạm và gạch nợ đi qua **Billing Hub (BLH)**, không qua Payment Gate (v2.9). DVKH HO gạch nợ online / gạch nợ tạm trên Fox ERP › Quản lý công nợ › Quản lý gạch nợ — xem [Gạch nợ & hậu kỳ](../../../08-GACH-NO-HAU-KY/quy-trinh-nghiep-vu.md).
- Xác nhận thanh toán gửi khách qua HiFPT hoặc Zalo / SMS (1 số điện thoại tối đa 10 lần / tháng).

## Vật tư trên MobiX

> Nguồn: `FTP_MobinetNextgen_v1.0_URD_Quanlyvattu_v1.1`, `ĐTYC_Quản lý mac theo ngày xuất`. Quy trình đầy đủ ở [Tool Quản lý vật tư](../../../10-QUAN-LY-VAT-TU/quy-trinh-nghiep-vu.md).

- KTV xem kho tạm của mình, tạo phiếu **tạm ứng** (chỉ kho chi nhánh đang trực thuộc, theo quota), **nhập trả**, **chuyển** cho nhân sự cùng chi nhánh, **nhận** vật tư được chuyển.
- Quản lý MAC theo ngày nhận (xuất trước dùng trước). Vật tư giữ quá 15 ngày ⇒ cảnh báo; từ 30 ngày ⇒ khóa tạm ứng thêm / sử dụng / chuyển, chỉ được nhập trả về kho.
