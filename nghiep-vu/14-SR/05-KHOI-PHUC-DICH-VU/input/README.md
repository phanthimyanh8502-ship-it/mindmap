# Input — SR KHÔI PHỤC DỊCH VỤ (KPDV)

Tài liệu đầu vào của quy trình nghiệp vụ ở [`../quy-trinh-nghiep-vu.md`](../quy-trinh-nghiep-vu.md).

## Tool

- **Tool SR** — Fox ERP › Service Request — tạo và xử lý SR.
- Hệ thống liên quan: SPF (đơn hàng, thu tiền), Inside (phát hành hóa đơn).

## Thao tác

### Bật lại dịch vụ đã ngưng (SR)
1. Tạo SR: chọn hợp đồng, dịch vụ Chủ thuê bao đi vắng / Đã chấm dứt.
2. Liên hệ, tư vấn khách.
3. Xử lý giao dịch: chọn gói, câu lệnh giá (lấy lại câu lệnh cũ nếu còn hiệu lực).
4. Xử lý ticket duyệt nếu có: thiết bị, thay đổi câu lệnh giá, miễn giảm.
5. Đơn hàng SPF thu tiền → cấu hình từ xa, phát hành hóa đơn → SR Đã xử lý.

## Ý chính tài liệu

### `ISC-FTEL Service Request V1.2 - KPDV_URD V1.0_02082024.docx` · `ISC_Service-Request-Transaction_v.1.2_URD_v1.0_22082024.docx`
- SR **khôi phục dịch vụ (KPDV)** cho dịch vụ Chủ thuê bao đi vắng hoặc Đã chấm dứt hợp đồng.
- Lấy lại câu lệnh giá cũ nếu còn hiệu lực; tổng thanh toán = cước khôi phục + cước tháng cũ.
- Sinh đơn hàng SPF để thu tiền; thanh toán xong thì cấu hình từ xa (bật lại dịch vụ) và phát hành hóa đơn.
- File Transaction là màn xử lý giao dịch của KPDV, không phải luồng chung của mọi SR.

## Nguồn

- `ISC-FTEL Service Request V1.2 - KPDV_URD V1.0_02082024.docx` (file nằm ở [input của SR](../../input/))
- `ISC_Service-Request-Transaction_v.1.2_URD_v1.0_22082024.docx` (file nằm ở [input của SR](../../input/))
