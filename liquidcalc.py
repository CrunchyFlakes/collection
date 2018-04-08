#!/usr/bin/env python3
### !!!! not working


vg_gperml = 1.2613
pg_gperml = 1.0373
h2o_gperml = 1
flavor_gperml = pg_gperml  # change if needed


batch_ml = float(input("batch in ml: "))
nicotine_strength_base_mg = float(input("nicotine base mg/ml: "))
nicotine_strength_target_mg = float(input("nicotine target mg/ml: "))
nicotine_vg_per = float(input("nicotine base VG in %: "))
nicotine_pg_per = float(input("nicotine base PG in %: "))
vg_target_per = float(input("VG target in %: "))
pg_target_per = float(input("PG target in %: "))
h2o_target_per = float(input("H2O target in %: "))
flavor_target_per = float(input("flavor target in %: "))



nicotine_gperml = ((nicotine_pg_per * pg_gperml) + (nicotine_vg_per * vg_gperml))

nicotine_base_ml = batch_ml * (nicotine_strength_target_mg / nicotine_strength_base_mg)
print(str(nicotine_base_ml))

