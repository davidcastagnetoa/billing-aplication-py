def golden_ratio_width(height: float):
    phi = 1.61803398875
    width = height * phi
    return width

height = float(input("Enter height: "))
print(f"width : {golden_ratio_width(height)} ")