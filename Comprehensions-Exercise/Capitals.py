countries = [i for i in input().split(", ")]
capitals = [i for i in input().split(", ")]
[print(f"{k} -> {capitals[i]}") for (i,k) in enumerate(countries)]