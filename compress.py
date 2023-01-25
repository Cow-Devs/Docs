import json

with open("docs.json") as f1:
 e = json.load(f1)
with open("compressed.json", "w") as f2:
 json.dump(e, f2, seperators=(",", ":"))
