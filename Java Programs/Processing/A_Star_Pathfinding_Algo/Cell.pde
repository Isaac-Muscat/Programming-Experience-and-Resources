class Cell{
  boolean wall = false;
  float f, g, h;
  int x, y;
  Cell came_from = null;
  ArrayList<Cell> neighbours;
  
  Cell(int x, int y){
    f = g = h = 0;
    this.x = x;
    this.y = y;
    neighbours = new ArrayList<Cell>();
  }
  
  void display(color c){
    stroke(0);
    fill(c);
    rect(x*ts, y*ts, ts, ts);
  }
  
  void find_neighbours(){
    if(x>0){ 
      if(grid[x-1][y].wall == false)neighbours.add(grid[x-1][y]);
    }
    if(x<w-1){
      if(grid[x+1][y].wall == false)neighbours.add(grid[x+1][y]);
    }
    if(y>0){
      if(grid[x][y-1].wall == false)neighbours.add(grid[x][y-1]);
    }
    if(y<w-1){ 
      if(grid[x][y+1].wall == false)neighbours.add(grid[x][y+1]);
    }
    
    
    
    if(x>0 && y>0){ 
      if(grid[x-1][y-1].wall == false)neighbours.add(grid[x-1][y-1]);
    }
    if(x<w-1 && y>0){
      if(grid[x+1][y-1].wall == false)neighbours.add(grid[x+1][y-1]);
    }
    if(y>0&&x>0){
      if(grid[x-1][y-1].wall == false)neighbours.add(grid[x-1][y-1]);
    }
    if(y<w-1&&x<w-1){ 
      if(grid[x+1][y+1].wall == false)neighbours.add(grid[x+1][y+1]);
    }
  }
  
}
