def is_blood_compatible(donor_blood_type, receiver_blood_type):
    donor_antigen_a = 'A' in donor_blood_type
    donor_antigen_b = 'B' in donor_blood_type
    donor_rh_factor = '+' in donor_blood_type

    receiver_antigen_a = 'A' in receiver_blood_type
    receiver_antigen_b = 'B' in receiver_blood_type
    receiver_rh_factor = '+' in receiver_blood_type

    if donor_antigen_a and not receiver_antigen_a:
        return False
    if donor_antigen_b and not receiver_antigen_b:
        return False
    if donor_rh_factor and not receiver_rh_factor:
        return False
    if not donor_antigen_a and not donor_antigen_b and not donor_rh_factor:
        return True  

    return True

donor_type = "A+"
receiver_type = "A+"

if is_blood_compatible(donor_type, receiver_type):
    print("The donor can safely give blood to the receiver.")
else:
    print("The donor cannot safely give blood to the receiver.")
