#Prompts user for weather input
weather = str(input("What's the weather like today? (sunny/rainy/cold): "))

#Provides clothing recommendations based on user input.
if weather == 'sunny':
    print("Wear a t-shirt and sungglasses.")
elif weather == 'rainy': 
      print("Don't forget your umbrella and a raincoat.")
elif weather == 'cold':
      print("Make sure to wear a warm coat and a scarf.")
else:
      print("Sorry, I don't have any recommendations for this weather.")