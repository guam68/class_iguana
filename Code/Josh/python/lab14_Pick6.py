import random
from random import randint

def pick_6():
    nums = []
    for i in range(6):
        j = randint(0, 50)
        nums.append(j)
        # print(j)
    return nums
# print(pick_6())

# winning_ticket = pick_6()

# user_ticket = pick_6()

# print(winning_ticket)

# print(user_ticket)

def matching_nums(y, x):
    counter = 0
    if y[0] == x[0]:
        counter += 1
    if y[1] == x[1]:
        counter += 1
    if y[2] == x[2]:
        counter += 1
    if y[3] == x[3]:
        counter += 1
    if y[4] == x[4]:
        counter += 1
    if y[5] == x[5]:
        counter += 1
    return counter
# ticket_matches = matching_nums(winning_ticket, user_ticket)
# print(ticket_matches)
def ticket_value(matches):
    dollars = 0
    if matches == 0:
        return
    if matches == 1:
        dollars = + 4
    if matches == 2:
        dollars = + 7
    if matches == 3:
        dollars = 100
    if matches == 4:
        dollars = 50000
    if matches == 5:
        dollars == 1000000
    if matches == 6:
        dollars == 25000000
    return dollars
# print(ticket_value(ticket_matches))
# print(ticket_value(ticket_matches))

tix = int(input('How many tickets do you want?'))
counter = 0
running_total = 0
matching_tix = [0,0,0,0,0,0]
for i in range(tix):
    winning_ticket = pick_6()
    user_ticket = pick_6()
    winners = matching_nums(winning_ticket, user_ticket)
    if winners != None:
        counter += 1
        running_total += winners
        print(winners)
        print(running_total)
        if winners == 1:
            correct_nums = 0
            matching_tix[correct_nums] += 1
        if winners == 2:
            correct_nums = 1
            matching_tix[correct_nums] += 1
        if winners == 3:
            correct_nums = 2
            matching_tix[correct_nums] += 1
        if winners == 4:
            correct_nums = 3
            matching_tix[correct_nums] += 1
        if winners == 5:
            correct_nums = 4
            matching_tix[correct_nums] += 1
        if winners == 6:
            correct_nums = 5
            matching_tix[correct_nums] += 1







print(f'it cost you ${tix * 2} for {tix} tickets you had {counter} winning tickets and won ${running_total}')
print(f'{matching_tix[0]} with 1 matching number\n{matching_tix[1]} with 2 matching number\n{matching_tix[2]} with 3 matching number\n{matching_tix[3]} with 4 matching number\n{matching_tix[4]} with 5 matching number\n{matching_tix[5]} with 6 matching number\n')




