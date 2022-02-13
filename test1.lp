\* ConceptMatching *\
Maximize
obj: drain
Subject To
Alice_can_learn_one_concept_only_once:
 var_binary_round_0::learning::name::Alice___round_0::concept::5
 + var_binary_round_1::learning::name::Alice___round_1::concept::5
 + var_binary_round_2::learning::name::Alice___round_2::concept::5 <= 1
John_can_learn_one_concept_only_once:
 var_binary_round_0::learning::name::John___round_0::concept::2
 + var_binary_round_1::learning::name::John___round_1::concept::2
 + var_binary_round_2::learning::name::John___round_2::concept::2 <= 1
flow_constraint_round_0::concept::2:
 - var_binary_round_0::concept::2___round_0::teaching::name::Mary
 + var_binary_round_0::learning::name::John___round_0::concept::2 = 0
flow_constraint_round_0::concept::3:
 - var_binary_round_0::concept::3___round_0::teaching::name::Alice = 0
flow_constraint_round_0::concept::5:
 - var_binary_round_0::concept::5___round_0::teaching::name::John
 + var_binary_round_0::learning::name::Alice___round_0::concept::5 = 0
flow_constraint_round_0::learning::name::Alice:
 - var_binary_round_0::learning::name::Alice___round_0::concept::5
 + var_binary_source___round_0::learning::name::Alice = 0
flow_constraint_round_0::learning::name::John:
 - var_binary_round_0::learning::name::John___round_0::concept::2
 + var_binary_source___round_0::learning::name::John = 0
flow_constraint_round_0::teaching::name::Alice:
 var_binary_round_0::concept::3___round_0::teaching::name::Alice
 - var_binary_round_0::teaching::name::Alice___drain = 0
flow_constraint_round_0::teaching::name::John:
 var_binary_round_0::concept::5___round_0::teaching::name::John
 - var_binary_round_0::teaching::name::John___drain = 0
flow_constraint_round_0::teaching::name::Mary:
 var_binary_round_0::concept::2___round_0::teaching::name::Mary
 - var_binary_round_0::teaching::name::Mary___drain = 0
flow_constraint_round_1::concept::2:
 - var_binary_round_1::concept::2___round_1::teaching::name::Mary
 + var_binary_round_1::learning::name::John___round_1::concept::2 = 0
flow_constraint_round_1::concept::3:
 - var_binary_round_1::concept::3___round_1::teaching::name::Alice = 0
flow_constraint_round_1::concept::5:
 - var_binary_round_1::concept::5___round_1::teaching::name::John
 + var_binary_round_1::learning::name::Alice___round_1::concept::5 = 0
flow_constraint_round_1::learning::name::Alice:
 - var_binary_round_1::learning::name::Alice___round_1::concept::5
 + var_binary_source___round_1::learning::name::Alice = 0
flow_constraint_round_1::learning::name::John:
 - var_binary_round_1::learning::name::John___round_1::concept::2
 + var_binary_source___round_1::learning::name::John = 0
flow_constraint_round_1::teaching::name::Alice:
 var_binary_round_1::concept::3___round_1::teaching::name::Alice
 - var_binary_round_1::teaching::name::Alice___drain = 0
flow_constraint_round_1::teaching::name::John:
 var_binary_round_1::concept::5___round_1::teaching::name::John
 - var_binary_round_1::teaching::name::John___drain = 0
flow_constraint_round_1::teaching::name::Mary:
 var_binary_round_1::concept::2___round_1::teaching::name::Mary
 - var_binary_round_1::teaching::name::Mary___drain = 0
flow_constraint_round_2::concept::2:
 - var_binary_round_2::concept::2___round_2::teaching::name::Mary
 + var_binary_round_2::learning::name::John___round_2::concept::2 = 0
flow_constraint_round_2::concept::3:
 - var_binary_round_2::concept::3___round_2::teaching::name::Alice = 0
flow_constraint_round_2::concept::5:
 - var_binary_round_2::concept::5___round_2::teaching::name::John
 + var_binary_round_2::learning::name::Alice___round_2::concept::5 = 0
flow_constraint_round_2::learning::name::Alice:
 - var_binary_round_2::learning::name::Alice___round_2::concept::5
 + var_binary_source___round_2::learning::name::Alice = 0
flow_constraint_round_2::learning::name::John:
 - var_binary_round_2::learning::name::John___round_2::concept::2
 + var_binary_source___round_2::learning::name::John = 0
flow_constraint_round_2::teaching::name::Alice:
 var_binary_round_2::concept::3___round_2::teaching::name::Alice
 - var_binary_round_2::teaching::name::Alice___drain = 0
flow_constraint_round_2::teaching::name::John:
 var_binary_round_2::concept::5___round_2::teaching::name::John
 - var_binary_round_2::teaching::name::John___drain = 0
flow_constraint_round_2::teaching::name::Mary:
 var_binary_round_2::concept::2___round_2::teaching::name::Mary
 - var_binary_round_2::teaching::name::Mary___drain = 0
