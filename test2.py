from datetime import datetime

t_now = datetime.now()
t_9 = t_now.replace(hour=9, minute=0, second=0, microsecond=0)
t_start = t_now.replace(hour=9, minute=5, second=0, microsecond=0)
t_sell = t_now.replace(hour=15, minute=15, second=0, microsecond=0)
t_exit = t_now.replace(hour=15, minute=20, second=0,microsecond=0)
today = datetime.today().weekday()
print('t_now: ' + str(t_now))
print('t_9: ' + str(t_9))
print('t_start: ' + str(t_start))
print('t_sell: ' + str(t_sell))
print('t_exit: ' + str(t_exit))
print('week: ' + str(today))




# myList = ["a", "b", "c"]

# print(len(myList))

# print(1 <= 1)