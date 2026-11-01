print("======== Parking Fee System ========")
begin_hr = int(input("Begin_H:"))
begin_min = int(input("Begin_M:"))
end_hr = int(input("End_H:"))
end_min = int(input("End_M:"))
print("====================================")

# 停車2小時以內，每半小時10元
# 超過2小時以上的部份，每半小時30元
# 不滿30分鐘免費

parking_fee = 0

# 總分鐘
begin_total = (begin_hr * 60) + begin_min
end_total = (end_hr * 60) + end_min
total_min = end_total - begin_total

# 小時和分鐘
split_h = total_min // 60
split_m = total_min % 60

if total_min >= 120:
  # 扣除滿2小時外的半小時價格
  extrac_half_hr = (total_min - 120) // 30
  parking_fee = 40 + extrac_half_hr * 30

elif total_min < 120:
  # 計算2小時內，半小時有滿的價格
  half_hr = total_min // 30
  parking_fee = half_hr * 10

else:
  # 未滿30分鐘價格
  parking_fee = 0

print(f"*** Interval: {total_min} mins ({split_h}H {split_m}M)")
print(f"*** Parking Fee: {parking_fee}")