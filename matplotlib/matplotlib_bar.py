import matplotlib.pyplot as plt

payment_method = ['Debit', 'Credit', 'Cash', 'Other']
statistics = [48, 33, 9, 10]
colors = ['lightblue', 'yellowgreen', 'coral', 'gold']

plt.barh(payment_method, statistics, color=colors)

plt.xlabel('Methods')
plt.ylabel('Number of transactions (%)')
plt.title('Preferred payment methods in 2014')
plt.show()
