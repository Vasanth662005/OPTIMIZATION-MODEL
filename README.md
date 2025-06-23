# OPTIMIZATION-MODEL

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: N VASANTHA KUMAR

*INTERN ID*: CT08DG148

*DOMAIN*: Data Science

*DURATION*: 8 WEEKS

*MENTOR*: NEELA SANTOSH


# Data Science Internship Task 4 — Product Mix Optimization

**Internship Organization:** CODTECH  
**Intern Name:** Vasantha kumar N  
**Task Title:** Linear Programming for Product Mix Optimization  
**Technology Stack:** Python, PuLP (Linear Programming Library)

---

## Objective

The goal of this task was to build a linear programming model using Python to determine the optimal product mix for maximizing profit, given certain production constraints.

---

## Problem Statement

A company produces two products: **Product A** and **Product B**. Each product requires specific machine hours from two different machines. The company wants to find out how many units of each product should be produced to **maximize profit** while ensuring that the total machine hours used do not exceed the available capacity.

---

## Problem Formulation

- **Profit** per unit of:
  - Product A = ₹60
  - Product B = ₹40

- **Constraints:**
  - Machine 1 has **100 hours** available  
    (`2x + 1y <= 100`)
  - Machine 2 has **80 hours** available  
    (`1x + 1y <= 80`)

- **Objective:**  
  Maximize `60x + 40y`  
  Where `x = units of Product A`, `y = units of Product B`

---

## Tools & Libraries Used

- Python 3.12
- [PuLP](https://github.com/coin-or/pulp) — Python library for Linear Programming
- CBC Solver (Default solver in PuLP)

---

## Project Workflow

1. **Define the Problem:**
   - Set up objective function and constraints

2. **Model the Problem using PuLP:**
   - Defined decision variables `x` and `y`
   - Constructed and solved the LP model

3. **Output Interpretation:**
   - Printed optimal number of products and total profit

---

## Results

 **Optimal number of Product A:** 20 units  
 **Optimal number of Product B:** 60 units  
 **Maximum Profit:** ₹3600

---

## Files Included

| File Name                            | Description                                |
|-------------------------------------|--------------------------------------------|
| `Task4_Product_Mix_Optimization.ipynb` | Notebook with explanation and results      |
| `program_code.py`                   | Raw Python script for solving the problem  |
| `README.md`                         | This documentation                         |

---

## Learning Outcomes

- Learned to apply **Linear Programming** to solve real-world business optimization problems
- Understood how to model constraints and objectives using **PuLP**
- Gained experience in interpreting solver results and debugging optimization code

---

## Submission

This project is submitted as part of **Task 4 of the CODTECH Data Science Internship** and demonstrates practical understanding of optimization with Python.

