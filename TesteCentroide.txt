package net.sourceforge.jFuzzyLogic.demo.tipper;

import net.sourceforge.jFuzzyLogic.FIS;
import net.sourceforge.jFuzzyLogic.FunctionBlock;
import net.sourceforge.jFuzzyLogic.Gpr;
import net.sourceforge.jFuzzyLogic.plot.JFuzzyChart;
import net.sourceforge.jFuzzyLogic.rule.Variable;

/**
 *  Teste função bloco deslocar centroide
 * @author iranc
 *
 */

public class TestCentroid {
	
	public static void main(String[] args) throws Exception {
		// Load from 'FCL' file
		String fileName = "fcl/QualidadeAr.fcl";
		FIS fis = FIS.load(fileName, true);
		if (fis == null) { // Error while loading?
			System.err.println("Can't load file: '" + fileName + "'");
			return;
		}
		
		//Mostrar as regras da base de conhecimento
		FunctionBlock functionBlock = fis.getFunctionBlock(null);
		JFuzzyChart.get().chart(functionBlock);
         
		///Set entradas
		functionBlock.setVariable("pm10", 33.92);
		functionBlock.setVariable("pm25",33.92);
		functionBlock.setVariable("co2", 188);
		functionBlock.setVariable("co", 428);
		
		// Evaluate 
				functionBlock.evaluate();
				
	   // Mostrar variáveis
				
				Variable qualify = functionBlock.getVariable("qualidade");
				JFuzzyChart.get().chart(qualify, qualify.getDefuzzifier(), true);
				Gpr.debug("boa[pm10]: " + functionBlock.getVariable("pm10").getMembership("boa"));
				Gpr.debug("boa[pm25]: " + functionBlock.getVariable("pm25").getMembership("boa"));
				Gpr.debug("boa[co]: " + functionBlock.getVariable("co").getMembership("boa"));
				Gpr.debug("boa[co2]: " + functionBlock.getVariable("co2").getMembership("boa"));
				
      //imprime regras
				// Print ruleSet
				System.out.println(functionBlock);
				System.out.println("qualidade:" + functionBlock.getVariable("qualidade").getValue());
		
	}

}
