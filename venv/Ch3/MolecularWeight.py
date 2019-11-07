# MolecularWeight.py
# A program to compute the molecular weight of Carbohydrates


def getMolecularWeight():
    w_hydrogen = 1.00794
    w_carbon = 12.0107
    w_oxygen = 15.9994
    formula = input("Enter the Carbohydrate formula : <<format: Cx Hy Oz>> ")
    f_code = formula.split(" ")
    n_carbon = getAtomsCount(f_code[0])
    n_hydrogen = getAtomsCount(f_code[1])
    n_oxygen = getAtomsCount(f_code[2])
    print(type(n_carbon))
    print(n_carbon)
    automic_weight = n_carbon * w_carbon + n_hydrogen * w_hydrogen + n_oxygen * w_oxygen
    print("Automic Weight of " + formula + " is ", automic_weight)
    return automic_weight


def getAtomsCount(f_sub_code):
    atoms_count = int(f_sub_code.upper().replace('H', '').replace('C', '').replace('O', ''))
    return atoms_count


getMolecularWeight()
