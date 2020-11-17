import javax.swing.*;

//import java.util.*;
//import java.awt.event.*;

public class Tron {
  public static int width = 500;
  public static int height = 500;
  public static int scale = 5;
  
  public Tron(){
    
    JFrame frame = new JFrame();
    frame.setVisible(true);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setSize(width, height);
    Game tron = new Game();
    frame.add(tron);
    
    
  }
  
  public static void main(String[] args) {
    javax.swing.SwingUtilities.invokeLater(new Runnable() {
      public void run() {
        Tron tron = new Tron();
      }
    });
  }
}
      