
ArrayList<ParticleSystem> particleSystem;
PVector location;
void setup() {
  size(640, 340);
  particleSystem = new ArrayList<ParticleSystem>();
  
}

void draw() {
  background(255);
  PVector gravity = new PVector(0, 0.05);
  PVector windR = new PVector(0.05, 0);
  PVector windL = new PVector(-0.05, 0);
  
  for (ParticleSystem ps: particleSystem){
    ps.addParticle();
    ps.run();
    ps.applyForce(gravity);
    if (mousePressed) {
      ps.applyForce(windR);
    } else {
      ps.applyForce(windL);
    }
  }
}


void mousePressed() {
  location = new PVector(mouseX, mouseY);
}

void mouseReleased(){
  particleSystem.add(new ParticleSystem(location));
}
