def gcd_iter(var_2791, var_8844):
    while var_8844:
        var_2825 = var_8844
        var_8844 = var_2791 % var_8844
        var_2791 = var_2825
    return var_2791


print(var_4746(60, 48))

# Comment 24