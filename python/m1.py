import matplotlib.pyplot as plt

# Days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Example temperatures (°C)
temperatures = [28, 30, 32, 31, 29, 27, 26]

# Create the plot
plt.plot(days, temperatures, marker='o', color='orange', linestyle='-', linewidth=2)

# Add title and labels
plt.title("Daily Temperature for One Week")
plt.xlabel("Days of the Week")
plt.ylabel("Temperature (°C)")

# Show grid
plt.grid(True, linestyle='--', alpha=0.6)

# Display the plot
plt.show()
