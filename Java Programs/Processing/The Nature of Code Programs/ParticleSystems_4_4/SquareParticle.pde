class SquareParticle extends Particle {
  SquareParticle(PVector l) {
    super(l);
  }
  
  void display() {
    fill(127, lifespan);
    stroke(0);
    rectMode(CENTER);
    rect(location.x, location.y, 12, 12);
  }
  
  
  
}
