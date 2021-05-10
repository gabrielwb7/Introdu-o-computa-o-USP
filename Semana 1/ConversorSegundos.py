segundos_str = input('Coloque o tempo em segundos que deseja converter: ')
total_segs = int(segundos_str)

horas = total_segs // 3600
segs_restantes= total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final= segs_restantes % 60
dias = horas // 24
horas_restante= horas % 24

print( dias, "dias, ", horas_restante, "horas, ", minutos, "minutos e", segs_restantes_final, "segundos.")