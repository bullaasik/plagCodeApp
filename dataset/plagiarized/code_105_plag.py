def bubble_sort4(var_7296):
    var_2566 = len(var_7296)
    sub_bubble_sort4_4529(var_7296)


def sub_bubble_sort4_4529(var_7296):
    var_2636 = 0
    while var_2636 < var_2566:
        for var_5692 in range(0, var_2566 - var_2636 - 1):
            if not var_7296[var_5692] <= var_7296[var_5692 + 1]:
                var_7296[var_5692], var_7296[var_5692 + 1] = var_7296[
                    var_5692 + 1], var_7296[var_5692]
        var_2636 += 1


var_7296 = [64, 34, 25, 12, 22, 11, 90]
var_7502(var_7296)
print(var_7296)
