import javax.swing.*;
import java.awt.*;

public class Test {
  
  public Test(){
    JFrame frame = new JFrame();
    frame.setVisible(true);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setSize(500, 500);
    Test2 test2 = new Test2();
    frame.add(test2);
  }
  
  public static void main(String[] args) {
    javax.swing.SwingUtilities.invokeLater(new Runnable() {
      public void run() {
        Test test = new Test();
      }
    });
  }
  
  
  
  
  
}
