# KÊNH W-SALE (SaleChannelID 9)

> Tách từ `RULE-CHINH-SACH-KENH-BAN.md` (nguồn: QC cung cấp 03/11/2026). Rule chung: [00-CHUNG.md](../00-CHUNG.md) · Rule XHD: [`../../../../RULE-XHD.md`](../../../../RULE-XHD.md).

## Thông tin chung

| Mục | Nội dung |
|---|---|
| Owner | HoangVT11 |
| Nơi tạo đơn | Web W-Sale — http://wsale-stag.fpt.net/ |
| Host | **Cần host** |

## Hai luồng lên đơn (user 23/11/2026: tài liệu cũ đã thay, tách 2 luồng)

| Luồng | Ai lên đơn | Dịch vụ | Nguồn |
|---|---|---|---|
| **1. Lên đơn tích hợp SOP** | W-Sale chỉ là điểm vào; lên đơn trên **SDK bán hàng của SOP** | Bán mới, Bán thêm (theo SOP) | `input/ISC_WSale_v1.6_TC V1.0_R3 (1).xlsx` — sheet Lên đơn hàng, Tích hợp SOP Click to Call, Khách hàng tiềm năng |
| **2. Swap** | Lên đơn ngay trên W-Sale, W-Sale gửi SPF | Swap Wifi 6, Swap Box Only, Swap Combo | `input/[W-Sale] - Bán hàng trên web (Bảng mapping tình trạng SOP và W-Sale).xlsx` (UC1–12, Bảng định nghĩa dịch vụ) · `input/ISC_FPT-SWAP_MODEM_WIFI6_URD_v1.0.docx` · TC v1.6 sheet Tự động tạo SR HTKT |

Tổng quan (sheet Tổng quan, bảng mapping): W-Sale là module tích hợp trên nền Web của SOP, để salesman quản lý, tiếp nhận KHTN và lên đơn trên máy tính (trước đây chỉ có trên SOP mobile).

### 1. Lên đơn tích hợp SOP (TC W-Sale v1.6, round 1–3: 22/06–01/07/2026)
1. Sale tiếp nhận **KHTN được phân phối** (menu Khách được phân phối trên SOP).
2. Mở **Chi tiết KHTN**, gọi khách qua **SOP Click to Call** (W-Sale gửi thông tin KHTN sang SOP, SOP gọi ra).
3. Nút **Cập nhật**:
   - KQTV ≠ Đồng ý hoặc chưa có KQTV ⇒ chỉ chạy UC 6 cập nhật KQTV, không mở modal lên đơn.
   - KQTV = Đồng ý ⇒ modal **Lựa chọn hình thức bán** (Bán mới / Bán thêm). Modal cũng tự mở ngay sau khi UC 6 lưu thành công với KQTV Đồng ý.
4. Chọn Bán mới / Bán thêm ⇒ **SDK bán hàng mở ở tab mới**; toàn bộ nghiệp vụ lên đơn thuộc SDK (xem luồng SOP Desktop / Mobile).
5. Lên đơn thành công ⇒ W-Sale đồng bộ: KQTV giữ Đồng ý, pipeline **Đã tạo đơn**, lịch sử tư vấn có số hợp đồng, trang Chi tiết KHTN **chỉ đọc**.
6. Hủy / thoát SDK giữa chừng ⇒ KQTV, pipeline, progress bar giữ nguyên, trang vẫn sửa được.
7. Đồng bộ theo đơn:
   - Đơn **không triển khai** bị hủy TSD ⇒ KQTV Không đồng ý, pipeline Chuyển đổi thất bại.
   - PTC **NOT_OK** ⇒ KQTV tự đổi "PTC not OK", mở nút Cập nhật KQTV, dropdown chỉ cho chọn Không đồng ý ⇒ lưu thì hệ thống **tự hủy đơn**.
   - PTC **OK** (kể cả OK lại sau NOT_OK) ⇒ KQTV Đồng ý, trang giữ chỉ đọc. Hoàn tất ⇒ Đồng ý - Hoàn tất (Chuyển đổi thành công).
