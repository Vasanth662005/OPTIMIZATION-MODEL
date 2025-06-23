#  Linear Programming using PuLP
from pulp import LpMaximize, LpProblem, LpVariable, value

# Create the model
model = LpProblem("Maximize_Profit", LpMaximize)

# Define decision variables
x = LpVariable("Product_A", lowBound=0)
y = LpVariable("Product_B", lowBound=0)

# Objective function
model += 60 * x + 40 * y, "Total_Profit"

# Constraints
model += 2 * x + 1 * y <= 100, "Machine_1_Hours"
model += 1 * x + 1 * y <= 80, "Machine_2_Hours"

# Solve the problem
model.solve()

# Results
print(f"Status: {model.status}")
print(f"Optimal number of Product A: {x.varValue}")
print(f"Optimal number of Product B: {y.varValue}")
print(f"Maximum Profit: INR {value(model.objective)}")