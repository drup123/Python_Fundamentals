a = {
      "harry":[100,23,4], "dadu":60,"sama":70
  }

print(a.values())
print(a.items())
print(a.keys())
print(a.get("harry"))
a.update({"harry":50})
print(a)
print(['dadu'])

for i in a:
    print(i)
# DICTIONARY IS MUTABLE