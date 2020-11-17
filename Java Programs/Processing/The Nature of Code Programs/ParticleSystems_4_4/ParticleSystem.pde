class ParticleSystem {
  ArrayList<Particle> particles;
  PVector l;
  int particleType;
  
  ParticleSystem(PVector l) {
    particles = new ArrayList<Particle>();
    this.l = l;
    particleType = int(random(1,4));
  }
  
  void applyForce(PVector force) {
    for (Particle p : particles) {
      p.applyForce(force);
    }
  }
  void addParticle() {
    if (particleType == 1) {
      particles.add(new Particle(l));
    } else if (particleType == 2) {
      particles.add(new SquareParticle(l));
    } else if (particleType == 3) {
      particles.add(new RotatingParticle(l));
    }
  }
  
  void run() {
    for (int i = particles.size()-1; i >= 0; i--) {
      Particle p = particles.get(i);
      p.update();
      p.display();
      
      if (p.isDead()){
        particles.remove(i);
      }
    }
    
  }
  
  
  
  
}
