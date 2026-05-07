import json

with open('death_risk_prediction.ipynb', 'r') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code' and 'MULTICLASS LOGISTIC REGRESSION' in ''.join(cell['source']):
        print(f"Cell {i} outputs:")
        for output in cell.get('outputs', []):
            if output['output_type'] == 'error':
                print("Error Name:", output['ename'])
                print("Error Value:", output['evalue'])
                print("Traceback:")
                print('\n'.join(output['traceback']))
