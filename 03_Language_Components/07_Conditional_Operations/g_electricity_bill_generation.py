# g_electricity_bill_generation
"""
Purpose: Electricity Board Current Bill Slab rates

    Electricity bill slabs
    -------------------------------------
    units Range     |    amount per unit
	-------------------------------------
    0 till 60       |   1.25
	60 till 100     |   2.00
	100 till 150    |   4.00
	150 till 250    |   7.00
	250 +           |  10.00

electricity cess : 2%
discount         : -1.11%

GST              : 7%

units consumed : 357
         60     +   40      + 50    + 100    + 107
         1.25/- + 2.00/-    + 4.00/-+ 7.00/- + 10/-

"""

units_consumed = 357

remaining_units = units_consumed
amount = 0

if units_consumed > 250:
    slab_units = remaining_units - 250  # 107
    amount += slab_units * 10.0

if 150 < remaining_units <= 250:
    slab_units = remaining_units - 150
    amount += slab_units * 7.00
    
if 100 < remaining_units <= 150
    slab_units = remaining_units - 100


    