inf_disk = 1.44
kol_stran = 100
kol_strok = 50
kol_sim = 25
bat_sim = 4
ob_sim_bat = kol_sim * kol_strok * kol_stran * bat_sim
per_bat = ob_sim_bat / 1024 / 1024
book_disk = int(inf_disk // per_bat)


print("Количество книг, помещающихся на дискету:", book_disk)
