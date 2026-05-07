import json
import os

try:
    import nbformat as nbf
    use_nbf = True
except ImportError:
    use_nbf = False

if use_nbf:
    nb = nbf.read('death_risk_prediction.ipynb', as_version=4)
    md_cell = nbf.v4.new_markdown_cell("### Step 1.1 – Integrate Additional Excel Files\n\nLoad the additional Excel files containing Cause of Death (COD) statistics.")
    code_cell = nbf.v4.new_code_cell("""# Load the three excel files
excel_file_1 = '4_Table 1 Attachment to PR on 2024 COD as of 30November2024_ccv_vsd.xlsx'
excel_file_2 = 'Table 1_Attachment to PR on 2025 COD_as of 31 January 2026.xlsx'
excel_file_3 = 'Table 1_Attachment to PR on 2025 COD_as of 28 February 2026.xlsx'

# Read the excel files (adjust skiprows/sheet_name if necessary based on their formatting)
df_ex1 = pd.read_excel(excel_file_1)
df_ex2 = pd.read_excel(excel_file_2)
df_ex3 = pd.read_excel(excel_file_3)

print("File 1 Shape:", df_ex1.shape)
print("File 2 Shape:", df_ex2.shape)
print("File 3 Shape:", df_ex3.shape)

display(df_ex1.head(3))
display(df_ex2.head(3))
display(df_ex3.head(3))""")
    
    insert_idx = -1
    for i, cell in enumerate(nb.cells):
        if cell.cell_type == 'code' and "Number of Deaths by Risk Factors.csv" in cell.source:
            insert_idx = i + 1
            break
            
    if insert_idx != -1:
        nb.cells.insert(insert_idx, md_cell)
        nb.cells.insert(insert_idx + 1, code_cell)
        nbf.write(nb, 'death_risk_prediction.ipynb')
        print("Notebook updated successfully via nbformat.")
    else:
        print("Could not find the target cell to insert after.")
else:
    with open('death_risk_prediction.ipynb', 'r') as f:
        nb = json.load(f)
        
    md_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["### Step 1.1 \u2013 Integrate Additional Excel Files\n", "\n", "Load the additional Excel files containing Cause of Death (COD) statistics."]
    }
    code_cell = {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Load the three excel files\n",
            "excel_file_1 = '4_Table 1 Attachment to PR on 2024 COD as of 30November2024_ccv_vsd.xlsx'\n",
            "excel_file_2 = 'Table 1_Attachment to PR on 2025 COD_as of 31 January 2026.xlsx'\n",
            "excel_file_3 = 'Table 1_Attachment to PR on 2025 COD_as of 28 February 2026.xlsx'\n",
            "\n",
            "# Read the excel files (adjust skiprows/sheet_name if necessary based on their formatting)\n",
            "df_ex1 = pd.read_excel(excel_file_1)\n",
            "df_ex2 = pd.read_excel(excel_file_2)\n",
            "df_ex3 = pd.read_excel(excel_file_3)\n",
            "\n",
            "print(\"File 1 Shape:\", df_ex1.shape)\n",
            "print(\"File 2 Shape:\", df_ex2.shape)\n",
            "print(\"File 3 Shape:\", df_ex3.shape)\n",
            "\n",
            "display(df_ex1.head(3))\n",
            "display(df_ex2.head(3))\n",
            "display(df_ex3.head(3))"
        ]
    }
    
    insert_idx = -1
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code' and any("Number of Deaths by Risk Factors.csv" in line for line in cell['source']):
            insert_idx = i + 1
            break
            
    if insert_idx != -1:
        nb['cells'].insert(insert_idx, md_cell)
        nb['cells'].insert(insert_idx + 1, code_cell)
        with open('death_risk_prediction.ipynb', 'w') as f:
            json.dump(nb, f, indent=1)
        print("Notebook updated successfully via JSON fallback.")
    else:
        print("Could not find the target cell to insert after.")
