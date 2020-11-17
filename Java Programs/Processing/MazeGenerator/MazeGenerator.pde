
int cols, rows;
public static final int scale = 40;
Cell current, next;
ArrayList<Cell> stack = new ArrayList<Cell>();
Cell[][] grid;

public void setup(){
  size(800, 800);
  
  cols = width/scale;
  rows = height/scale;
  grid = new Cell[cols][rows];
  
  for(int y=0;y<rows;y++){
    for(int x=0;x<cols;x++){
      grid[y][x] = new Cell(x, y);
    }
  }
  current = grid[0][0];
  stack.add(current);
  
}



public void draw(){
  delay(0);
  background(255);
  
  for(int y=0;y<rows;y++){
    for(int x=0;x<cols;x++){
      grid[y][x].show();
    }
  }
  current.visited = true;
  current.highlight();
  
  if(checkNeighbour(current)){
    next = getNeighbour(current);
    next.visited = true;
    stack.add(current);
    removeWalls(current, next);
    current = next;
    
    
  }else if(stack.size() > 1){
    stack.remove(stack.size() - 1);
    current = stack.get(stack.size() - 1);
  }else{
    fill(0, 255, 0);
    rect(grid[rows - 1][cols - 1].x * scale + scale/4, grid[rows - 1][cols - 1].y * scale + scale/4, scale/2, scale/2);
  }
}


public boolean checkNeighbour(Cell current){
  int x = current.x;
  int y = current.y;
  if(y > 0){
    if(grid[y-1][x].visited == false){
      return true;
    }
  }
  if(x < cols-1){
    if(grid[y][x+1].visited == false){
      return true;
    }
  }
  if(y < rows-1){
    if(grid[y+1][x].visited == false){
      return true;
    }
  }
  if(x > 0){
    if(grid[y][x-1].visited == false){
      return true;
    }
  }
  return false;
}

public void removeWalls(Cell a,Cell b){
  
  int x = a.x - b.x;
  if(x==1){
    a.walls[3] = false;
    b.walls[1] = false;
  }else if(x==-1){
    a.walls[1] = false;
    b.walls[3] = false;
  }
  
  int y = a.y - b.y;
  if(y==1){
    a.walls[0] = false;
    b.walls[2] = false;
  }else if(y==-1){
    a.walls[2] = false;
    b.walls[0] = false;
  }
}

public Cell getNeighbour(Cell current){
  ArrayList<Cell> neighbours = new ArrayList<Cell>();
  
  int x = current.x;
  int y = current.y;
  Cell top = grid[0][0]; ;
  Cell right = grid[0][0];;
  Cell bottom = grid[0][0];;
  Cell left = grid[0][0];;
  
  if (y > 0) {
    top    = grid[y-1][x];
  }else {
    top    = grid[0][0];
  }
  if (x < cols-1) {
    right  = grid[y][x+1];
  }else {
    right    = grid[0][0];
  }
  if (y < rows-1) {
    bottom = grid[y+1][x];
  }else{
    bottom    = grid[0][0];
  }
  if (x > 0) {
    left   = grid[y][x-1];
  }else {
    left    = grid[0][0];
  }
  
  if(!top.visited){
    neighbours.add(top);
  }
  if(!right.visited){
    neighbours.add(right);
  }
  if(!bottom.visited){
    neighbours.add(bottom);
  }
  if(!left.visited){
    neighbours.add(left);
  }
  
  int r = (int)random(0, neighbours.size());
  return neighbours.get(r);
  
}
