import java.util.*;
public class stargame{
    
    public static void main(){
        Scanner sc= new Scanner(System.in);
        stargame ob=new stargame();
        System.out.println("Welcome to the Star Game");
        System.out.println("Enter your name:");
        String name=sc.nextLine();
        System.out.println(name +" ,you will have 21 stars and you will play with the computer \nOne can choose 1 or 2 or 3 or 4 stars in one go\nThe one picking the last star loses");
        System.out.println("Are you ready, enter yes or no");
        String ready=sc.nextLine();
        while(ready.tolower()=="yes"){
        for(int i=0;i<21;i++)
        System.out.println("*");
        int tstars=21;
        while(tstars!=1){
            System.out.println("Your turn:\n Enter the number of stars you wanna pick from 1 to 4");
            int stars=sc.nextInt();
            if(stars<5){
            tstars=tstars-stars;
            System.out.println("Stars  Remaining:");
            for(int i=0;i<tstars;i++)
            System.out.println("*");
            System.out.println("Computer's Turn:");
            int cstars=5-stars;
            tstars=tstars-cstars;
            System.out.println("Computer picks "+cstars+" stars.");
            System.out.println("Stars remaining:");
            for(int i=0;i<tstars;i++)
            System.out.println("*");
            }
            else{
                System.out.println("ERROR:PLease pick stars between 1 to 4(1 and 4 included)");
            }
            
        }
        System.out.println("You had to pick the last star, you lost to a bot.");
        System.out.println("DO you want to continue");
        String temp=sc.nextLine();
        ready=temp;



        

        

    }
    System.out.println("Bye. See you soon");
}
    

}