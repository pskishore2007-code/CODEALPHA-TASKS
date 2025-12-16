
CODE:
import matplotlib.pyplot as plt  
months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 120, 90, 150]

plt.plot(months, sales, marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
 


 NOTES:
 - Seaborn:
- Built on Matplotlib, adds beautiful defaults and statistical plots.
