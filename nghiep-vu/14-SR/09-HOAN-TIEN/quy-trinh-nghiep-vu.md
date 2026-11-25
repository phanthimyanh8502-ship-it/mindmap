# RULE — SR HOÀN TIỀN

> Một loại SR của [SR](../quy-trinh-nghiep-vu.md); luồng chung (tạo, phân công, liên hệ, đánh giá) xem ở đó.

Nguồn: URD SR Hoàn tiền v1.0, §B.II.

- Tạo từ **SR cha**: thanh lý trước sử dụng, thanh lý sau sử dụng hoặc khiếu nại; SR cha đang Đang xử lý / Đã xử lý / Đã hoàn tất. Tồn cọc phải lớn hơn hoặc bằng tiền cần hoàn.

| # | Bước | Hệ thống |
|---|---|---|
| 1 | Tạo SR hoàn tiền theo mã SR cha, phân công | Hệ thống SR |
| 2 | Xử lý giao dịch: chọn nguyên nhân, giao dịch đã thanh toán cần hoàn (3 năm gần nhất), số tiền **âm cọc** | Hệ thống SR |
| 3a | **Chuyển khoản**: chủ tài khoản khác chủ hợp đồng thì GĐCN duyệt → đề nghị hoàn tiền chuyển sang **ePayment** → ePayment duyệt OK thì gửi SMS hoàn tiền; NOT OK cho gửi lại, quá 3 lần thì hoàn cọc, SR không thành công | ePayment |
| 3b | **Online**: HO duyệt đề nghị → cập nhật kết quả hoàn tiền từ đối tác (import) → OK thành công, NOT OK không thành công | DVKH HO |
| 4 | Khách đánh giá, xử lý CSAT 1,2 | Hệ thống SR |
