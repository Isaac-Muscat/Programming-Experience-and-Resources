/* RiskGame.java
 * 
 * Risk class 2 of 3
 * Isaac Muscat
 * 1/6/2020
 */
import java.lang.Math;
import javax.swing.*;
import java.awt.*;
import java.util.*;
import java.awt.event.*;

public class RiskGame extends JPanel implements MouseListener, Runnable {
  //Variables
  public ArrayList<RiskTeam> team = new ArrayList<RiskTeam>();//Holds the 4 team objects.
  public boolean running = false;//Starts the program when the thread starts.
  public static int mode = 1;//Sets the mode to execute the three methods: setup, simulation, and result.
  public static int numSimulations = 1000;//The number of times the simulation is run.
  public Thread thread;//The thread which is used in order to use the "paint()" method.
  public int mouseY;//X position of the user mouse.
  public int mouseX;//Y position of the user mouse.
  
  //Additional setup for the program
  public RiskGame() {
    createTeams();
    addMouseListener(this);
    start();
  }
  
  //pre: RiskGame object is created in RiskSimulation.
  //post: Thread is created and started.
  public void start() {
    running = true;
    thread = new Thread(this);
    thread.start();
  }
  
  @Override
  //The Main Game Loop/Thread.
  public void run() {
    if(running){
      setup();//mode == 1
      simulation();//mode == 2
      result();//mode == 3
    }
  }
  
  //pre: The main thread has started. mode == 1.
  //post: The options for the setup of the simulation for each team is displayed.
   public void setup(){
    while(mode == 1) {
      mouseX = 0;
      mouseY = 0;
      delay(50);
      checkSelection();
      repaint();
    }
  }
  
  //pre: The user clicks start after the setup is completed. mode == 2.
  //post: The risk simulation is run 1000 times with different object variables being set based on the events.
  public void simulation(){
    //Arrays storing the attacking and defending teams.
    ArrayList<RiskTeam> attackers = new ArrayList<RiskTeam>();
    ArrayList<RiskTeam> defenders = new ArrayList<RiskTeam>();
    
    //Runs the simulation "numSimulation" times.
    for(int j = 0;j<numSimulations;j++){
      resetSimulation();//resets the team variables.
      
      //Runs one simulation of the game until their is one team left
      while(!winner()){
        //clears the arrays
        attackers.clear();
        defenders.clear();
        
        //Sets the attackers and defenders in the proper array.
        for(int i = 0;i < team.size();i++){
          if(team.get(i).simulationAttacking && team.get(i).inGame && !team.get(i).defeat && team.get(i).numTroops > 0){
            attackers.add(team.get(i));
          }else{
            defenders.add(team.get(i));
          }
        }
        
        //Pairs up the attackers and defenders to fight until one team loses.
        for(int i = 0;i < defenders.size() && i < attackers.size();i++){
          while(defenders.get(i).defeat == false && attackers.get(i).defeat == false){
            //One iteration of a turn.
            rollDice(attackers.get(i), defenders.get(i));
          }
          //For stats.
          defenders.get(i).numFights += 1;
          attackers.get(i).numFights += 1;
        }
      
        //Randomize attackers and defenders
        for(int i = 0;i < team.size();i++){
          if(team.get(i).inGame == true && team.get(i).defeat == false && team.get(i).numTroops > 0){
            int num = randomNum(1,2);
            if(num == 1){
              team.get(i).simulationAttacking = true;
            }else{
              team.get(i).simulationAttacking = false;
            }
          }
        }
      }
      
      //For stats.
      for(int i = 0;i<4;i++){
        team.get(i).numTroopsLeft.add(team.get(i).simulationNumTroops);
          if(team.get(i).defeat == false && team.get(i).inGame == true){
            team.get(i).numGameVictory += 1;
          }
        }
    }
    //Next method.
    mode = 3;
  }
  
  //pre: Simulation is run. mode == 3.
  public void result(){
    if(mode == 3){
      //Sets team results if they were added in the simulation.
      for(int i = 0; i<team.size();i++){
        if(team.get(i).inGame){
          team.get(i).setResults();
        }
      }
      //Uses paint() to display the team stats.
      repaint();
    }
  }
  
  //pre: A new simulation is started.
  //post: Resets the team variables to the set user values.
  public void resetSimulation(){
    for(int i = 0;i < team.size(); i++){
        team.get(i).simulationNumTroops = team.get(i).numTroops;
        team.get(i).simulationAttacking = team.get(i).attacking;
        team.get(i).defeat = false;
      }
  }
  
