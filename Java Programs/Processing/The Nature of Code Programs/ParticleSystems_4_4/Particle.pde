class Particle {
  PVector location, velocity, acceleration;
  float lifespan = 255;
  
  
  Particle(PVector l) {
    location = new PVector(l.x, l.y);
    velocity = new PVector(random(-1, 1), random(-1, 1));
    acceleration = new PVector(0,0);
  }
  
  void applyForce(PVector force) {
    acceleration.add(force);
  }
  
  void update() {
    velocity.add(acceleration);
    location.add(velocity);
    lifespan -= 2;
    acceleration.mult(0);
  }
  
  void display() {
    stroke(0, lifespan);
    strokeWeight(2);
    fill(127, lifespan);
    ellipse(location.x, location.y, 12, 12);
  }
  
  boolean isDead() {
    if (lifespan <= 0) {
      return true;
    } else {
      return false;
    }
  }
  
}
