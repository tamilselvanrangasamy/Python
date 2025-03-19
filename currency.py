rupees=int(input("Enter rupees: "))
yen=round(0.58*rupees,2)
usd=round(0.012*rupees,2)
aed=round(0.042*rupees,2)
riyal=round(0.043*rupees,2)
euro=round(0.011*rupees,2)

print(f"{rupees} rupees is equal to\n{yen} yen\n{usd} usd\n{aed} aed\n{riyal} riyal\n{euro} euro")
