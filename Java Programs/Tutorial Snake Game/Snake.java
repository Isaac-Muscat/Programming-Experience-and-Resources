import java.awt.*;
import java.util.*;

public class Snake {

 
 public static int NORTH = 1;
 public static int SOUTH = -1;
 public static int EAST = 2;
 public static int WEST = -2;
 
 private int blockSizeScale = 60;
 private int blockSize;
 private ArrayList<Point> snake;
 private int xDir = 0;
 private int yDir = 0;
 private int currentDir = 0;
 private Point last = new Point();
 private Dimension bounds;
 private boolean elongate = false;
 private boolean elongate2 = false;
 
 public Snake(int size, int startX, int startY, int direction, Dimension mapBounds) {
  bounds = mapBounds;
  if (bounds.getWidth() <= bounds.getHeight())
   blockSize = (int) (bounds.getWidth()/blockSizeScale);
  else
   blockSize = (int) (bounds.getHeight()/blockSizeScale);
  
  startX = startX/blockSize;
  startX = startX*blockSize;
  startY = startY/blockSize;
  startY = startY*blockSize;
  
  setDirection(direction);
  snake = new ArrayList<Point>();
  snake.add(new Point(startX, startY));
  for (int i = 1; i <= size-1; i++) {
   if (direction == Snake.NORTH)
    snake.add(new Point(startX, startY-i*blockSize));
   else if (direction == Snake.SOUTH) 
    snake.add(new Point(startX, startY+i*blockSize));
   else if (direction == Snake.EAST) 
    snake.add(new Point(startX-i*blockSize, startY));
   else if (direction == Snake.WEST)
    snake.add(new Point(startX+i*blockSize, startY));
   else 
    snake.add(new Point(startX-i*blockSize, startY));
  }
  
 }
 
 public void paint(Graphics g) {
  g.setColor(Color.WHITE);
  for (int i = 0; i < snake.size()-1; i++)
   g.fillRect(snake.get(i).getX(), snake.get(i).getY(), blockSize, blockSize);
 }
 
 public void move() {
   if (checkCollision() == false) {
     int newX = snake.get(0).getX() + xDir;
     int newY = snake.get(0).getY() + yDir;
     
     last.setX(snake.get(snake.size()-1).getX());
     last.setY(snake.get(snake.size()-1).getY());
     for (int i = snake.size()-1; i > 0; i--) {
       snake.get(i).setX(snake.get(i-1).getX());
       snake.get(i).setY(snake.get(i-1).getY());
     }
     
     if (elongate) {
       snake.add(new Point(last.getX(), last.getY()));
       elongate = false;
       elongate2 = true;
     }
     
     if (elongate2) {
       snake.add(new Point(last.getX(), last.getY()));
       elongate2 = false;
     }
     
     snake.get(0).setX(newX);
     snake.get(0).setY(newY);
   }
 }

 public void setDirection(int direction) {
  if (currentDir != direction*-1) {
   if (direction == Snake.NORTH) {
    yDir = -blockSize;
    xDir = 0;
    currentDir = Snake.NORTH;
   }
   else if (direction == Snake.SOUTH) {
    yDir = blockSize;
    xDir = 0;
    currentDir = Snake.SOUTH;
   }
   else if(direction == Snake.EAST) {
    xDir = blockSize;
    yDir = 0;
    currentDir = Snake.EAST;
   }
   else if (direction == Snake.WEST) {
    xDir = -blockSize;
    yDir = 0;
    currentDir = Snake.WEST;
   }
  }
 }
 
 public void setBounds(Dimension s) {
  int oldBlockSize = blockSize;
  bounds = s;
  if (bounds.getWidth() <= bounds.getHeight())
   blockSize = (int) (bounds.getWidth()/blockSizeScale);
  else
   blockSize = (int) (bounds.getHeight()/blockSizeScale);
  for (int i = 0; i < snake.size(); i++) {
    snake.get(i).setX(snake.get(i).getX()/oldBlockSize*blockSize);
    snake.get(i).setY(snake.get(i).getY()/oldBlockSize*blockSize);
  }
 }
 
 public boolean checkCollision() {

  if (snake.get(0).getX() < 0 || snake.get(0).getX() >= bounds.getWidth()-blockSize*2 || snake.get(0).getY() < 0 || snake.get(0).getY() >= bounds.getHeight()-blockSize-40)
   return true;
  
  for (int i = 1; i < snake.size(); i++) {
   if (snake.get(i).getX() == snake.get(0).getX() && snake.get(i).getY() == snake.get(0).getY())
    return true;
  }
  return false;  
 }

 public int getBlockSize() {
  return blockSize;
 }
 
 public int getX() {
  return snake.get(0).getX();
 }
 
 public int getY() {
  return snake.get(0).getY();
 }

 public boolean checkTokenOverlay(Point token) {
  for (int i = 0; i < snake.size(); i++) {
   if ((Math.sqrt(Math.pow(snake.get(i).getX()- token.getX(), 2) +  Math.pow(snake.get(i).getY()-token.getY(), 2)) < blockSize))
    return true;
  }
  return false;
 }
 
 public void elongate() {
  elongate = true;
  
 }
}