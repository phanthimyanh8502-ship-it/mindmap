# RULE CHỦ THỂ — SR (SERVICE REQUEST)

> Cập nhật hợp đồng sau khi bán: đổi thông tin khách hàng, chuyển địa điểm, chuyển dịch vụ, thanh lý / tạm ngưng, khôi phục dịch vụ, thanh lý trước sử dụng, khóa ứng dụng FPT Play, thủ tục thanh toán, hoàn tiền.
> Chỉ ghi quy trình tổng quan. Nguồn: 9 URD SR trong [`input/`](input/README.md).

---

## Luồng chung của một SR

SR là nơi ghi nhận yêu cầu của khách hàng và điều hướng các ticket để xử lý trọn luồng. Mỗi SR gắn với 1 hợp đồng.

Cập nhật hợp đồng có 2 tool (QC cung cấp 25/11/2026): **Inside** chỉ cập nhật thông tin khách hàng; **SR** cập nhật được nhiều hơn, theo các loại dưới đây.

| # | Bước | Hệ thống | Lưu ý |
|---|---|---|---|
| 1 | Tạo SR: chọn hợp đồng → loại yêu cầu → dịch vụ | Hệ thống SR | Màn danh sách yêu cầu › Tạo SR |
| 2 | Phân công, nhận SR | Hệ thống SR | CBQL phân công |
| 3 | Liên hệ, tư vấn khách hàng | Hệ thống SR | SR **Đang xử lý** |
| 4 | Khách đồng ý → Xử lý giao dịch | SR → Inside | Không cần liên hệ / KH không đồng ý / 3 lần không liên lạc được ⇒ **Xử lý không thành công** |
| 5 | Các ticket theo loại SR | SR, Inside | Miễn giảm, thu tiền, phát hành hóa đơn, ký kết, triển khai… |
| 6 | Gửi thông tin sang hệ thống quản trị dịch vụ / hợp đồng | Hệ thống SR | SR **Đã xử lý** |
| 7 | Khách đánh giá | HiFPT, SR | OK hoặc không đánh giá ⇒ **Đã hoàn tất**; NOT OK ⇒ ticket Xác nhận với khách hàng |

Trạng thái SR: Chưa phân công → Chưa xử lý → Đang xử lý → Đã xử lý → Đã hoàn tất, hoặc Xử lý không thành công. SR không thành công thì các ticket còn mở tự chuyển **Đã hủy**.

Thu tiền và hóa đơn (dùng chung): SR đẩy sang Inside tạo **khoản thu**. Khoản thu **Đã thanh toán** ⇒ Inside **tự phát hành hóa đơn**.

---

## Các loại SR (mỗi loại 1 tài liệu riêng)

| Loại SR | Tài liệu |
|---|---|
| SR THAY ĐỔI THÔNG TIN KHÁCH HÀNG | [`01-THAY-DOI-THONG-TIN-KH/`](01-THAY-DOI-THONG-TIN-KH/quy-trinh-nghiep-vu.md) |
| SR CHUYỂN ĐỊA ĐIỂM CÙNG TỈNH (CDD) | [`02-CHUYEN-DIA-DIEM/`](02-CHUYEN-DIA-DIEM/quy-trinh-nghiep-vu.md) |
| SR CHUYỂN DỊCH VỤ (CDV) | [`03-CHUYEN-DICH-VU/`](03-CHUYEN-DICH-VU/quy-trinh-nghiep-vu.md) |
| SR THANH LÝ / TẠM NGƯNG (TL/TN) | [`04-THANH-LY-TAM-NGUNG/`](04-THANH-LY-TAM-NGUNG/quy-trinh-nghiep-vu.md) |
| SR KHÔI PHỤC DỊCH VỤ (KPDV) | [`05-KHOI-PHUC-DICH-VU/`](05-KHOI-PHUC-DICH-VU/quy-trinh-nghiep-vu.md) |
| SR THANH LÝ TRƯỚC SỬ DỤNG (TL TSD) — CHỈ ĐƠN CHƯA THANH TOÁN | [`06-THANH-LY-TRUOC-SU-DUNG/`](06-THANH-LY-TRUOC-SU-DUNG/quy-trinh-nghiep-vu.md) |
| SR KHÓA ỨNG DỤNG FPT PLAY | [`07-KHOA-UNG-DUNG-FPT-PLAY/`](07-KHOA-UNG-DUNG-FPT-PLAY/quy-trinh-nghiep-vu.md) |
| SR THỦ TỤC THANH TOÁN | [`08-THU-TUC-THANH-TOAN/`](08-THU-TUC-THANH-TOAN/quy-trinh-nghiep-vu.md) |
| SR HOÀN TIỀN | [`09-HOAN-TIEN/`](09-HOAN-TIEN/quy-trinh-nghiep-vu.md) |
