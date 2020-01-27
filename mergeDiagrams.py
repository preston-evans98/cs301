import json
with open("diagram.json", "r") as f:
    diagram = json.load(f)

with open("d2.json", "r") as f:
    d2 = json.load(f)

max_shape_id = diagram['shapes'][-1]['details']['id']
max_connector_id = diagram['connectors'][-1]['details']['id']
for shape in d2['shapes']:
    shape['details']['id'] += max_shape_id
for connector in d2['connectors']:
    connector['source'] += max_shape_id
    connector['destination'] += max_shape_id
    connector['details']['id'] += max_connector_id


diagram['shapes'] += d2['shapes']
diagram['connectors'] += d2['connectors']

with open("output.json", "w") as f:
    json.dump(diagram, f, indent=2)
