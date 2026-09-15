from .simulator import streaks, creation_of_prediction

list_results = []

heads = 0
tails = 0

profitable_experiments = 0
losing_experiments = 0
break_even = 0

best_balance = 0
worst_balance = 0
low_balance = 0

longest_heads_streak = 0
longest_tails_streak = 0

av_balance = 0

value_head = int(input("Enter the head value: "))
value_tail = int(input("Enter the tail value: "))
range_predictions = int(input("Enter the range of predictions: "))
number_of_experiments = int(input("Enter the number of the experiments: "))

for i in range(number_of_experiments):

    predictions = creation_of_prediction(range_predictions)
    streaks_h_max, streaks_t_max = streaks(predictions)
    total_head = predictions.count("H")
    total_tail = predictions.count("T")
    av_heads = (total_head / range_predictions) * 100
    av_tails = (total_tail / range_predictions) * 100

    money_earned = total_head * value_head
    money_lost = total_tail * value_tail
    balance = money_earned - money_lost
    result = {
        "total Head": total_head,
        "total Tails": total_tail,
        "av_heads": av_heads,
        "av_tails": av_tails,
        "money_earned": money_earned,
        "money_lost": money_lost,
        "streak_h": streaks_h_max,
        "streak_t": streaks_t_max,
        "balance": balance,
    }

    list_results.append(result)


for index, i in enumerate(list_results):

    heads += i["av_heads"]
    tails += i["av_tails"]

    av_balance += i["balance"]

    if best_balance < i["balance"]:
        best_balance = i["balance"]
    if index == 0:
        worst_balance = i["balance"]
    if worst_balance > i["balance"]:
        worst_balance = i["balance"]

    if longest_heads_streak < i["streak_h"]:
        longest_heads_streak = i["streak_h"]
    if longest_tails_streak < i["streak_t"]:
        longest_tails_streak = i["streak_t"]

    if i["balance"] > 0:
        profitable_experiments += 1
    if i["balance"] < 0:
        losing_experiments += 1
    if i["balance"] == 0:
        break_even += 1


average_heads = heads / number_of_experiments
average_tails = tails / number_of_experiments

probability_profit = (profitable_experiments / number_of_experiments) * 100
probability_loss = (losing_experiments / number_of_experiments) * 100
probability_break_even = (break_even / number_of_experiments) * 100

total_balance = av_balance / number_of_experiments


print(f"Experiments: {number_of_experiments}")
print(f"Tosses per experiment: {range_predictions}")
print("")
print(f"Average_balance: {total_balance: .2f}")
print(f"")
print(f"Average heads :{average_heads: .2f} %")
print(f"Average tails : {average_tails: .2f} %")
print("")
print(f"Profitable experiments : {profitable_experiments}")
print(f"Losing experiments : {losing_experiments}")
print(f"Break-even experiments : {break_even}")
print("")
print(f"Probability of profit : {probability_profit}")
print(f"Probability of loss : {probability_loss}")
print(f"Probability of break-even : {probability_break_even}")
print(f"Best balance : {best_balance}")
if best_balance == worst_balance:
    print(f"worst balance : N/A")
if best_balance != worst_balance:
    print(f"worst balance : {worst_balance}")
print("")
print(f"Longest Heads streak : {longest_heads_streak}")
print(f"Longest Tails streak : {longest_tails_streak}")
