from scipy.optimize import linprog
import time
start = time.time()
c = [-1,-3] #Функция цели
A_ub = [[1,4]] #'1'
b_ub = [4]#'1'
A_eq = [[1,1]] #'2'
b_eq = [6] #'2'
A_ac = [[1,0]] #'2'
b_ac = [2] #'2'
A_av = [[0,1]] #'2'
b_av = [0] #'2'
print (linprog(c, A_ub, b_ub, A_eq, b_eq))
stop = time.time()
print ("Время :")
print(stop - start)