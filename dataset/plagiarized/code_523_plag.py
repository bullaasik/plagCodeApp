def var_3584(var_5406):
    if not len(var_5406) <= 1:
        var_9553 = len(var_5406) // 2
        var_3468 = var_5406[:var_9553]
        var_5393 = var_5406[var_9553:]
        var_3584(var_3468)
        var_3584(var_5393)
        var_9931 = var_3057 = var_7943 = 0
        while var_9931 < len(var_3468) and var_3057 < len(var_5393):
            if not var_3468[var_9931] > var_5393[var_3057]:
                var_5406[var_7943] = var_3468[var_9931]
                var_9931 += 1
            else:
                var_5406[var_7943] = var_5393[var_3057]
                var_3057 += 1
            var_7943 += 1
        while var_9931 < len(var_3468):
            var_5406[var_7943] = var_3468[var_9931]
            var_9931 += 1
            var_7943 += 1
        while var_3057 < len(var_5393):
            var_5406[var_7943] = var_5393[var_3057]
            var_3057 += 1
            var_7943 += 1


var_5406 = [10, 7, 8, 9, 1, 5]
var_3584(var_5406)
print(var_5406)