into_drain: - drain + var_binary_round_0::teaching::name::Alice___drain
 + var_binary_round_0::teaching::name::John___drain
 + var_binary_round_0::teaching::name::Mary___drain
 + var_binary_round_1::teaching::name::Alice___drain
 + var_binary_round_1::teaching::name::John___drain
 + var_binary_round_1::teaching::name::Mary___drain
 + var_binary_round_2::teaching::name::Alice___drain
 + var_binary_round_2::teaching::name::John___drain
 + var_binary_round_2::teaching::name::Mary___drain = 0
round_0::person_is_never_teaching_one_and_learning_other_name::Alice:
 var_binary_round_0::concept::3___round_0::teaching::name::Alice
 + var_binary_round_0::learning::name::Alice___round_0::concept::5 <= 1
round_0::person_is_never_teaching_one_and_learning_other_name::John:
 var_binary_round_0::concept::5___round_0::teaching::name::John
 + var_binary_round_0::learning::name::John___round_0::concept::2 <= 1
round_0::person_is_never_teaching_one_and_learning_other_name::Mary:
 var_binary_round_0::concept::2___round_0::teaching::name::Mary <= 1
round_1::person_is_never_teaching_one_and_learning_other_name::Alice:
 var_binary_round_1::concept::3___round_1::teaching::name::Alice
 + var_binary_round_1::learning::name::Alice___round_1::concept::5 <= 1
round_1::person_is_never_teaching_one_and_learning_other_name::John:
 var_binary_round_1::concept::5___round_1::teaching::name::John
 + var_binary_round_1::learning::name::John___round_1::concept::2 <= 1
round_1::person_is_never_teaching_one_and_learning_other_name::Mary:
 var_binary_round_1::concept::2___round_1::teaching::name::Mary <= 1
round_2::person_is_never_teaching_one_and_learning_other_name::Alice:
 var_binary_round_2::concept::3___round_2::teaching::name::Alice
 + var_binary_round_2::learning::name::Alice___round_2::concept::5 <= 1
round_2::person_is_never_teaching_one_and_learning_other_name::John:
 var_binary_round_2::concept::5___round_2::teaching::name::John
 + var_binary_round_2::learning::name::John___round_2::concept::2 <= 1
round_2::person_is_never_teaching_one_and_learning_other_name::Mary:
 var_binary_round_2::concept::2___round_2::teaching::name::Mary <= 1
Bounds
0 <= var_binary_round_0::teaching::name::Alice___drain <= 5
0 <= var_binary_round_0::teaching::name::John___drain <= 5
0 <= var_binary_round_0::teaching::name::Mary___drain <= 5
0 <= var_binary_round_1::teaching::name::Alice___drain <= 5
0 <= var_binary_round_1::teaching::name::John___drain <= 5
0 <= var_binary_round_1::teaching::name::Mary___drain <= 5
0 <= var_binary_round_2::teaching::name::Alice___drain <= 5
0 <= var_binary_round_2::teaching::name::John___drain <= 5
0 <= var_binary_round_2::teaching::name::Mary___drain <= 5
Generals
var_binary_round_0::teaching::name::Alice___drain
var_binary_round_0::teaching::name::John___drain
var_binary_round_0::teaching::name::Mary___drain
var_binary_round_1::teaching::name::Alice___drain
var_binary_round_1::teaching::name::John___drain
var_binary_round_1::teaching::name::Mary___drain
var_binary_round_2::teaching::name::Alice___drain
var_binary_round_2::teaching::name::John___drain
var_binary_round_2::teaching::name::Mary___drain
Binaries
var_binary_round_0::concept::2___round_0::teaching::name::Mary
var_binary_round_0::concept::3___round_0::teaching::name::Alice
var_binary_round_0::concept::5___round_0::teaching::name::John
var_binary_round_0::learning::name::Alice___round_0::concept::5
var_binary_round_0::learning::name::John___round_0::concept::2
var_binary_round_1::concept::2___round_1::teaching::name::Mary
var_binary_round_1::concept::3___round_1::teaching::name::Alice
var_binary_round_1::concept::5___round_1::teaching::name::John
var_binary_round_1::learning::name::Alice___round_1::concept::5
var_binary_round_1::learning::name::John___round_1::concept::2
var_binary_round_2::concept::2___round_2::teaching::name::Mary
var_binary_round_2::concept::3___round_2::teaching::name::Alice
var_binary_round_2::concept::5___round_2::teaching::name::John
var_binary_round_2::learning::name::Alice___round_2::concept::5
var_binary_round_2::learning::name::John___round_2::concept::2
var_binary_source___round_0::learning::name::Alice
var_binary_source___round_0::learning::name::John
var_binary_source___round_1::learning::name::Alice
var_binary_source___round_1::learning::name::John
var_binary_source___round_2::learning::name::Alice
var_binary_source___round_2::learning::name::John
End
