/* RiskTeam.java
 * 
 * Risk class 3 of 3
 * Isaac Muscat
 * 1/6/2020
 */
import javax.swing.*;
import java.awt.*;
import java.util.*;

//This class manages the individual team properties to use less code.
public class RiskTeam extends JPanel{
  //Variables for setup/display
  public int posX;
  public int posY;
  public int teamNum;
  public boolean inGame = false;
  
  //variables for setting team values
  public Color teamColor;
  public int numTroops = 0;
  public boolean attacking = false;
  public boolean defeat = false;
  
  //variables for individual simulation values
  public int simulationNumTroops = 0;
  public boolean simulationAttacking = false;
  
  //variables for statistics
  public int numFights = 0;
  public int numGameVictory = 0;
  public int numVictory = 0;
  public int numDefeat = 0;
  public int winPercentage = 0;
  public int lossPercentage = 0;
  public ArrayList<Integer> numTroopsLeft = new ArrayList<Integer>(); 
  public int averageTroopsLeft = 0;
  
  
  
  
  //Constructor for the 4 team objects
  public RiskTeam(int teamNum, Color color, int posX, int posY){
    this.teamNum = teamNum;
    teamColor = color;
    this.posX = posX;
    this.posY = posY;
  }
  
  //pre: User clicks on the team area. Passed in the paint() method.
  //post: Options for inputting different values for each team is displayed.
  public void displayTeamOptions(Graphics g){
    g.setColor(Color.WHITE);
    g.fillRect(posX + 10, posY + 150, RiskSimulator.width/4 - 20, RiskSimulator.height - 400);
    g.setColor(Color.BLACK);
    g.drawString("Team " + teamNum + " has " + numTroops + " troops.", posX + 12, posY + 180);
    //1 troop
    g.setColor(teamColor);
    g.fillRect(posX + 20, posY + 200, 50, 100);
    
    //5 troops
    g.setColor(teamColor);
    g.fillRect(posX + 75, posY + 200, 50, 100);
    
    //10 troops
    g.setColor(teamColor);
    g.fillRect(posX + 130, posY + 200, 50, 100);
    
    //1 troop
    g.setColor(teamColor);
    g.fillRect(posX + 20, posY + 310, 50, 100);
    
    //5 troops
    g.setColor(teamColor);
    g.fillRect(posX + 75, posY + 310, 50, 100);
    
    //10 troops
    g.setColor(teamColor);
    g.fillRect(posX + 130, posY + 310, 50, 100);
    
    g.setColor(Color.BLACK);
    g.drawString("+ 1", posX + 22, posY + 250);
    g.drawString("+ 5", posX + 77, posY + 250);
    g.drawString("+ 10", posX + 132, posY + 250);
    g.drawString("- 1", posX + 22, posY + 360);
    g.drawString("- 5", posX + 77, posY + 360);
    g.drawString("- 10", posX + 132, posY + 360);
    
    g.setColor(teamColor);
    g.fillRect(posX + 50, posY + 420, 100, 100);
    g.setColor(Color.BLACK);
    if(attacking){
      g.drawString("Attacking", posX + 62, posY + 450);
    }else{
      g.drawString("Defending", posX + 62, posY + 450);
    } 
  }
  
  //pre: Simulation is run and the result variables are set.
  //post: Displays the statistics and numbers about the individual team simulation to the user.
  public void displayTeamResults(Graphics g){
    g.setColor(Color.WHITE);
    g.fillRect(posX + 5, posY + 150, RiskSimulator.width/4 - 5, RiskSimulator.height - 400);
    g.setColor(Color.BLACK);
    g.drawString("Team " + teamNum + ":", posX + 5, posY + 180);
    g.drawString(" won " + numGameVictory + " simulations.", posX + 5, posY + 200);
    g.drawString(" had " + numFights + " fights.", posX + 5, posY + 220);
    g.drawString(" won " + numVictory + " fights.", posX + 5, posY + 240);
    g.drawString(" lost " + numDefeat + " fights.", posX + 5, posY + 260);
    g.drawString(" won " + winPercentage + "% of their fights.", posX + 5, posY + 280);
    g.drawString(" lost " + lossPercentage + "% of their fights.", posX + 5, posY + 300);
    g.drawString(" had " + averageTroopsLeft + " troops left on average.", posX + 5, posY + 320);
    g.drawString(" had " + numTroops + " troops originally.", posX + 5, posY + 420);
  }
  
