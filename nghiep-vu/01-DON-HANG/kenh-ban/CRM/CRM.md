# KÊNH CRM (SaleChannelID 13)

> Tách từ `RULE-CHINH-SACH-KENH-BAN.md` (nguồn: QC cung cấp 03/11/2026). Rule chung: [00-CHUNG.md](../00-CHUNG.md) · Rule XHD: [`../../../../RULE-XHD.md`](../../../../RULE-XHD.md).

## Thông tin chung

| Mục | Nội dung |
|---|---|
| Owner | HoangPHD |
| Nơi tạo đơn | Web CRM — https://crm-stag.fpt.net/ |
| Host | **Cần host** |
| Dịch vụ | Hiện chỉ bán **FPT Play SME** (dịch vụ FPL) — QC xác nhận 23/11/2026 |

## Cách tạo đơn
1. Tạo đơn cơ hội
2. Tạo báo giá
3. Đánh dấu version
4. Chờ 5 phút
5. Tạo đơn hàng

## Luồng theo URD Sprint 2

> Nguồn: `input/ISC_FTEL_B2B CRM V1.6_URD Sprint 2.docx` (URD B2B CRM, khởi tạo 05/06/2026, ThaoLTT84 · review HoangPHD) — B.II mục 1) Cơ hội kinh doanh và mục 4) Đơn hàng - Hủy đơn hàng, Tích hợp tạo ID khoản thu Billing Hub.

### Dịch vụ (mục 1 · Tạo cơ hội, cụm Thông tin sản phẩm/dịch vụ đề xuất)
- **Danh mục sản phẩm** (bắt buộc): URD có FPT Camera và FPT Play SME, nhưng **hiện chỉ bán FPT Play SME** (QC xác nhận 23/11/2026).
- **Sản phẩm**: nhóm dịch vụ theo Tenant, tối đa 10 dòng · **Dịch vụ quan tâm**: loại dịch vụ cụ thể, load theo Sản phẩm · phải có ≥1 dòng Sản phẩm - Dịch vụ.
- Khi kết thúc thành công: tick **Dịch vụ/Sản phẩm đã chốt** (1 hoặc nhiều, dạng Sản phẩm - Dịch vụ). Đơn hàng lấy SPDV, đơn vị, số lượng, đơn giá, VAT, gói tính cước (Tháng/Lần) theo báo giá.
- URD không liệt kê tên dịch vụ cụ thể trong từng sản phẩm.

### Cơ hội kinh doanh (mục 1)
1. Staff ghi nhận cơ hội: khách hàng cũ chọn từ danh sách, khách hàng mới nhập thông tin cơ bản (Web: menu Tạo cơ hội · Mobile: icon Tạo cơ hội ở Danh sách cơ hội).
2. Manager phê duyệt: không đủ điều kiện khai thác ⇒ kết thúc.
3. Khai thác qua các giai đoạn **Khảo sát → Demo → Chào giá → Đàm phán → Kết thúc**. Mỗi giai đoạn phải có ≥1 tracklog mới được Hoàn thành giai đoạn (BR03). Giai đoạn Chào giá ghi ngày gửi báo giá, ngày hết hiệu lực, **version bản chào giá**, kết quả (KH đồng ý / chưa đồng ý).
4. Kết thúc **thành công**: nhập số hợp đồng (tối đa 10 số, mỗi số ≤9 ký tự), SPDV đã chốt, thông tin bàn giao ⇒ sang Danh sách hợp đồng. Cơ hội thành công phải có ≥1 số hợp đồng; hợp đồng lên từ luồng tạo đơn hàng không được xóa (BR04).
5. Kết thúc **không thành công**: giai đoạn dừng lại, lý do, chi tiết nguyên nhân, mức độ tiềm năng.

### Đơn hàng (mục 4)
1. Tạo đơn hàng CRM từ version báo giá đã chốt. Mã đơn = `DH` + số đuôi cơ hội (vd `2511250001`) - XXX.
2. Mỗi địa chỉ triển khai là 1 **mã triển khai** = Số HĐ-TK X (1–9), có số hợp đồng, Order ID (SPF), SPDV phân bổ theo địa chỉ.
3. Bấm **Tạo Order ID (SPF)** ở từng mã triển khai ⇒ CRM gọi SPF tạo OrderID.
4. Bấm **Kích hoạt triển khai** (hoặc hệ thống tự kích hoạt theo luồng hiện hành) ⇒ CRM gọi tool PTC tạo **phiếu thi công**.
5. PTC trả thông tin ⇒ CRM gọi **Billing Hub** tạo **ID khoản thu** ⇒ Billing Hub trả kết quả ⇒ CRM lưu và hiển thị khoản thu.

Trạng thái đơn hàng CRM:

| Trạng thái | Điều kiện |
|---|---|
| Mới tạo | Tạo đơn thành công, mọi địa chỉ "Chưa tạo đơn hàng SPF" |
| Đang thực hiện | ≥1 địa chỉ "Đang triển khai" / "Tạm dừng triển khai" |
| Hoàn thành | Mọi địa chỉ "Hoàn tất triển khai" |
| Hủy | Mọi địa chỉ "Hủy triển khai" |

Tiền: Thành tiền dòng báo giá = Số lượng × đơn giá có VAT × số tháng tính cước; theo mã triển khai = Số lượng × đơn giá có VAT.

### Hủy TSD đơn hàng (mục 4)
- Nút Hủy TSD chỉ hiện khi các mã triển khai của đơn **chưa hoàn tất thi công**.
- Xác nhận "Bạn có chắc chắn Hủy đơn hàng này?" ⇒ hệ thống check điều kiện: thành công ⇒ đơn "Đã hủy", bắn tín hiệu tới SPF, PTC, Owner; thất bại ⇒ báo hủy thất bại.

### Điểm URD chưa rõ (cần hỏi BA)
- CRM-1: nút Kích hoạt triển khai — bảng bước ghi "gọi tool PTC khởi tạo phiếu", bảng trường ghi "gọi tạo yêu cầu kích hoạt triển khai trên SPF". Gọi tool nào?
- CRM-2: khoản thu tạo ở trạng thái nào (Chưa / Đã thanh toán), PTTT nào; khoản thu có hiện trên SPF không.
- CRM-3: BBĐT, hình thức triển khai khác PTC (quầy, Vendor) không được nhắc.
- CRM-4: "đánh dấu version, chờ 5 phút" (rule owner) không có trong URD; URD chỉ có "Version bản chào giá" ở giai đoạn Chào giá.
- CRM-5: điều kiện hủy mà hệ thống "call check" chưa được mô tả; mục bước tạo khoản thu bị đặt nhầm tiêu đề "Hủy đơn hàng".
- ✅ CRM-7: URD có danh mục FPT Camera nhưng hiện CRM chỉ bán FPT Play SME (user trả lời 23/11/2026). Còn mở: danh sách dịch vụ cụ thể trong FPT Play SME.
- CRM-6: BR04 bắt buộc ≥1 số hợp đồng khi thành công, nhưng trường Số hợp đồng ở popup Kết thúc thành công ghi Bắt buộc = N.

## Phạm vi test XHD
Ngoài scope test — `RULE-XHD.md` §1.1.
