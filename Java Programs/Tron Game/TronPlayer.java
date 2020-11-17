import java.util.*;
import java.awt.*;
import javax.swing.*;

public class TronPlayer extends JPanel {
  
  private int xDirection = 0;
  private int yDirection = 0;
  public ArrayList<TronBlock> body;
  
  
  public TronPlayer(int startX, int startY, int dx) {
    xDirection = dx;
    body = new ArrayList<TronBlock>();
    body.add(new TronBlock(startX, startY));
   
  }
  public void setDirection(int direction){
    if (direction == 1){
      xDirection = 0;
      yDirection = -1;
    }else if (direction == 2){
      xDirection = -1;
      yDirection = 0;
    }else if (direction == 3){
      xDirection = 0;
      yDirection = 1;
    }else if (direction == 4){
      xDirection = 1;
      yDirection = 0;
    }
  }
  public void move(){
    body.add(new TronBlock(body.get(body.size()-1).getX() + xDirection, 
                           body.get(body.size()-1).getY() + yDirection));
  }
  
  public void paint(Graphics g) {
    for(int i = 0; i < body.size(); i++){
      g.setColor(Color.BLUE);
      g.fillRect(body.get(i).getX() * Tron.scale, body.get(i).getY() * Tron.scale, Tron.scale, Tron.scale);
    }
  }
}