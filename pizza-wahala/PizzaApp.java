import java.util.Scanner;

public class PizzaApp{

	public static void main(String... args){

		Scanner input = new Scanner(System.in);
		
		System.out.print("Enter Pizza Type: ");
		String pizzaType = input.nextLine();	
		System.out.print("Enter number of Guests: ");
		int guests = input.nextInt();

//		System.out.print("Enter Pizza Type: ");
//		String pizzaType = input.nextLine();	

		int numberOfSlices;
		int pricePerBox;
		double boxesOfPizza = 0;
		int slicesLeftover = 0;
		double price = 0;
		double division = 0;
	
		if(pizzaType.equalsIgnoreCase("Sapa Size")){

			numberOfSlices = 4;
			pricePerBox = 2000;

			boxesOfPizza = Math.round(guests / numberOfSlices);
			slicesLeftover = numberOfSlices - guests % numberOfSlices;
			price = pricePerBox * boxesOfPizza;

		}else if(pizzaType.equalsIgnoreCase("Small Money")){

			numberOfSlices = 6;
			pricePerBox = 2400;

			boxesOfPizza = Math.round(guests / numberOfSlices);
			slicesLeftover = numberOfSlices - guests % numberOfSlices;
			price = pricePerBox * boxesOfPizza;

		}else if(pizzaType.equalsIgnoreCase("Big Boys")){

			numberOfSlices = 8;
			pricePerBox = 3000;

			boxesOfPizza = Math.round(guests / numberOfSlices);
			slicesLeftover = numberOfSlices - guests % numberOfSlices;
			price = pricePerBox * boxesOfPizza;

		}else if(pizzaType.equalsIgnoreCase("Odogwu")){

			numberOfSlices = 12;
			pricePerBox = 4200;

			division = guests / numberOfSlices;
			boxesOfPizza = Math.ceil(division);
			slicesLeftover = numberOfSlices - guests % numberOfSlices;
			price = pricePerBox * boxesOfPizza;

		}else{

			System.out.println("Invalid Pizza Type Oga");

		}


		System.out.println("Number of boxes of pizza to buy = " + boxesOfPizza);
		System.out.println("Number of left over slices after serving = " + slicesLeftover);
		System.out.println("Prices = " + price);



	}




}