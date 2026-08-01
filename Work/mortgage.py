# # mortgage.py
# #
# # Exercise 1.7

# principal = 500000.0
# rate = 0.05
# payment = 2684.11
# total_paid = 0.0
# extra_payment_start_month = 61
# extra_payment_end_month = 108
# extra_payment = 1000

# months = 0
# while principal > 0:
#     months = months + 1
#     payment_modified = payment
#     if months >= extra_payment_start_month and months <= extra_payment_end_month:
#         payment_modified = payment + extra_payment
#     principal = principal * (1+rate/12) - payment_modified
#     total_paid = total_paid + payment_modified

# print(f'''Total paid: {round(total_paid, 2)}
# Months: {months}''')
# # print('Total paid', round(total_paid, 2))
# # print('Months', months)

# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid', total_paid)
