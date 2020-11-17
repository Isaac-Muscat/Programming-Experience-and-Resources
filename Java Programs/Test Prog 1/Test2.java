import javax.swing.*;
import java.awt.*;
import java.util.*;
import java.awt.event.*;


public class Test2 extends JPanel implements KeyListener, Runnable{
  
  public boolean o = false;
  //public int x = 10;
  //public int y = 10;
  public Thread t;
  //public ArrayList<Block> body = new ArrayList<Block>();
  
  
  
  public Test2() {
    //body.add(new Block(x, y));
    start();
  }
  public void start(){
    t = new Thread(this);
    t.start();
  }
  
  @Override
  public void run(){
    //while (body.size() < 500){
    
      repaint();
      try {
      Thread.sleep(500);
     }
      catch(InterruptedException ex) {}
      o = true;
      repaint();
      //body.add(new Block(body.get(body.size()-1).getX() + 1, body.get(body.size()-1).getY()));
    //}
  }
    
  public void paint(Graphics g){
    super.paintComponent(g);
    if (o == true) {
      
      g.setColor(Color.RED);
      g.fillRect(0, 0, 100, 100);
    }
    //for (int i = 0; i < body.size(); i++){
    //g.fillRect(body.get(i).getX(),body.get(i).getY(), 10, 10);
    
  }
  @Override
  public void keyPressed(KeyEvent e){}
  @Override
  public void keyReleased(KeyEvent e){}
  @Override
  public void keyTyped(KeyEvent e){}
}