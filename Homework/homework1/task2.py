
total_value = 2.36 # this is a dollar amount
value_in_cents = 100 * total_value # value of the dollar amount in cents

value_of_q = 25
value_of_d = 10
value_of_n = 5
value_of_p = 1

number_of_q = value_in_cents // value_of_q

remaining_balance = value_in_cents % value_of_q

number_of_dimes = remaining_balance // value_of_d

remaining_balance = remaining_balance % value_of_d

number_of_n = remaining_balance // value_of_n

remaining_balance = remaining_balance % value_of_n

number_of_pennies = remaining_balance // value_of_p

print(f"""You will get {number_of_q} amount quarters, {number_of_dimes} amount of dimes,
{number_of_n} amount of nickels and lastly you will get {number_of_pennies} amount of 
pennies.""")


























