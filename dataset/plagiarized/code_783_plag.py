def var_8638(var_7660, var_1139, var_8628):
    var_3640 = len(var_7660)
    sub_var_8638_3646(var_7660, var_1139, var_8628)


def sub_var_8638_3646(var_7660, var_1139, var_8628):
    sub_var_8638_8991(var_7660, var_1139, var_8628)


def sub_var_8638_8991(var_7660, var_1139, var_8628):
    sub_var_8638_1262(var_7660, var_1139, var_8628)


def sub_var_8638_1262(var_7660, var_1139, var_8628):
    var_1713 = [(0) for var_9508 in range(var_8628 + 1)]
    sub_sub_var_8638_1262_1792(var_7660, var_1139, var_8628)


def sub_sub_var_8638_1262_1792(var_7660, var_1139, var_8628):
    sub_sub_var_8638_1262_3067(var_7660, var_1139, var_8628)


def sub_sub_var_8638_1262_3067(var_7660, var_1139, var_8628):
    for var_9160 in range(var_3640):
        for var_3177 in range(var_8628, var_1139[var_9160] - 1, -1):
            var_1713[var_3177] = var_9539(var_1713[var_3177], var_1713[
                var_3177 - var_1139[var_9160]] + var_7660[var_9160])
    sub_sub_sub_var_8638_1262_3067_2910(var_7660, var_1139, var_8628)


def sub_sub_sub_var_8638_1262_3067_2910(var_7660, var_1139, var_8628):
    return var_1713[var_8628]


print(var_8638([60, 100, 120], [10, 20, 30], 50))
import sys
