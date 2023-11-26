from ortools.linear_solver import pywraplp



def setup(variables, constraints, objective, solver):
    new_variables = [solver.NumVar(variables[i].Lb(), variables[i].Ub(), "v"+str(i)) for i in range(len(variables)) ]
    new_constraints = []
    for i in range(len(constraints)) :
        lb = constraints[i].Lb()
        ub = constraints[i].Ub()
        nc = solver.Constraint(lb, ub)
        for j in range(len(variables)):
            coefficient = constraints[i].GetCoefficient(variables[j])
            nc.SetCoefficient(new_variables[j], coefficient)
            new_constraints.append(nc)

    new_objective = solver.Objective().SetMinimization()

    for i in range(len(variables)):
        coefficient = objective.GetCoefficient(variables[i])
        new_objective.SetCoefficient(new_variables[i], coefficient)
    return (new_variables, new_constraints, new_objective, solver)
    