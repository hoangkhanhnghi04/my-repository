select v.*, w.avg_tavg, w.avg_tmax, w.avg_tmin, w.avg_tobs, c.total_cases, c.total_tests, h.day_total as 'hospital_day_total', d.*
from vaccine v 
left join weather w on v.date = w.date
left join cases_deaths c on v.date = c.date
left join deaths d on v.date = d.date
left join hospital h on v.date = h.date