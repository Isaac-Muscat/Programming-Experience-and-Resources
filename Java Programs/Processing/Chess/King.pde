class King extends Piece{
  boolean was_checked = false;
  King(int x, int y, boolean white){
    super(x, y, white);
    if(white)img = chess_pieces.get(0,0,200, 200);
    if(!white)img = chess_pieces.get(0,200,200, 200);
    img.resize(ts,0);
  }
  
  boolean can_move(int x2, int y2, Board board, int index){
    if(passed_through(x2, y2, board.pieces,index))return false;
    if(attacking_own_team(x2, y2, board.pieces,index))return false;
    if(abs(x-x2) <= 1 && abs(y-y2) <= 1){
      return true;
    }
    return false;
  }
  
}
