\* Toy_Factory *\
Maximize
Total_profit;_to_be_maximized: 25 Toy_A_Type + 20 Toy_B_Type
Subject To
Time_constraint: 5 Toy_A_Type + 5 Toy_B_Type <= 540
Units_constraint: 20 Toy_A_Type + 12 Toy_B_Type <= 2000
Bounds
0 <= Toy_A_Type
0 <= Toy_B_Type
Generals
Toy_A_Type
Toy_B_Type
End
