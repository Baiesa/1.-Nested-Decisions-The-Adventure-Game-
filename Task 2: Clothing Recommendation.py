'''
Task 2: Clothing Recommendation
Based on the corrected code from Task 1,
further enhance the program to recommend additional items like "hat" or "boots" based on the weather.
'''

weather = input("Enter the weather sunny, rainy, or cold: ")
clothing = "sunglasses" if weather == "sunny" else "umbrella,boots,hat" if weather == "rainy" else "sweater" 
print(clothing)
if clothing == "sunglasses":
    print("Accessory recommendation: Wear sunscreen to protect your skin.")
elif clothing == "umbrella":
    print("Accessory recommendation: Bring a waterproof bag to keep your belongings dry.")
elif clothing == "sweater":
    print("Accessory recommendation: Carry a scarf for extra warmth.")




