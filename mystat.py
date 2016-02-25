#!/bin/python

mean = 'mean'
median = 'median'
maximum = 'maximum'
minimum = 'minimum'
perc95 = 'perc95'
perc5 = 'perc5'
perc25 = 'perc25'
perc75 = 'perc75'

def get_stats_with_names(values):
    #Returns a dict with keys = statistic name, and value = value of that statistic
    values.sort()
    stat_dict = {}
    
    if len(values) > 0:
        stat_dict[minimum] = values[0]
        stat_dict[maximum] = values[len(values) - 1]
        median_val = values[len(values) // 2]
        if len(values) % 2 == 0:
            median_val = (values[len(values) // 2 - 1] + values[len(values) // 2]) / 2
        stat_dict[median] = median_val
        stat_dict[mean] = sum(values) / len(values)
        stat_dict[perc95] = values[len(values) * 95 // 100]
        stat_dict[perc5] = values[len(values) * 5 // 100]
        stat_dict[perc25] = values[len(values) * 25 // 100]
        stat_dict[perc75] = values[len(values) * 75 // 100]
        return stat_dict
    stat_dict['ZEROVALUES'] = 0
    return stat_dict