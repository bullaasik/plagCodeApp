def gcd4(var_4407, var_6921):
    while var_6921:
        var_4407, var_6921 = var_6921, var_4407 % var_6921
    return var_4407


print(var_74024(60, 48))
