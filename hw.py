def shutdown():
  user_input = input("Enter 'Yes' or 'No': ")

  if user_input == "Yes"or user_input=="yes":
    print("shutting down")
  elif user_input == "No"or user_input=="no":
      print("abort shut down")
  else:
    print("sorry")
shutdown()
