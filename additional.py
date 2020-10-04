import pulp
from scipy.stats import kendalltau
from input import locations, locations_if_p1, TIME_LIMIT, BUDGET


# Technical functions to calculate sums for problems (as constraint) and to sum up after all


def money_spent_constraint(prob, p1):
    total = 0
    for variable in prob.variables():
        if p1: total += variable * locations_if_p1[variable.name]['price']
        else: total += variable * locations[variable.name]['price']
    return total


def time_spent_constraint(prob, p1):
    total = 0
    for variable in prob.variables():
        if p1: total += variable * locations_if_p1[variable.name]['duration']
        else: total += variable * locations[variable.name]['duration']
    return total


def money_spent_total(prob, p1):
    total = 0
    for variable in prob.variables():
        if p1:
            if len(variable.name) == 2: total += variable.varValue * locations[variable.name]['price']
            else:
                group = variable.name.split("_")
                for group_variable in group:
                    total += variable.varValue * locations[group_variable]['price']
        else: total += variable.varValue * locations[variable.name]['price']
    return total


def time_spent_total(prob, p1):
    total = 0
    for variable in prob.variables():
        if p1:
            if len(variable.name) == 2: total += variable.varValue * locations[variable.name]['duration']
            else:
                group = variable.name.split("_")
                for group_variable in group:
                    total += variable.varValue * locations[group_variable]['duration']
        else: total += variable.varValue * locations[variable.name]['duration']
    return total


# Preference constraints (first preference is not a constraint for problem, but a different set of grouped locations)


def preference_2(problem):
    total = 0
    for variable in problem.variables():
        if variable.name == "TE" or variable.name == "CA": total += variable
    return total == 2


def preference_3(problem):
    total = 0
    for variable in problem.variables():
        if variable.name == "CN" or variable.name == "SC": total += variable
    return total <= 1


def preference_4(problem):
    for variable in problem.variables():
        if variable.name == "TM": return variable == 1


def preference_5(problem):
    total = 0
    for variable in problem.variables():
        if variable.name == "ML": total -= variable
        if variable.name == "CP": total += variable
    return total >= 0


# A bit different way to calculate constraints in case of grouped locations (preference 1)


def preference_2_if_p1(problem):
    total = 0
    for variable in problem.variables():
        if variable.name == "TE" or variable.name == "CA": total += variable
    return total == 2


def preference_3_if_p1(problem):
    for variable in problem.variables():
        if variable.name == "CP_CN_SC_ML": return variable == 0


def preference_4_if_p1(problem):
    for variable in problem.variables():
        if variable.name == "TM": return variable == 1


# Function to initialize and solve a problem depending on preference set
def calculate_problem(title, p1=False, p2=False, p3=False, p4=False, p5=False):
    problem, list_visit = pulp.LpProblem("paris_problem_"+title, pulp.LpMaximize), []
    te = pulp.LpVariable("TE", 0, 1, pulp.LpInteger)
    ca = pulp.LpVariable("CA", 0, 1, pulp.LpInteger)
    bs = pulp.LpVariable("BS", 0, 1, pulp.LpInteger)
    tm = pulp.LpVariable("TM", 0, 1, pulp.LpInteger)
    if p1:
        at_ac = pulp.LpVariable("AT_AC", 0, 1, pulp.LpInteger)
        mo_jt_pc = pulp.LpVariable("MO_JT_PC", 0, 1, pulp.LpInteger)
        cp_cn_sc_ml = pulp.LpVariable("CP_CN_SC_ML", 0, 1, pulp.LpInteger)
        problem += te + ca + bs + tm + at_ac + mo_jt_pc + cp_cn_sc_ml, "amount_of_locations_to_be_maximized"
    else:
        ml = pulp.LpVariable("ML", 0, 1, pulp.LpInteger)
        at = pulp.LpVariable("AT", 0, 1, pulp.LpInteger)
        mo = pulp.LpVariable("MO", 0, 1, pulp.LpInteger)
        jt = pulp.LpVariable("JT", 0, 1, pulp.LpInteger)
        cp = pulp.LpVariable("CP", 0, 1, pulp.LpInteger)
        cn = pulp.LpVariable("CN", 0, 1, pulp.LpInteger)
        sc = pulp.LpVariable("SC", 0, 1, pulp.LpInteger)
        pc = pulp.LpVariable("PC", 0, 1, pulp.LpInteger)
        ac = pulp.LpVariable("AC", 0, 1, pulp.LpInteger)
        problem += te + ml + at + mo + jt + ca + cp + cn + bs + sc + pc + tm + ac, "amount_of_locations_to_be_maximized"
    problem += money_spent_constraint(problem, p1) <= BUDGET, "budget_constraint"
    problem += time_spent_constraint(problem, p1) <= TIME_LIMIT, "time_constraint"
    if p1:
        if p2: problem += preference_2_if_p1(problem), "preference_2"
        if p3: problem += preference_3_if_p1(problem), "preference_3"
        if p4: problem += preference_4_if_p1(problem), "preference_4"
    else:
        if p2: problem += preference_2(problem), "preference_2"
        if p3: problem += preference_3(problem), "preference_3"
        if p4: problem += preference_4(problem), "preference_4"
        if p5: problem += preference_5(problem), "preference_5"
    problem.writeLP("problems/"+title+".lp")
    problem.solve()
    for value in problem.variables():
        if value.varValue:
            if len(value.name) == 2:
                list_visit.append(value.name+": "+locations[value.name]["title"])
            else:
                group = value.name.split("_")
                for group_value in group:
                    list_visit.append(group_value + ": " + locations[group_value]["title"])
    return list_visit, time_spent_total(problem, p1), money_spent_total(problem, p1)


def lists_similarity(list_visit_1, list_visit_2):
    if len(list_visit_1) == len(list_visit_2):
        for location in list_visit_1:
            if location not in list_visit_2: return False
        return True
    else: return False


def generate_problem_output(title, list_visit, time, money, lv1):
    output = title + "\n\n   Locations selected:\n\n"
    for location in list_visit: output += "   " + location + '\n'
    output += '\n   Total amount:   ' + str(len(list_visit)) + ' / 13 locations\n' \
              '   Total time:     ' + str(time) + ' / ' + str(TIME_LIMIT) + ' hours\n' \
              '   Total money:    ' + str(money) + ' / ' + str(BUDGET) + ' euros\n\n'
    if lv1 is not None:
        if lists_similarity(list_visit, lv1): output += '   This list is SIMILAR to list_visit_1\n\n'
        else: output += '   This list is NOT SIMILAR to list_visit_1\n\n'
    return output


def get_kendell_lists():
    kendell_duration, kendell_rate, kendell_price = [], [], []
    for key in locations.keys():
        kendell_duration.append(locations[key]['duration'])
        kendell_rate.append(locations[key]['rate'])
        kendell_price.append(locations[key]['price'])
    return kendell_duration, kendell_rate, kendell_price


def calculate_kendell(list_1, list_2):
    tau, p_value = kendalltau(list_1, list_2)
    return tau
