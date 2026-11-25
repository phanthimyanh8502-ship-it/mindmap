# RULE CHỦ THỂ — PHÂN BỔ DOANH THU

> Sau khi xuất hóa đơn, hệ thống phân bổ doanh thu của hóa đơn vào các tháng khách dùng dịch vụ.
> Nguồn: `phan-bo-doanh-thu/00_input/v1.0/Doc/Phan_bo_doanh_thu_v1_0_PRD_v1_1.docx` (PRD v1.1, chốt 12/11/2026) và phân tích ở `phan-bo-doanh-thu/02_analyze-requirements/v1.0/` (4 module PBD, PBA, BCT, BCPB).
> Liên quan: [Xuất hóa đơn](../07-XUAT-HOA-DON/quy-trinh-nghiep-vu.md) (S-01 là bước phát hành hóa đơn).

---

## 1. Thuật ngữ

| Thuật ngữ | Ý nghĩa |
|---|---|
| Phân bổ dương | Chia doanh thu của hóa đơn vào các tháng sử dụng dịch vụ |
| Phân bổ âm | Ghi giảm doanh thu đã hoặc sẽ phân bổ khi có điều chỉnh giảm hóa đơn |
| Kỳ hạn hóa đơn | Từ ngày – đến ngày của hóa đơn. Có hóa đơn xác định được ngay lúc xuất (vd hóa đơn gia hạn), có hóa đơn chỉ ghi số tháng dùng |
| Danh sách chờ phân bổ (treo) | Dịch vụ đã xuất hóa đơn nhưng chưa active nên chưa được phân bổ |
| Dịch vụ hóa đơn | Các dòng cùng một dịch vụ trên một hóa đơn (nhiều gói con, nhiều số lượng), xét chung một nhóm khi phân bổ |
| Ngày active | Ngày dịch vụ kích hoạt thành công. Internet: ngày online (FirstAccess) |
| ĐCG | Điều chỉnh giảm hóa đơn |
| Khóa sổ | Kế toán chốt doanh thu tháng T vào ngày 02 tháng T+1 (vd 02/10 chốt tháng 9); sau đó không ghi thêm vào tháng T |

**Phạm vi áp dụng:** lên pilot cùng dự án quy hoạch xuất hóa đơn. Xuất hóa đơn mở tới tỉnh / chi nhánh nào thì phân bổ dương mở theo tới đó (hóa đơn phải có trong bảng dữ liệu hóa đơn IIA). B2B và B2C dùng chung cơ chế.

---

## 2. Các bước (PRD §5.2)

| ID | Bước | Actor | Mô tả | Kết quả |
|---|---|---|---|---|
| S-01 | Xuất hóa đơn | Hệ thống PHHĐ | Giao hàng hoàn tất hoặc thanh toán hoàn tất ⇒ xuất hóa đơn | Có hóa đơn |
| S-02 | Xét dịch vụ | Hệ thống | Dịch vụ có trong danh mục cần phân bổ không? | Không có thì không chia |
| S-03 | Kiểm tra kỳ hạn | Hệ thống | Lúc xuất đã xác định được kỳ hạn ⇒ chia như hiện nay | Biết đi luồng cũ hay mới |
| S-04 | Kiểm tra active | Hệ thống | Đã active ⇒ chia luôn (S-06) | Biết treo hay chia ngay |
| S-05 | Treo | Hệ thống | Chưa active ⇒ đưa vào danh sách chờ | Hóa đơn nằm trong báo cáo treo |
| S-06 | Phân bổ dương | Hệ thống | Chia doanh thu từ ngày active, đủ số tháng | Đánh dấu **Đã phân bổ** |
| S-07 | Điều chỉnh giảm | Bộ phận điều chỉnh hóa đơn | Phát sinh hóa đơn điều chỉnh giảm | Cần trừ doanh thu |
| S-08 | Phân bổ âm | Hệ thống | Hóa đơn gốc đã chia: trừ ngay, từ tháng xa nhất. Còn treo: treo khoản giảm, chia xong mới trừ | Khoản giảm ghi riêng |
| S-09 | Xem báo cáo | Người dùng báo cáo | Xem báo cáo treo và báo cáo kế toán | Biết tiền đang treo và đã chia |

---

## 3. Phân bổ dương (module PBD · BR-01 → BR-07)

