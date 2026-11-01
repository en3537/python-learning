try:
  result = 8 / 0
except:
  message = "發生錯誤，假設結果為 -999"
  result = -999
else:
  message = "順利執行"
finally:
  print("=== 實驗完成 ===")
print("實驗結果:", message)
print("result =", result)