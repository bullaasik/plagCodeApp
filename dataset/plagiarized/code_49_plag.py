def var_5564(var_5616):
    if var_5616 == 0:
        return 1
    return var_5616 * var_5564(var_5616 - 1)


print(var_5564(5))

# Comment 36