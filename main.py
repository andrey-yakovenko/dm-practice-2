from datetime import datetime
from additional import calculate_problem, generate_problem_output, get_kendell_lists, calculate_kendell

# Solving all problems from questions
list_visit_1, time_1, money_1 = calculate_problem("q1")
list_visit_2a_1, time_2a_1, money_2a_1 = calculate_problem("q2a_p1", p1=True)
list_visit_2a_2, time_2a_2, money_2a_2 = calculate_problem("q2a_p2", p2=True)
list_visit_2a_3, time_2a_3, money_2a_3 = calculate_problem("q2a_p3", p3=True)
list_visit_2a_4, time_2a_4, money_2a_4 = calculate_problem("q2a_p4", p4=True)
list_visit_2a_5, time_2a_5, money_2a_5 = calculate_problem("q2a_p5", p5=True)
list_visit_2b, time_2b, money_2b = calculate_problem("q2b", p1=True, p2=True)
list_visit_2c, time_2c, money_2c = calculate_problem("q2c", p1=True, p3=True)
list_visit_2d, time_2d, money_2d = calculate_problem("q2d", p1=True, p4=True)
list_visit_2e, time_2e, money_2e = calculate_problem("q2e", p2=True, p5=True)
list_visit_2f, time_2f, money_2f = calculate_problem("q2f", p3=True, p4=True)
list_visit_2g, time_2g, money_2g = calculate_problem("q2g", p4=True, p5=True)
list_visit_2h, time_2h, money_2h = calculate_problem("q2h", p1=True, p2=True, p4=True)
list_visit_2i, time_2i, money_2i = calculate_problem("q2i", p2=True, p3=True, p5=True)
list_visit_2j, time_2j, money_2j = calculate_problem("q2j", p2=True, p3=True, p4=True, p5=True)
list_visit_2k, time_2k, money_2k = calculate_problem("q2k", p1=True, p2=True, p4=True, p5=True)
list_visit_2l, time_2l, money_2l = calculate_problem("q2l", p1=True, p2=True, p3=True, p4=True, p5=True)
kendell_duration, kendell_rate, kendell_price = get_kendell_lists()
tau_duration_rate = calculate_kendell(kendell_duration, kendell_rate)
tau_duration_price = calculate_kendell(kendell_duration, kendell_price)
tau_rate_price = calculate_kendell(kendell_rate, kendell_price)

# Generating the output's header including the list of preferences
output = 'Student: Andrii Yakovenko (M2 BDMA)\n' \
         'Course: Decision Modelling (2020-2021)\n' \
         'Assignment: Linear Programing and Preferences (Practical Work 2)\n\n' \
         'AUTOMATICALLY GENERATED REPORT (generated on ' + str(datetime.now())[:16] + ')\n\n\n'

# Generating problems' outputs
output += 'QUESTIONS AND ANSWERS:\n\n'
output += generate_problem_output("(Q.1) No preferences", list_visit_1, time_1, money_1, None)
output += generate_problem_output("(Q.2a.1) Preference 1", list_visit_2a_1, time_2a_1, money_2a_1, list_visit_1)
output += generate_problem_output("(Q.2a.2) Preference 2", list_visit_2a_2, time_2a_2, money_2a_2, list_visit_1)
output += generate_problem_output("(Q.2a.3) Preference 3", list_visit_2a_3, time_2a_3, money_2a_3, list_visit_1)
output += generate_problem_output("(Q.2a.4) Preference 4", list_visit_2a_4, time_2a_4, money_2a_4, list_visit_1)
output += generate_problem_output("(Q.2a.5) Preference 5", list_visit_2a_5, time_2a_5, money_2a_5, list_visit_1)
output += generate_problem_output("(Q.2b) Preferences 1, 2", list_visit_2b, time_2b, money_2b, list_visit_1)
output += generate_problem_output("(Q.2c) Preferences 1, 3", list_visit_2c, time_2c, money_2c, list_visit_1)
output += generate_problem_output("(Q.2d) Preferences 1, 4", list_visit_2d, time_2d, money_2d, list_visit_1)
output += generate_problem_output("(Q.2e) Preferences 2, 5", list_visit_2e, time_2e, money_2e, list_visit_1)
output += generate_problem_output("(Q.2f) Preferences 3, 4", list_visit_2f, time_2f, money_2f, list_visit_1)
output += generate_problem_output("(Q.2g) Preferences 4, 5", list_visit_2g, time_2g, money_2g, list_visit_1)
output += generate_problem_output("(Q.2h) Preferences 1, 2, 4", list_visit_2h, time_2h, money_2h, list_visit_1)
output += generate_problem_output("(Q.2i) Preferences 2, 3, 5", list_visit_2i, time_2i, money_2i, list_visit_1)
output += generate_problem_output("(Q.2j) Preferences 2, 3, 4, 5", list_visit_2j, time_2j, money_2j, list_visit_1)
output += generate_problem_output("(Q.2k) Preferences 1, 2, 4, 5", list_visit_2k, time_2k, money_2k, list_visit_1)
output += generate_problem_output("(Q.2l) Preferences 1, 2, 3, 4, 5", list_visit_2l, time_2l, money_2l, list_visit_1)
output += "(Q.3) Kendall rank correlation coefficient (higher - more similar, or identical for a correlation of 1):\n\n"
output += "   DURATION-RATE:    " + str(tau_duration_rate) + '\n'
output += "   DURATION-PRICE:   " + str(tau_duration_price) + '\n'
output += "   RATE-PRICE:      " + str(tau_rate_price) + '\n'

# Generating an output file 'output.txt'
file = open("output.txt", "w", encoding="utf-8")
file.write(output)
file.close()
