# RULE CHỦ THỂ — XUẤT HÓA ĐƠN

> Đồng bộ đơn hàng và xuất hóa đơn tự động (SPF → Kafka → INVOICE → Billing).
> Tách từ `../../RULE-XHD.md`; số mục (§) giữ theo file gốc.

---

> Nguồn: `qc-iia/02_analyze-requirements/v2.0/XHD/` + `HK/requirement_traceability.md` (URD rev 2.2 — `Invoice_Issuance_Architecture_v2_2_URD_v2_0.docx` §B.I.c) + các clarification (CL) đã chốt đến 23/10/2026.
> Module XHD = **Đồng bộ đơn hàng & xuất hóa đơn tự động** (SPF → Kafka → INVOICE → Billing).

---

## 1. Phạm vi

### 1.1 Kênh bán (SaleChannelID) — REQ-XHD-001
| ID | Kênh | Phạm vi test |
|---|---|---|
| 1 | Mobile | Bán mới + bán thêm, 19 nhóm (trừ nhóm 25 Prepaid 3) |
| 2 | Desktop | Bán mới + bán thêm, 19 nhóm (trừ nhóm 25 Prepaid 3) |
| 4 | DKOL | Bán mới 8 nhóm {1,4,5,6,7,9,10,21} · bán thêm 3 nhóm {1,4,7} |
| 9 | W-Sale | Chỉ bán thêm {1,7} |
| 10 | FPL (FPT Play) | Chỉ nhóm 5 — FPT Play Stands Alone · có rule riêng |
| 16 | CMR-App (FSS) | Chỉ bán mới nhóm {3} |
| 17 | Momo | Chỉ bán mới {1,7} |
| 20 | Shopee | Chỉ bán mới {1,3,5,6,7} — hồi quy Phase 1 |
| 21 | Tiktok | Chỉ bán mới {1,3,4,5,6,7} — hồi quy Phase 1 |
| 7, 11, 12, 13, 14, 15, 19 | API, VNTT, MBBank, CRM, TGDD, F-Retail, HiFPT | Ngoài scope test |
| 18 | SR-KPDV | Không test |

### 1.2 Dịch vụ — REQ-XHD-002
- 20 nhóm / 55 dịch vụ (dạng `SubServiceType – Tên dịch vụ (Type)`).
- **Loại trừ:** ServiceID 2 (SubServiceType 5–9) và ServiceID 22 (GSafe).
- Thiết bị Oncall và Thiết bị IP phone (SubServiceType 31) là **1 dịch vụ**.

### 1.3 Loại đơn — REQ-XHD-040
- Áp dụng cho cả **bán mới** và **bán thêm** (bán thêm = đơn trên hợp đồng đang hoạt động).

---

## 2. Đồng bộ đơn hàng (BR-DB)

| Rule | Nội dung |
|---|---|
| **BR-DB-01** — Sự kiện từ SPF | Chỉ 2 sự kiện: **thanh toán**, **hủy đơn**. Thời gian tạo đơn xem trên Web admin. |
| **BR-DB-02** — Tín hiệu giao hàng | Đi thẳng về INVOICE (không qua đơn SPF) từ 3 nguồn: **phiếu thi công** ("Đã xử lý hoàn tất"), **Vendor**, **phiếu giao tại quầy**. Gồm: mã đơn, ServiceCode, SubserviceType, phương thức triển khai, nguồn gửi, thời gian hoàn tất. |
| BR-DB-02 — Đơn TMĐT | Tín hiệu thanh toán = lúc SPF đánh dấu "đã thanh toán"; đồng thời ghi Paid ở trạng thái **gạch nợ tạm**. |
| **BR-DB-03** — Thông tin khách | Mặc định lấy theo **hợp đồng** tại thời điểm phát hành. |
| BR-DB-03 — Ngoại lệ FPL | Khách chọn có lấy hóa đơn không; nếu có thì tự nhập 7 trường (tên, email, SĐT, MST, mã định danh, mã quan hệ ngân sách, số hộ chiếu) trong **tối đa 2 giờ** từ lúc ghi nhận trên kênh. Không lấy / quá 2 giờ ⇒ vẫn phát hành theo thông tin hợp đồng; quá 2 giờ thì ẩn nút Xuất hóa đơn. |
| BR-DB-03 — Cập nhật thông tin | Cập nhật thông tin khách **không** kích hoạt phát hành; lần phát hành sau dùng thông tin mới nhất. |
| **BR-DB-04** — ProductType | SPF gắn sẵn **DV/TB** trên từng dòng; INVOICE dùng trường này, không tự suy diễn. |
| **BR-DB-05** — Đồng bộ nhiều lần | Lần đẩy cuối là mới nhất. Chỉ xuất phần **chưa có hóa đơn**; phần đã xuất không ghi đè / xóa / phát hành lại. Ghi thời điểm nhận bản tin để phân luồng worker/realtime. |
| **BR-DB-07** — Map tín hiệu giao hàng | Khóa 4 thành phần: **mã đơn + ServiceCode + SubserviceType + phương thức triển khai** (cho TB chưa xuất). TB đã có hóa đơn hoặc không khớp khóa ⇒ **không ghi nhận**, log vào cột Note. Không ràng buộc nguồn nào báo cho phương thức nào. |

### Hình thức triển khai → nguồn tín hiệu (REQ-XHD-043)
| HT triển khai | Nguồn tín hiệu |
|---|---|
| TIN/PNC, TIN/PNC giao hàng, FTI | Phiếu thi công |
| NCC Samsung / Sony / Casper | Vendor |
| Quầy, Sale | Phiếu giao tại quầy |
| Không / None | Qua phiếu quầy; quầy không gửi ⇒ không xuất hóa đơn |

