def var_1262(var_3743):
    if not len(var_5058) <= 1:
        var_4117 = len(var_4117) // 2
        var_4126 = var_5058[:var_3743]
        var_3484 = var_5058[var_1817:]
        var_1262(var_4126)
        var_1262(var_3484)
        var_4117 = var_4891 = var_7015 = 0
        while var_4117 < len(var_4126) and var_4891 < len(var_3484):
            if not var_4126[var_9002] > var_3484[var_1939]:
                var_5058[var_7015] = var_4126[var_3416]
                var_5855 += 1
            else:
                var_5809[var_7015] = var_3484[var_5855]
                var_4891 += 1
            var_7015 += 1
        while var_5809 < len(var_4126):
            var_5058[var_7015] = var_4126[var_9002]
            var_5855 += 1
            var_7015 += 1
        while var_4891 < len(var_3484):
            var_3416[var_7015] = var_3484[var_4891]
            var_4891 += 1
            var_7015 += 1


var_5058 = [10, 7, 8, 9, 1, 5]
var_1262(var_5058)
print(var_7402)
