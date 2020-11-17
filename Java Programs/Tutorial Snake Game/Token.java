import java.awt.*;
import java.util.*;

public class Token {
 
 private int blockSizeScale = 60;
 private Snake snake;
 private Dimension bounds;
 private Random rand = new Random();
 private Point token = new Point();
 private int blockSize;
 private int score = 0;
 
 public Token(Snake s, Dimension map) {
  this.snake = s;
  this.bounds = map;
  if (bounds.getWidth() <= bounds.getHeight())
   blockSize = (int) (bounds.getWidth()/blockSizeScale);
  else
   blockSize = (int) (bounds.getHeight()/blockSizeScale);
  generateToken();
 }
 
 private void generateToken() {
  do {
   token.setX(rand.nextInt((int) bounds.getWidth()/blockSize-1)*blockSize);
   token.setY(rand.nextInt((int) (bounds.getHeight()-40)/blockSize-1)*blockSize);
  } while (snake.checkTokenOverlay(token));
 }
 
 public void paint(Graphics g) {
  g.setColor(Color.GREEN);
  g.fillRect(token.getX(), token.getY(), blockSize, blockSize);
  g.drawString("Score: " +Integer.toString(score), (int)bounds.getWidth()/2-30, (int) bounds.getHeight()/5);
  if (checkTokenCollision()) {
   score++;
   generateToken();
   snake.elongate();
  }
 }
 
 private boolean checkTokenCollision() {
  if (snake.getX() == token.getX() && snake.getY() == token.getY()) 
    return true;
  else
   return false;
 }
 
 public int getScore() {
  return score;
 }

 public void setBounds(Dimension s) {
 int oldBlockSize = blockSize;
  bounds = s;
  if (bounds.getWidth() <= bounds.getHeight())
   blockSize = (int) (bounds.getWidth()/blockSizeScale);
  else
   blockSize = (int) (bounds.getHeight()/blockSizeScale);
  
  token.setX(token.getX()/oldBlockSize*blockSize);
  token.setY(token.getY()/oldBlockSize*blockSize);
 }
}