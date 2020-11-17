import javax.swing.*;
import java.awt.*;
import java.util.*;
import java.awt.event.*;

public class Game extends JPanel implements KeyListener, Runnable {
  
  public boolean running = false;
  public Thread thread;
  public TronPlayer player_1;
  public TronPlayer player_2;
  
  public Game() {
    player_1 = new TronPlayer(120/Tron.scale, Tron.height/2/Tron.scale, 1);
    player_2 = new TronPlayer((Tron.width - 120)/Tron.scale, Tron.height/2/Tron.scale, -1);

    addKeyListener(this);
    start();
  }
  
  public void start() {
    running = true;
    thread = new Thread(this);
    thread.start();
  }
  
  @Override
  public void run() {
    while(running) {
      repaint();
      try {
        thread.sleep(50);
      }catch(InterruptedException ex) {}
      player_1.move();
      player_2.move();
      
    }
  }
  
  public void paint(Graphics g) {
    super.paintComponent(g);
    g.setColor(Color.BLACK);
    g.fillRect(0, 0, Tron.width, Tron.height);
    player_1.paint(g);
    player_2.paint(g);
    
    
  }

  
  
  @Override
  public void keyPressed(KeyEvent e){
    
    if (e.getKeyCode() == KeyEvent.VK_UP){
      player_1.setDirection(1);
      
   } else if (e.getKeyCode() == KeyEvent.VK_LEFT){
      player_1.setDirection(2);
      
   } else if (e.getKeyCode() == KeyEvent.VK_DOWN){
      player_1.setDirection(3);
      
   } else if (e.getKeyCode() == KeyEvent.VK_RIGHT){
      player_1.setDirection(4);
      
    }
   
   if (e.getKeyCode() == KeyEvent.VK_W){
      player_2.setDirection(1);
      
   } else if (e.getKeyCode() == KeyEvent.VK_A){
      player_2.setDirection(2);
      
   } else if (e.getKeyCode() == KeyEvent.VK_S){
      player_2.setDirection(3);
      
   } else if (e.getKeyCode() == KeyEvent.VK_D){
      player_2.setDirection(4);
      
    }
  }
  
  
  @Override
  public void keyReleased(KeyEvent e) {}
  @Override
  public void keyTyped(KeyEvent e){}
}
  
  
  
  
