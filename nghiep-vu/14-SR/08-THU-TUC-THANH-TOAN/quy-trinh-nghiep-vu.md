# RULE — SR THỦ TỤC THANH TOÁN

> Một loại SR của [SR](../quy-trinh-nghiep-vu.md); luồng chung (tạo, phân công, liên hệ, đánh giá) xem ở đó.

Nguồn: URD SR Thủ tục thanh toán v1.0, §C.I (bảng map loại yêu cầu + 5 lưu đồ dạng hình).

| Loại yêu cầu | Điều kiện hợp đồng | Luồng |
|---|---|---|
| Thu tiền tại nhà | Khác Đã chấm dứt | Đổi ngày / gia hạn nếu cần → nhân viên thu cước thu tiền |
| Thay đổi ngày thanh toán (duy trì / chỉ trong tháng T) | Billing, Bình thường | Đổi ngày khóa cước → có tiền phải thu thì thu tiền |
| Yêu cầu mở dịch vụ (đã bị khóa) | Billing, Ngưng vì lý do thanh toán | **Gia hạn thanh toán** (mở dịch vụ, có phí gia hạn; miễn phí thì L1 SOC / TP DVKH duyệt) → đối soát → thu tiền |
| Yêu cầu kích thanh toán (chưa bị khóa) | Bình thường | Đối soát: tiền online kiểm Merchant view → gạch nợ online; chuyển khoản kiểm sổ phụ → gạch nợ chuyển khoản; chưa trả thì tư vấn → thu tiền |
| Nộp tiền tại quầy | Mọi tình trạng | Kích thanh toán tiền mặt tại quầy: hóa đơn, khoản thu tự **Đã thanh toán** |

Kết thúc chung: hóa đơn, khoản thu Đã thanh toán → SR Đã xử lý (hợp đồng Ngưng vì lý do thanh toán về Bình thường) → khách đánh giá → Đã hoàn tất.
