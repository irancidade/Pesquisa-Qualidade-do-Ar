package net.sourceforge.jFuzzyLogic.demo.tipper;

import net.sourceforge.jFuzzyLogic.FIS;

public class TesteQualidade {
	public static void main(String[] args) throws Exception {
	    FIS fis = FIS.load("fcl/QualidadeAr.fcl", true); // Load from 'FCL' file
	    fis.setVariable("pm10", 33.92); // Set inputs
	    fis.setVariable("pm25", 33.92);
	    fis.setVariable("co",  188);
	    fis.setVariable("co2",428);
	    fis.evaluate(); // Evaluate

	    // Show output variable
	    System.out.println("Output value:" + fis.getVariable("qualidade").getValue()); 
	  }
	}