  //pre: Simulation is run and mode is set to 3
  //post: All of the team statistic variables are set to be displayed 
  public void setResults(){
    winPercentage = 100*numVictory/ numFights;
    lossPercentage = 100*numDefeat/ numFights;
    
    int totalTroops = 0;
    for(int i = 0; i < numTroopsLeft.size(); i++){
      totalTroops += numTroopsLeft.get(i);
    }
    averageTroopsLeft = totalTroops/RiskGame.numSimulations;
  }
  
  //pre: User clicks on add troops to a team in the display.
  //post: "numTroops" is incremented based on which option is selected for that team.
  public void checkAddedTroops(int mouseX, int mouseY){
    if(inGame == true && mouseX > posX + 20 && mouseX < posX + 70 && mouseY > posY + 200 && mouseY < posY + 300){
      numTroops += 1;
    }else if(inGame == true && mouseX > posX + 75 && mouseX < posX + 125 && mouseY > posY + 200 && mouseY < posY + 300){
      numTroops += 5;
    }else if(inGame == true && mouseX > posX + 130 && mouseX < posX + 180 && mouseY > posY + 200 && mouseY < posY + 300){
      numTroops +=10;
    }
  }

  //pre: User clicks on remove troops to a team in the display.
  //post: "numTroops" is decremented based on which option is selected for that team.
  public void checkRemovedTroops(int mouseX, int mouseY){
    if(inGame == true && mouseX > posX + 20 && mouseX < posX + 70 && mouseY > posY + 310 && mouseY < posY + 410 && numTroops > 0){
      numTroops -= 1;
    }else if(inGame == true && mouseX > posX + 75 && mouseX < posX + 125 && mouseY > posY + 310 && mouseY < posY + 410 && numTroops >= 5){
      numTroops -= 5;
    }else if(inGame == true && mouseX > posX + 130 && mouseX < posX + 180 && mouseY > posY + 310 && mouseY < posY + 410 && numTroops >= 10){
      numTroops -= 10;
    }
  }
  //pre: Checks if user selected the attack button.
  //post: Toggles whether the team will be attacking or defending in the simlation.
  public void checkAttacking(int mouseX, int mouseY){
    if(inGame == true && mouseX > posX + 50 && mouseX < posX + 150 && mouseY > posY +420 && mouseY < posY + 520){
      attacking = !attacking;
    }
  }
  
  //pre: Checks if the user clicked in the team area.
  //post: Sets the team status to "inGame" allowing other options to be shown.
  public void checkSelectedTeam(int mouseX, int mouseY){
    if(mouseX > posX && mouseX < posX + RiskSimulator.width/4 && mouseY > posY && mouseY < posY + RiskSimulator.height - 200){
      inGame = true;
    }
  }
  
  //pre: The method "repaint()" is called in the main thread in RiskGame.
  //post: Each team graphics mode is displayed to the user.
  public void paint(Graphics g){
    super.paintComponent(g);
    g.setColor(teamColor);
    g.fillRect(posX, posY, RiskSimulator.width/4, RiskSimulator.height);
    g.setColor(Color.BLACK);
    g.drawString("Team " + teamNum, posX + 50, RiskSimulator.height/8);
    
    if(inGame && RiskGame.mode == 1){
      displayTeamOptions(g);
    }else if(inGame && RiskGame.mode == 3){
      displayTeamResults(g);
    }
  }
}
  