  //pre: One iteration of turns is run.
  //post: Checks if their is one team left.
  public boolean winner(){
    int numAlive = 0;
    for(int i = 0;i < team.size();i++){
      if(team.get(i).inGame == true && team.get(i).defeat == false && team.get(i).numTroops > 0){
        numAlive += 1;
      }
    }
    if(numAlive > 1){
      return false;
    }else{
      return true;
    }
  }
  
  
  //pre: Attackers and defenders are set in "simulation()".
  //post: Two teams roll dice according to their troop counts and lose troops depending on the results.
  public void rollDice(RiskTeam attacker, RiskTeam defender){
    //Checks that each team has more than one troop.
    if(attacker.simulationNumTroops > 0 && defender.simulationNumTroops > 0){
      ArrayList<Integer> attackRoll = new ArrayList<Integer>();
      ArrayList<Integer> defendRoll = new ArrayList<Integer>();
      
      //Adds random dice rolls to the attacking array.
      if(attacker.simulationNumTroops > 0){
        for(int i = 0;i< attacker.simulationNumTroops && i < 3;i++){
          attackRoll.add(randomNum(1,6));
        }
      }
      //Adds random dice rolls to the defending array.
      if(defender.simulationNumTroops > 0){
        for(int i = 0;i< defender.simulationNumTroops && i < 2;i++){
          defendRoll.add(randomNum(1,6));
        }
      }
      //Ranks the values(Dice Rolls) in the arrays from greatest to least.
      Collections.sort(attackRoll);
      Collections.sort(defendRoll);
      
      //Compares the each dice roll between the attacking and defending team.
      for(int i = 0;i<attackRoll.size() && i< defendRoll.size();i++){
        if(attackRoll.get(i) <= defendRoll.get(i)){
          attacker.simulationNumTroops -= 1;
        }else{
          defender.simulationNumTroops -= 1;
        }
      }
    
      //Sets values based on which team wins the fight
      if(attacker.simulationNumTroops == 0){
        attacker.defeat = true;
        attacker.numDefeat += 1;
        defender.numVictory += 1;
      }else if (defender.simulationNumTroops == 0){
        defender.defeat = true;
        defender.numDefeat += 1;
        attacker.numVictory += 1;
      }
    }
  }
  
  
  //Creates the four teams
  public void createTeams(){
    team.add(new RiskTeam(1, new Color(255, 204, 204), 0, 0));
    team.add(new RiskTeam(2, new Color(204, 224, 255), RiskSimulator.width/4, 0));
    team.add(new RiskTeam(3, new Color(214, 245, 214), RiskSimulator.width/2, 0));
    team.add(new RiskTeam(4, new Color(255, 255, 204), RiskSimulator.width * 3/4, 0));
  }
  
  //pre: The user mouse position is set and the "setup()" method is called.
  //post: Checks what options the user selects for each team in mode 1.
  public void checkSelection(){
    for(int i = 0;i< team.size();i++){
      team.get(i).checkSelectedTeam(mouseX, mouseY);
      team.get(i).checkAddedTroops(mouseX, mouseY);
      team.get(i).checkRemovedTroops(mouseX, mouseY);
      team.get(i).checkAttacking(mouseX, mouseY);
    }
    //Checks if the user wants to run the simulation with the given variables.
    if(mouseX > RiskSimulator.width * 2/8 && mouseX < RiskSimulator.width * 2/8 + RiskSimulator.width / 2 &&
       mouseY > RiskSimulator.height * 6/8 && mouseY < RiskSimulator.height * 6/8 + RiskSimulator.height / 4 - 50){
      mode = 2;
    }
  }
  
  //Draws each team object's graphics for the result or mode 3.
  public void drawResult(Graphics g){
    for(int i = 0;i<team.size();i++){
      team.get(i).paint(g);
    }
  }
  
  //Draws the team  graphics for the setup or mode 1.
  public void drawSetup(Graphics g){
    for(int i = 0;i<team.size();i++){
      team.get(i).paint(g);
    }
    
    g.setColor(Color.WHITE);
    g.fillRect(RiskSimulator.width * 2/8, RiskSimulator.height * 6/8, RiskSimulator.width / 2, RiskSimulator.height / 4 - 50);
    g.setColor(Color.BLACK);
    g.drawString("Click Here to start", RiskSimulator.width * 2/8 + 20, RiskSimulator.height * 6/8 + 30);
    g.drawString("Click on a team to use", RiskSimulator.width * 2/8 + 20, RiskSimulator.height * 6/8 + 60);
    g.drawString("Adjust amount of players", RiskSimulator.width * 2/8 + 20, RiskSimulator.height * 6/8 + 90);
    g.drawString("And run the simulator", RiskSimulator.width * 2/8 + 20, RiskSimulator.height * 6/8 + 120);
    g.drawString("The simulation will run " + numSimulations + " times", RiskSimulator.width * 2/8 + 180, RiskSimulator.height * 6/8 + 30);
  }
  
  
  //pre: "repaint()" method is called  in a loop in the setup, simualtion, and result methods.
  //post: screen is drawn white and graphics are drawn for mode 1 or mode 2 displaying information for each team.
  public void paint(Graphics g) {
    super.paintComponent(g);
    g.setColor(Color.WHITE);
    g.fillRect(0, 0, RiskSimulator.width, RiskSimulator.height);
    
    if(mode == 1){
      drawSetup(g);
    }else if(mode == 3){
      drawResult(g);
    }
  }
  
  //Easier to create a pause in the program rather than writing out all that code every time.
  public static void delay(int milli){
    try {
        Thread.sleep(milli);
      }catch(InterruptedException ex) {}
  }
  
  //pre: Rolling dice in the risk program. Easier to generate random numbers.
  //post: a random number between "min" and "max" is generated. 
  public static int randomNum(int min, int max){
    int result;
    result = (int) (Math.random() * max + min);
    return result;
  }
  
  @Override
  public void mouseExited(MouseEvent e){}
  @Override
  public void mouseEntered(MouseEvent e){}
  @Override
  public void mouseReleased(MouseEvent e){}
  @Override
  public void mousePressed(MouseEvent e){}
  
  //pre: User enters mouse input.
  //post: User's mouse position is set.
  @Override
  public void mouseClicked(MouseEvent e){
    
  mouseX = e.getX();
  mouseY = e.getY();
  
  }
  
}