8. Khoản thu, phiếu, BBĐT, xuất hóa đơn: theo luồng SOP (TC không mô tả riêng).

### 2. Swap
**Dịch vụ** (Bảng định nghĩa dịch vụ):
- **Swap Wifi 6** — Gói cơ bản / Gói nâng cao: phí nâng cấp (vd 495,000 đ), phí thay đổi hàng tháng (vd 38,500 đ), thiết bị 1 modem wifi6 + 1 AP wifi6 hoặc 1 ONU + 1 AP wifi6. Trường nhập: gói dịch vụ nâng cấp, gói tính cước, modem, AccessPoint, thu hồi thiết bị, nhân viên hưởng hoa hồng, phí Swap, tăng cước Internet, số tháng thanh toán còn lại, SĐT kích hoạt.
- **Swap Box Only** — phí nâng cấp miễn phí, FPT Playbox 650. Trường nhập: gói tính cước, số lượng box khả dụng, box, nhân viên hưởng hoa hồng, phí Swap Box.
- **Swap Combo** — modem + AP wifi6 kèm box.

**Luồng:**
1. KHTN dịch vụ Swap: KH đã có hợp đồng đang hoạt động, thiết bị NET đủ điều kiện swap. Omnisell phân công; danh sách chia giai đoạn Liên hệ / Cơ hội / Chuyển đổi.
2. Tư vấn (tab Tư vấn – Dịch vụ – Thanh toán): gọi KH, tra cứu chính sách giá, xem năng lực triển khai 7 ngày.
3. Lưu KQTV (nút Cập nhật):
   - Không đồng ý có **bộ lý do riêng cho Swap** (value 120–135, dịch vụ 28 Swap wifi 6 / 32 Swap box; vd "Không đồng ý phí chuyển đổi", "KH đã mua wifi 6").
   - Đồng ý ⇒ phải đủ trường bắt buộc và ≥1 dịch vụ; thiếu ⇒ báo lỗi, không lưu; đủ ⇒ tab Xác nhận.
4. Tab Xác nhận ⇒ **Tiếp tục** ⇒ W-Sale gửi **SPF tạo đơn**; lỗi / timeout ⇒ "Đã có lỗi xảy ra. Vui lòng thử lại sau.".
5. Tab Hẹn triển khai: chọn ngày, khung giờ theo năng lực; tải QR thanh toán.
6. Phiếu thi công (TIN/PNC).
7. **Khi nào tạo SR HTKT** (TC v1.6 sheet Tự động tạo SR HTKT; revision history: "luồng tự động tạo SR HTKT với dịch vụ Swap" — chỉ luồng Swap, luồng tích hợp SOP không có): đơn Swap ở trạng thái **chờ hoàn tất**, user role CSCT-Staff / Team Leader / Manager bấm **[Hoàn tất giao dịch]** trên W-Sale ⇒ hệ thống SR **tự tạo 1 SR HTKT** gắn SHD, trạng thái "Chưa xử lý"; đơn W-Sale chuyển **"Đã hoàn tất"**, phần "Chi tiết yêu cầu swap" chỉ đọc.
   - 1 PTC swap = đúng 1 SR, không tạo trùng; swap box nhiều lần trên 1 SHD ⇒ mỗi lần 1 SR riêng, không gộp.
   - Swap wifi: TC chỉ test lần đầu trên SHD (chưa rõ lần sau có tạo SR không).
   - Hết phiên khi bấm ⇒ giao dịch không hoàn tất, không tạo SR (TC_04.10).
   - Swap box only: Dịch vụ "FPT Play", sự cố "KH cần thay/lắp đặt, kết nối BOX".
   - Swap box combo: Dịch vụ "FPT Play, Internet", sự cố "KH cần thay/lắp đặt, kết nối BOX và Truy cập mạng chậm hoặc chập chờn".
   - Swap wifi 5/6/7 (lần đầu trên SHD): Dịch vụ "Internet", sự cố "Truy cập mạng chậm hoặc chập chờn".
