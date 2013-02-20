import ActiveAnalysis
import ActiveStat
import 1553types
import iVDE
import BusMon
import time

Test = ActiveStat("MVB_FDG_APPROACH_LO_FQT_TP")
Test.covers("R000001", "R000002","R000003","R000004","R000005")

# Making a change that requires approval, approve me!

def testCase5(self):
	Test.testing("R000001", "R000005", "R000004")
	while(BusMon.get(1553types.Address("A12R2SA12W2")) != 0x0102)
		time.wait(1)
	iVDE.PIMFD.push("R4", "T4", "R2")
	if BusMon.get(1553types.Address("A12R2SA12W4")) == 0x0160:
		Test.fail("R000001")
	
	
