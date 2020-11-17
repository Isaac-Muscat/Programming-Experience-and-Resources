/* RiskSimulator.java
 * 
 * Risk Class 1 of 3
 * Isaac Muscat
 * 1/6/2020
 * 
 * This program is designed to simulate different 
 * attacking situations in the board game risk by 
 * repedeatdly executing different micro scenarios 
 * in the game and creating statistics based on the 
 * data. You might have to briefly look up the rules
 * of the game to understand this program.
 */
import javax.swing.*;

//Displays the Risk Game to the screen through the swing class and the main method.
public class RiskSimulator {
  //Frame size variables.
  public static final int width = 800;
  public static final int height = 800;
  //Setting up the frame.
  public RiskSimulator(){
    JFrame frame = new JFrame();
    frame.setVisible(true);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setSize(width, height);
    RiskGame game = new RiskGame();
    frame.add(game);
  }
  //main method runs the constructor.
  public static void main(String[] args) {
    javax.swing.SwingUtilities.invokeLater(new Runnable() {
      public void run() {
        RiskSimulator start = new RiskSimulator();
      }
    });
  }
  
  
  
 
}