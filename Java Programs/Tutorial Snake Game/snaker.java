import javax.swing.*;
import java.awt.event.*;
import java.awt.*;

public class snaker {

  public static JFrame frame;
  
 public static void main(String[] args) {
   
  javax.swing.SwingUtilities.invokeLater(new Runnable() {

   @Override
   public void run() {
    frame = new JFrame();
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    final SnakeGame game = new SnakeGame();
    frame.add(game);
    frame.pack();
    frame.addComponentListener(new ComponentAdapter() {
      @Override
      public void componentResized(ComponentEvent componentEvent) {
         game.resized(frame.getWidth(), frame.getHeight());
      }
    });
    frame.setVisible(true);
   }
  });
 }
}