| BR | Nội dung |
|---|---|
| **BR-01** — Danh mục phân bổ | Hợp đồng **FTI (chi nhánh 90)** không phân bổ. Hợp đồng còn lại: chỉ chia dịch vụ nằm trong danh mục cần phân bổ; một hóa đơn có thể có cả dịch vụ cần và không cần phân bổ |
| **BR-02** — Dịch vụ hóa đơn | Một dòng trong nhóm active thì cả nhóm chia từ ngày đó; dòng active sau không đổi gì. Gói con khác số tháng: chung ngày bắt đầu, mỗi gói kết thúc riêng |
| **BR-03** — Đã có kỳ hạn lúc xuất | Chia theo kỳ hạn như hiện nay, không tra active, không treo. Chưa có kỳ hạn ⇒ dùng thông tin active, đi luồng mới (BR-04 → BR-07). ✅ Chốt 19/11/2026 (bạn): **theo workflow** Hình 1 — xét dịch vụ (S-02) ⇒ kiểm tra kỳ hạn (S-03) ⇒ kiểm tra active (S-04). Workflow không có điều kiện "kỳ hạn phải vắt sang tháng sau" nên không áp dụng |
| **BR-04** — Treo khi chưa active | Đã active khi xuất ⇒ chia luôn. Chưa active ⇒ treo, chưa tính doanh thu; active mới chia. Ngày bắt đầu chia = ngày active |
| **BR-05** — Khóa sổ | Active trong tháng T, dữ liệu về trễ: chấp nhận đến hết ngày 01 tháng T+1, phân bổ vào tháng T. Về từ ngày 02 tháng T+1: vẫn ở danh sách chờ, có cảnh báo, vận hành phân bổ thủ công vào tháng đang mở |
| **BR-06** — Kỳ chia | Từ ngày active. Tháng dương lịch: ngày active + số tháng − 1 ngày. Tháng 30 ngày: ngày active + số tháng × 30 − 1 ngày |
| **BR-07** — Chia theo số ngày | Chia trên tiền trước VAT (VAT, tổng tiền chia cùng cách). Tiền 1 ngày = tổng tiền ÷ số ngày (làm tròn đến đồng). Tháng lẻ = số ngày dùng × tiền 1 ngày. Tháng trọn chia đều phần còn lại |

**Ví dụ (AC-01.1.01):** gói 6 tháng, 6.000.000đ trước VAT, tháng dương lịch, active 15/08/2026 ⇒ phân bổ 15/08/2026 → 14/02/2027 (184 ngày). Tháng 30 ngày ⇒ 15/08/2026 → 10/02/2027 (180 ngày).

---

## 4. Phân bổ âm (module PBA · BR-08 → BR-12)

| BR | Nội dung |
|---|---|
| **BR-08** — Trừ từ tháng xa nhất | Khoản giảm tính trên tổng tiền dịch vụ, ghi riêng; trừ từ tháng xa nhất lùi về |
| **BR-09** — Gốc treo thì giảm treo | Hóa đơn gốc còn treo ⇒ khoản giảm cũng treo; gốc chia xong mới trừ |
| **BR-10** — Tối đa 3 lần | Lần sau trừ trên phần còn lại; tổng giảm không vượt tổng đã chia; nhiều khoản giảm đang treo thì trừ lần lượt |
| **BR-11** — Hóa đơn bị thay thế | Hóa đơn cũ chuyển **Đã hủy**, ghi âm toàn bộ: đã chia ⇒ phân bổ âm; còn treo ⇒ treo âm, triệt tiêu treo dương. ⚠️ Chờ chốt: phần ở tháng đã qua ghi âm 1 lần tại tháng hiện tại hay giữ rule cũ |
| **BR-12** | Không làm điều chỉnh 0đ đổi kỳ hạn trong phiên bản này |

---

## 5. Báo cáo (menu mới **Inside › Quản lý kế toán › Master doanh thu** — đường dẫn: QC cung cấp 25/11/2026)

### 5.1 Báo cáo treo (module BCT · BR-13 → BR-17) — Inside › Quản lý kế toán › Master doanh thu › Báo cáo treo
- **BR-13:** chỉ gồm dịch vụ chưa active của hóa đơn đi luồng mới (tính theo từng dịch vụ) và các hóa đơn điều chỉnh liên quan.
- **BR-14:** tháng này xem đến hiện tại, tháng trước xem số đã chốt.
- **BR-15:** báo cáo tổng hợp 4 nhóm **Còn lại · Phát sinh · Đã điều chỉnh · Đã thay thế**; mỗi chi nhánh 1 dòng, có dòng tổng khu vực và toàn quốc; mỗi nhóm gồm Số hóa đơn, Doanh thu (trước VAT), VAT, Tổng tiền.
- **BR-16:** bấm số hóa đơn ở nhóm nào thì mở danh sách chi tiết của nhóm đó.
- **BR-17:** dịch vụ đã online mà chưa chia ⇒ cột Cảnh báo ghi "Đã online, chưa phân bổ" (chữ, không tô màu, xuất Excel vẫn giữ).

### 5.2 Báo cáo doanh thu phân bổ (module BCPB · BR-18 → BR-20) — Inside › Quản lý kế toán › Master doanh thu › Báo cáo doanh thu phân bổ
- **BR-18:** chuyển từ menu cũ *Báo cáo doanh thu › BC kế toán › PB Doanh thu*; giống báo cáo cũ (cùng bộ lọc, cột, cách trình bày), thêm 3 cột **DT chờ phân bổ · Đã phân bổ · DT phân bổ trong kỳ**.
- **BR-19:** tiền treo ghi 1 lần ở tháng phát hành; xuất và chia trong cùng tháng thì chỉ hiện ở cột cũ.
- **BR-20:** báo cáo treo và báo cáo kế toán phải khớp: tiền còn treo đến 1 tháng = tổng DT chờ phân bổ − tổng Đã phân bổ đến tháng đó = Doanh thu nhóm Còn lại trên báo cáo treo tổng hợp cùng kỳ.

**Phân quyền:** theo HRIS và Fox ERP.

---

## 6. Ngoài phạm vi
Điều chỉnh 0đ đổi kỳ hạn · các kiểu điều chỉnh giảm khác (thanh lý ngừng phân bổ, chia đều theo lịch…) · nâng/hạ gói đổi kỳ hạn · hóa đơn treo lâu (tạm để treo) · nghiệp vụ điều chỉnh hóa đơn · hợp đồng FTI (chi nhánh 90).