- Đơn có ≥1 SPDV mix TIN/PNC ⇒ cả đơn đi luồng TIN/PNC. Mix "Không" + TIN/PNC ⇒ theo phiếu thi công.

---

## 3. Lịch xuất hóa đơn & phân luồng

### 3.1 BR-XHD-01 — Lịch (tham số cấu hình, không hardcode)
- **Mọi kênh trừ FPL:** 2 đợt/ngày — đợt 1 chốt **12:00** chạy **12:05**; đợt 2 chốt **18:00** chạy **18:05**.
- Mỗi đợt quét dòng **chưa xuất** có mốc nghiệp vụ **trong ngày, trước giờ chốt**.
- Đủ điều kiện **sau giờ chốt cuối của ngày cuối tháng** ⇒ phát hành sang **tháng sau** (vd: tín hiệu về 00:01 ngày 01/11 ⇒ đợt 12:05 ngày 01/11, BillDate = 01/11).
- **Kênh FPL:** worker **2 giờ/lần** (0h–2h, 2h–4h, …) + mốc **22:05** chốt dữ liệu 0h–22h.

### 3.2 BR-XHD-02 — Phân luồng
- Tín hiệu về **trước giờ chốt** đợt ⇒ **worker**.
- Tín hiệu về **sau giờ chốt cuối** trong ngày ⇒ **realtime** (FPL: sau **22h**).
- Worker lọc theo mốc nghiệp vụ; realtime lọc theo thời điểm nhận tín hiệu — 2 luồng không trùng.

---

## 4. Điều kiện phát hành (BR-XHD-03)

| Đối tượng | Điều kiện |
|---|---|
| **Dịch vụ (DV)** | Có tín hiệu **"đã thanh toán"** từ SPF |
| **Thiết bị (TB)** | Có tín hiệu **giao hàng hoàn tất** của phương thức triển khai tương ứng; chỉ phát hành TB có trong tín hiệu |
| DV và TB | Xét **độc lập**, dùng chung mọi kênh |
| **Đơn TMĐT** | DV khi SPF đánh dấu "đã thanh toán"; TB khi giao hàng thành công |
| **Kênh FPL** | Delay **2 giờ** tính từ thời gian tạo đơn — áp cả DV và TB |
| **Hợp đồng tổ chức** (KH cấp 1 = Tổ chức) | Chỉ phát hành khi **đã duyệt PĐK** (lấy từ SPF); **2 ngày lịch cuối tháng** không xét. Chưa duyệt ⇒ chặn, ghi log, phải xuất tay (đợt sau không tự phát hành). Đơn bán thêm phải duyệt PĐK mới của đơn đó. |
| **Hợp đồng con** (có gắn hợp đồng cha/dự án) | **Không phát hành** cả DV và TB |
| **Hợp đồng SST / hợp đồng nghiệp vụ** | **Không tự động xuất hóa đơn** (yêu cầu BA 23/10/2026, ngoài URD) |

---

## 5. Gộp hóa đơn

| Rule | Nội dung |
|---|---|
| **BR-XHD-05** — Worker | Trong cùng đợt, các dòng DV/TB đủ điều kiện của **cùng một đơn** gộp vào **1 hóa đơn**. Chỉ 1 thành phần đủ điều kiện ⇒ xuất phần đó, phần còn lại chờ đợt sau. Chi nhánh không phải tiêu chí tách. |
| **BR-XHD-06** — Realtime | **Không gộp**. Mỗi tín hiệu chỉ phát hành đúng thành phần của nó (thanh toán ⇒ DV; giao hàng ⇒ TB của phương thức đó). Xử lý ngay, không chờ worker. |

---

## 6. Điều kiện hợp lệ của đơn (BR-XHD-10)

Đơn chỉ được xuất hóa đơn khi:
- **Đơn hợp lệ:** không bị hủy, không đang cập nhật.
- **Hợp đồng hợp lệ:** hợp đồng còn hiệu lực.
- **Đủ thông tin chung:** sale team, kênh bán, tên khách hàng, loại hình khách hàng, địa chỉ xuất hóa đơn, địa bàn (LocationID).
- **Đủ thông tin dịch vụ:** dịch vụ, nhóm dịch vụ, gói dịch vụ, chính sách, câu lệnh giá, CTKM đều phải có giá trị hợp lệ (> 0).

Không hợp lệ ⇒ **không xuất hóa đơn** và ghi log; hệ thống không giữ lại để xuất sau.

---

## 7. Phát hành hóa đơn (BR-XHD-12, 13, 14)

- Hóa đơn được phát hành qua **Billing System**, ghi nhận **số hóa đơn (BillNumber)** và **ngày hóa đơn (BillDate** = ngày phát hành thực tế).
- **Chi nhánh xuất hóa đơn** = chi nhánh quản lý hợp đồng.
- **Nội dung hóa đơn:** tên dịch vụ + số tháng sử dụng.
- **Một đơn có thể có nhiều hóa đơn** (dịch vụ và thiết bị xuất ở các đợt khác nhau).
- **Kiểm tra hóa đơn đã xuất:** Inside › **Quản lý kế toán › Liệt kê cước** (QC cung cấp 25/11/2026).
- Sau khi phát hành, INVOICE gửi bản tin báo hóa đơn đã phát hành (**Invoice Event**) để chuyển sang **gạch nợ** và **hậu kỳ**.

---

**Sau khi phát hành:** hệ thống phân bổ doanh thu của hóa đơn, xem [Phân bổ doanh thu](../13-PHAN-BO-DOANH-THU/quy-trinh-nghiep-vu.md).
