horiscope_dict = {'January': 'Aries', 'February': 'Taurus', 'March': 'Gemini', 'Aprul': 'Cancer', 'May': 'Leo', 'June': 'Virgo', 'July': 'Libra', 'August': 'Scorpio', 'September': 'Sagittarius', 'October': 'Capricorn', 'November': 'Aquarius', 'December': 'Pisces'}

user_month = input("Which month are you born in?")

if user_month in horiscope_dict:
    x = horiscope_dict[user_month]
    print(f"Your star sign might be {x}")