8. Hoàn tất giao dịch xong mới **xuất hóa đơn** → gạch nợ. SR HTKT tạo kèm lúc hoàn tất, không phải điều kiện để xuất hóa đơn (QC xác nhận 23/11/2026).

**URD FPT Swap Modem Wifi 6** (v3.1, 21/08/2023, LOCNDP) mô tả màn tư vấn Swap trên **Inside › Chăm sóc khách hàng › Quản lý Telesales** (tìm HĐ → màn Swap Modem Wifi 6): Modem (mặc định Swap Modem Wifi 6, gói Sky, chọn thiết bị, AP, thu hồi thiết bị), Box (Swap có phí / Swap không phí có hóa đơn / Swap không phí không hóa đơn), Hẹn triển khai (ngày, khung giờ, năng lực), Thanh toán (phí Swap bắt buộc, tăng cước Internet, số tháng TT còn lại, hình thức triển khai chỉ hiển thị, tổng tiền).

### Mapping tình trạng SOP ⇄ W-Sale (sheet Bảng đề xuất mapping W-sale)
| Giai đoạn SOP | Tình trạng W-Sale |
|---|---|
| Lead · Liên hệ | Chưa tư vấn, Đã tiếp nhận, Đứt gãy, Không liên hệ được KH, KH không nghe máy, Hẹn gọi lại sau, SĐT không chính chủ |
| Cơ hội → Tư vấn | Có nhu cầu → Đồng ý, KH tiềm năng, Suy nghĩ lại · Không có nhu cầu → Không đồng ý (+ lý do con), Tình trạng khác, KH không tiềm năng, Không có hạ tầng |
| Chuyển đổi | Đã tạo đơn, Đã tạo hợp đồng, PTC not ok, Chuyển đổi thất bại, Chuyển đổi thành công = Đồng ý - Hoàn tất |

### Điểm cần hỏi
- WS-1: TC_04.7 ghi SR HTKT của Swap box có Dịch vụ "Internet", mâu thuẫn TC_04.4 ("FPT Play").
- WS-2: [Hoàn tất giao dịch] trên W-Sale có phải là hoàn tất phiếu thi công không, hay là bước riêng trước / sau PTC?
- WS-3: URD Swap Modem Wifi 6 là màn Inside telesales (2023); W-Sale hiện có thay hẳn màn này không?
- WS-5: TC_04.1–04.9 tạo SR khi bấm [Hoàn tất giao dịch], nhưng kết quả mong đợi TC_04.10 ghi "SR HTKT được tạo ở step Tạo đơn hàng". SR tạo lúc nào? Swap wifi lần 2 trên cùng SHD có tạo SR không?
- WS-4: luồng tích hợp SOP — khoản thu, PTC, BBĐT có khác gì đơn tạo thẳng trên SOP không?

## Hình thức triển khai
Đơn **chỉ có hình thức triển khai TIN/PNC** ⇒ phiếu thi công. Cách hoàn tất: [00-CHUNG.md §5.1](../00-CHUNG.md#51-hoàn-tất-phiếu-thi-công-ptc--hình-thức-tinpnc).

## Phạm vi test XHD
Chỉ bán thêm {1,7} — `RULE-XHD.md` §1.1.

## Khoản thu
Đơn W-Sale **có khoản thu** (nguồn: QC xác nhận 19/11/2026).

## Chưa có thông tin
Luồng thanh toán khoản thu chi tiết (tải QR ở tab Hẹn triển khai), use case Tích hẹn triển khai, BBĐT, đơn Swap có phiếu thi công / hình thức triển khai nào.
