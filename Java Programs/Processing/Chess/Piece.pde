class Piece{
  int x, y;
  int ax, ay;
  boolean white, selected;
  PImage img;
  
  Piece(int x, int y, boolean white){
    this.x = x;
    this.y = y;
    ax = x*ts + ts/2;
    ay = y*ts + ts/2;
    
    selected = false;
    this.white = white;
  }
  
  void snap_piece(){
    ax = x*ts + ts/2;
    ay = y*ts + ts/2;
  }
  
  Piece check_taken(int x2, int y2, Board board, int index){
    for(Piece p: board.pieces){
      if(index != board.pieces.indexOf(p) && white != p.white && x2 == p.x && y2 == p.y){
        return p;
      }
    }
    return null;
  }
  
  boolean piece_at(int x2, int y2, ArrayList<Piece> pieces, int index){
    for(Piece p: pieces){
      if(pieces.indexOf(p) != index && p.x == x2 && p.y == y2)return true;
    }
    return false;
  }
  
  boolean can_move(int x2, int y2, Board board, int index){
    return true;
  }
  
  boolean passed_through(int x2, int y2, ArrayList<Piece> pieces, int index){
    int x_steps = x2-x;
    int y_steps = y2-y;
    if(x_steps != 0 && x_steps <0)x_steps+=1;
    if(x_steps != 0 && x_steps >0)x_steps-=1;
    if(y_steps != 0 && y_steps <0)y_steps+=1;
    if(y_steps != 0 && y_steps >0)y_steps-=1;
    while(x_steps != 0 || y_steps != 0){
      if(piece_at(x+x_steps, y+y_steps, pieces, index))return true;
      if(x_steps != 0 && x_steps <0)x_steps+=1;
      if(x_steps != 0 && x_steps >0)x_steps-=1;
      if(y_steps != 0 && y_steps <0)y_steps+=1;
      if(y_steps != 0 && y_steps >0)y_steps-=1;
    }
    return false;
  }
  
  boolean attacking_own_team(int x2, int y2, ArrayList<Piece> pieces, int index){
    for(Piece p: pieces){
      if(index != pieces.indexOf(p) && white == p.white && x2 == p.x && y2 == p.y)return true;
    }
    
    return false;
  }
  
}

class Queen extends Piece{
  
  Queen(int x, int y, boolean white){
    super(x, y, white);
    if(white)img = chess_pieces.get(200,0,200, 200);
    if(!white)img = chess_pieces.get(200,200,200, 200);
    img.resize(ts,0);
  }
  
  boolean can_move(int x2, int y2, Board board, int index){
    if(passed_through(x2, y2, board.pieces,index))return false;
    if(attacking_own_team(x2, y2, board.pieces,index))return false;
    if(x2 == x||y2 == y||abs(x-x2) == abs(y-y2)){
      return true;
    }
    
    return false;
  }
  
}

class Pawn extends Piece{
  boolean firstMove = true;
  Pawn(int x, int y, boolean white){
    super(x, y, white);
    if(white)img = chess_pieces.get(1000,0,200, 200);
    if(!white)img = chess_pieces.get(1000,200,200, 200);
    img.resize(ts,0);
  }
  
  boolean can_move(int x2, int y2, Board board, int index){
    if(passed_through(x2, y2, board.pieces,index))return false;
    if(attacking_own_team(x2, y2, board.pieces,index))return false;
    if(
    ((firstMove && x2 == x) 
    && 
    ((!white && y2 - y == 2)||(white && y - y2 == 2)))
    ||
    (x2 == x &&((!white && y2 - y == 1)||(white && y - y2 == 1))&& !piece_at(x2, y2, board.pieces, index))
    ||
    (piece_at(x2, y2, board.pieces, index)&&((white && abs(x - x2) == y - y2)  ||  (!white && abs(x-x2) == y2 - y)))
    ){
      firstMove = false;
      return true;
    }
    
    
    return false;
  }
  
}

class Knight extends Piece{
  
  Knight(int x, int y, boolean white){
    super(x, y, white);
    if(white)img = chess_pieces.get(600,0,200, 200);
    if(!white)img = chess_pieces.get(600,200,200, 200);
    img.resize(ts,0);
  }
  
  boolean can_move(int x2, int y2, Board board, int index){
    if(attacking_own_team(x2, y2, board.pieces,index))return false;
    if((abs(x2-x)==1 && abs(y2-y)==2) || (abs(x2-x)==2 && abs(y2-y)==1)){
      return true;
    }
    
    return false;
  }
  
}

class Rook extends Piece{
  
  Rook(int x, int y, boolean white){
    super(x, y, white);
    if(white)img = chess_pieces.get(800,0,200, 200);
    if(!white)img = chess_pieces.get(800,200,200, 200);
    img.resize(ts,0);
  }
  
  boolean can_move(int x2, int y2, Board board, int index){
    if(attacking_own_team(x2, y2, board.pieces,index))return false;
    if(passed_through(x2, y2, board.pieces,index))return false;
    if(x2 == x||y2 == y){
      return true;
    }
    
    return false;
  }
  
}

class Bishop extends Piece{
  
  Bishop(int x, int y, boolean white){
    super(x, y, white);
    if(white)img = chess_pieces.get(400,0,200, 200);
    if(!white)img = chess_pieces.get(400,200,200, 200);
    img.resize(ts,0);
  }
  
  boolean can_move(int x2, int y2, Board board, int index){
    if(attacking_own_team(x2, y2, board.pieces,index))return false;
    if(passed_through(x2, y2, board.pieces,index))return false;
    if(abs(x-x2) == abs(y-y2)){
      return true;
    }
    
    return false;
  }
  
}
