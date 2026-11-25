# Input — SR THỦ TỤC THANH TOÁN

Tài liệu đầu vào của quy trình nghiệp vụ ở [`../quy-trinh-nghiep-vu.md`](../quy-trinh-nghiep-vu.md).

## Tool

### Tool thao tác, cập nhật
- **Tool SR** — Fox ERP › Service Request — tạo và xử lý SR.
- Hệ thống liên quan: Inside (khoản thu, gạch nợ), Merchant view, sổ phụ (đối soát).

## Thao tác

### Xử lý yêu cầu thanh toán của khách (SR)
1. Tạo SR: chọn loại yêu cầu theo tình trạng hợp đồng.
2. Tạo giao dịch: chọn hóa đơn, khoản thu nợ, lịch hẹn thanh toán.
3. Xử lý theo loại: đổi ngày thanh toán / gia hạn để mở dịch vụ / đối soát tiền khách đã trả / kích thanh toán tại quầy.
4. Thu tiền, gạch nợ → hóa đơn, khoản thu Đã thanh toán → SR Đã xử lý.

## Ý chính tài liệu

### `ISC_SR Thủ tục thanh toán_v.1.0_URD_v1.0.docx`
- 5 nhóm yêu cầu: thu tiền tại nhà, đổi ngày thanh toán, mở dịch vụ bị khóa (gia hạn thanh toán), kích thanh toán khi đã trả mà chưa ghi nhận, nộp tiền tại quầy.
- Gia hạn có phí; miễn phí gia hạn phải L1 SOC / TP DVKH duyệt. Đối soát qua Merchant view (online) hoặc sổ phụ (chuyển khoản) rồi gạch nợ.
- Luồng chỉ có trong hình của tài liệu.

## Nguồn

- `ISC_SR Thủ tục thanh toán_v.1.0_URD_v1.0.docx` (file nằm ở [input của SR](../../input/))
