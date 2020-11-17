class RotatingParticle extends Particle {
  float angle, aVelocity, aAcceleration;
  RotatingParticle(PVector l) {
    super(l);
    angle = random(1, 360);
    aVelocity = random(-0.1, 0.1);
    aAcceleration = random(-0.005, 0.005);
  }
  
  void display() {
    pushMatrix();
    translate(location.x, location.y);
    rotate(angle);
    fill(127, lifespan);
    stroke(0);
    rectMode(CENTER);
    rect(0, 0, 12, 12);
    popMatrix();
  }
  
  void update() {
    aVelocity += aAcceleration;
    angle += aVelocity;
    super.update();
  }
  
}
