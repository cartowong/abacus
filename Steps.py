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
    Step(si.no_carry_borrow),
    Step(si.plus5_eq_minus5_plus10),
    Step(si.minus5_eq_plus5_minus10),
    Step(si.plus5_eq_minus5_plus10, si.minus5_eq_plus5_minus10),
    Step(si.plus6_eq_minus4_plus10),
    Step(si.minus6_eq_plus4_minus10),
    Step(si.plus6_eq_minus4_plus10, si.minus6_eq_plus4_minus10),
    Step(si.plus7_eq_minus3_plus10),
    Step(si.minus7_eq_plus3_minus10),
    Step(si.plus7_eq_minus3_plus10, si.minus7_eq_plus3_minus10),
    Step(si.plus8_eq_minus2_plus10),
    Step(si.minus8_eq_plus2_minus10),
    Step(si.plus8_eq_minus2_plus10, si.minus8_eq_plus2_minus10),
    Step(si.plus9_eq_minus1_plus10),
    Step(si.minus9_eq_plus1_minus10),
    Step(si.plus9_eq_minus1_plus10, si.minus9_eq_plus1_minus10),
    Step(si.plus5_eq_minus5_plus10,
         si.minus5_eq_plus5_minus10,
         si.plus6_eq_minus4_plus10,
         si.minus6_eq_plus4_minus10,
         si.plus7_eq_minus3_plus10,
         si.minus7_eq_plus3_minus10,
         si.plus8_eq_minus2_plus10,
         si.minus8_eq_plus2_minus10,
         si.plus9_eq_minus1_plus10,
         si.minus9_eq_plus1_minus10).with_description("Combo - steps 19, 22, 25, 28, 31"),
    Step(si.plus1_eq_minus9_plus10),
    Step(si.minus1_eq_plus9_minus10),
    Step(si.plus1_eq_minus9_plus10, si.minus1_eq_plus9_minus10),
    Step(si.plus2_eq_minus8_plus10),
    Step(si.minus2_eq_plus8_minus10),
    Step(si.plus2_eq_minus8_plus10, si.minus2_eq_plus8_minus10),
    Step(si.plus3_eq_minus7_plus10),
    Step(si.minus3_eq_plus7_minus10),
    Step(si.plus3_eq_minus7_plus10, si.minus3_eq_plus7_minus10),
    Step(si.plus4_eq_minus6_plus10),
    Step(si.minus4_eq_plus6_minus10),
    Step(si.plus4_eq_minus6_plus10, si.minus4_eq_plus6_minus10),
    Step(si.plus1_eq_minus9_plus10,
         si.minus1_eq_plus9_minus10,
         si.plus2_eq_minus8_plus10,
         si.minus2_eq_plus8_minus10,
         si.plus3_eq_minus7_plus10,
         si.minus3_eq_plus7_minus10,
         si.plus4_eq_minus6_plus10,
         si.minus4_eq_plus6_minus10).with_description("Combo - steps 35, 38, 41, 44"),
    Step(si.plus1_eq_minus9_plus10,
         si.minus1_eq_plus9_minus10,
         si.plus2_eq_minus8_plus10,
         si.minus2_eq_plus8_minus10,
         si.plus3_eq_minus7_plus10,
         si.minus3_eq_plus7_minus10,
         si.plus4_eq_minus6_plus10,
         si.minus4_eq_plus6_minus10,
         si.plus5_eq_minus5_plus10,
         si.minus5_eq_plus5_minus10,
         si.plus6_eq_minus4_plus10,
         si.minus6_eq_plus4_minus10,
         si.plus7_eq_minus3_plus10,
         si.minus7_eq_plus3_minus10,
         si.plus8_eq_minus2_plus10,
         si.minus8_eq_plus2_minus10,
         si.plus9_eq_minus1_plus10,
         si.minus9_eq_plus1_minus10).with_description("Combo - steps 19, 22, 25, 28, 31, 35, 38, 41, 44")
]
