def mothers_day():
  return "Happy Mother's Day, Mom!"

def better_mothers_day(name):
  return "Happy Mother's Day, {}!".format(name)

def best_mothers_day(name="Mom"):
  return "Happy Mother's Day, {}!".format(name)

def holiday_greeting(recipient = "Mom", sender = "Your Favorite Child", occasion = "Mother's Day"):
  return "Happy {}, {}! - From {}".format(occasion, recipient, sender)