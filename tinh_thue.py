def tinh_thue_bac_thang(thu_nhap_tinh_thue):
    """Tính thuế TNCN dựa trên biểu thuế lũy tiến từng phần (tháng)"""
    if thu_nhap_tinh_thue <= 0:
        return 0
    
    # Biểu thuế: (Mức trần, Thuế suất, Khoản giảm trừ nhanh)
    bieu_thue = [
        (5000000, 0.05, 0),
        (10000000, 0.10, 250000),
        (18000000, 0.15, 750000),
        (32000000, 0.20, 1950000),
        (52000000, 0.25, 4750000),
        (80000000, 0.30, 9750000),
        (float('inf'), 0.35, 18150000)
    ]
    
    for muc_tran, thue_suat, giam_tru_nhanh in bieu_thue:
        if thu_nhap_tinh_thue <= muc_tran:
            return thu_nhap_tinh_thue * thue_suat - giam_tru_nhanh
    return 0

def phan_mem_tinh_thue():
    # --- CHỨC NĂNG 1: Thiết lập hạn mức miễn trừ ---
    mien_tru_ban_than = 11000000  # 11 triệu
    mien_tru_phu_thuoc = 4400000  # 4.4 triệu

    # --- CHỨC NĂNG 2: Thiết lập tham số người lao động ---
    print("=== THIẾT LẬP THÔNG TIN NGƯỜI LAO ĐỘNG ===")
    ten = input("Nhập tên người lao động: ")
    nam = input("Nhập năm tính thuế: ")
    while True:
        try:
            so_npt = int(input("Nhập số người phụ thuộc: "))
            break
        except ValueError:
            print("Vui lòng nhập số nguyên.")

    # Tổng miễn trừ hàng tháng
    tong_mien_tru_thang = mien_tru_ban_than + (so_npt * mien_tru_phu_thuoc)
    
    # --- CHỨC NĂNG 3: Nhập thu nhập từng tháng ---
    thu_nhap_thang = [0] * 12
    thue_tam_nop_thang = [0] * 12
    
    print(f"\n=== NHẬP THU NHẬP NĂM {nam} ===")
    print("(Nhập '0' hoặc nhấn Enter bỏ qua nếu tháng đó không có thu nhập)")
    
    for i in range(12):
        try:
            nhap = input(f"Thu nhập tháng {i+1}: ")
            thu_nhap = float(nhap) if nhap else 0
            thu_nhap_thang[i] = thu_nhap
            
            # Tính thuế TNCN tạm nộp của tháng
            thu_nhap_tinh_thue = thu_nhap - tong_mien_tru_thang
            thue_tam_nop_thang[i] = tinh_thue_bac_thang(thu_nhap_tinh_thue)
        except ValueError:
            print("Dữ liệu không hợp lệ, coi như thu nhập bằng 0.")

    # --- CHỨC NĂNG 4: Quyết toán thuế cả năm ---
    tong_thu_nhap_nam = sum(thu_nhap_thang)
    tong_thue_da_tam_nop = sum(thue_tam_nop_thang)
    
    # Quyết toán: Tính trên tổng thu nhập cả năm và tổng miễn trừ cả năm
    tong_mien_tru_nam = tong_mien_tru_thang * 12
    tn_tinh_thue_nam = tong_thu_nhap_nam - tong_mien_tru_nam
    
    # Thuế thực tế tính bằng cách lấy trung bình tháng rồi nhân 12 (đúng luật quyết toán)
    thue_thuc_te_nam = tinh_thue_bac_thang(tn_tinh_thue_nam / 12) * 12 if tn_tinh_thue_nam > 0 else 0
    tien_thue_chenh_lech = tong_thue_da_tam_nop - thue_thuc_te_nam

    # IN KẾT QUẢ
    print("\n" + "="*50)
    print(f"BẢNG QUYẾT TOÁN THUẾ TNCN NĂM {nam}")
    print(f"Nhân viên: {ten}")
    print(f"Số người phụ thuộc: {so_npt}")
    print(f"Mức miễn trừ gia cảnh/tháng: {tong_mien_tru_thang:,.0f} VND")
    print("-" * 50)
    print(f"{'Tháng':<10} | {'Thu nhập':>15} | {'Thuế tạm nộp':>15}")
    print("-" * 50)
    
    for i in range(12):
        print(f"Tháng {i+1:<5} | {thu_nhap_thang[i]:>15,.0f} | {thue_tam_nop_thang[i]:>15,.0f}")
    
    print("-" * 50)
    print(f"Tổng thuế TNCN đã tạm nộp:    {tong_thue_da_tam_nop:>15,.0f} VND")
    print(f"Thuế TNCN thực tế cả năm:     {thue_thuc_te_nam:>15,.0f} VND")
    
    if tien_thue_chenh_lech > 0:
        print(f"Số tiền thuế bạn nhận lại:    {tien_thue_chenh_lech:>15,.0f} VND")
    elif tien_thue_chenh_lech < 0:
        print(f"Số tiền thuế phải nộp thêm:   {abs(tien_thue_chenh_lech):>15,.0f} VND")
    else:
        print("Trạng thái: Đã nộp đủ thuế, không chênh lệch.")
    print("="*50)

if __name__ == "__main__":
    phan_mem_tinh_thue()