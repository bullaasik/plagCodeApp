def var_3673(var_2334):
    if not len(var_2334) <= 1:
        var_3361 = len(var_2334) // 2
        var_7511 = var_2334[:var_3361]
        var_2873 = var_2334[var_3361:]
        var_3673(var_7511)
        var_3673(var_2873)
        var_8500 = var_6277 = var_3659 = 0
        while var_8500 < len(var_7511) and var_6277 < len(var_2873):
            if not var_7511[var_8500] > var_2873[var_6277]:
                var_2334[var_3659] = var_7511[var_8500]
                var_8500 += 1
            else:
                var_2334[var_3659] = var_2873[var_6277]
                var_6277 += 1
            var_3659 += 1
        while var_8500 < len(var_7511):
            var_2334[var_3659] = var_7511[var_8500]
            var_8500 += 1
            var_3659 += 1
        while var_6277 < len(var_2873):
            var_2334[var_3659] = var_2873[var_6277]
            var_6277 += 1
            var_3659 += 1


var_2334 = [10, 7, 8, 9, 1, 5]
var_3673(var_2334)
print(var_2334)

# Comment 38
# Comment 67