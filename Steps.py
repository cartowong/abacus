import Skills as si
from Core import Step


steps = [
    Step(si.simple_addition_or_subtraction),
    Step(si.simple_addition_or_subtraction_allow_upper_bead),
    Step(si.plus1_eq_minus4_plus5),
    Step(si.minus1_eq_plus4_minus5),
    Step(si.plus1_eq_minus4_plus5, si.minus1_eq_plus4_minus5),
    Step(si.plus2_eq_minus3_plus5),
    Step(si.minus2_eq_plus3_minus5),
    Step(si.plus2_eq_minus3_plus5, si.minus2_eq_plus3_minus5),
    Step(si.plus3_eq_minus2_plus5),
    Step(si.minus3_eq_plus2_minus5),
    Step(si.plus3_eq_minus2_plus5, si.minus3_eq_plus2_minus5),
    Step(si.plus4_eq_minus1_plus5),
    Step(si.minus4_eq_plus1_minus5),
    Step(si.plus4_eq_minus1_plus5, si.minus4_eq_plus1_minus5),
    Step(si.plus1_eq_minus4_plus5,
         si.minus1_eq_plus4_minus5,
         si.plus2_eq_minus3_plus5,
         si.minus2_eq_plus3_minus5,
         si.plus3_eq_minus2_plus5,
         si.minus3_eq_plus2_minus5,
         si.plus4_eq_minus1_plus5,
         si.minus4_eq_plus1_minus5).with_description('Combo - steps 5, 8, 11, 14'),
    Step(si.no_carry_borrow)
]